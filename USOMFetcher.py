import requests

class USOMFetcher:
    def __init__(self, url_template, last_id_file):
        self.url_template = url_template
        self.last_id_file = last_id_file
        self.url_list = []
        self.ip_list = []
        self.current_last_fetched_id = None
        self.previous_last_fetched_id = self.read_last_fetched_id()

    def fetch_data(self):
        page = 0
        first_id_on_first_page = None
        while True:
            url = self.url_template.format(page)
            response = requests.get(url, headers={'accept': 'application/json'})
            response.raise_for_status()
            data = response.json()
            
            if not data['models']:  # No more data to fetch
                break

            # Store the first ID on the first page
            if page == 0 and data['models']:
                first_id_on_first_page = data['models'][0]['id']

            if self.process_data(data):
                break

            page += 1  # Move to the next page

        # Update last fetched ID to the first ID on the first page
        if first_id_on_first_page is not None:
            self.current_last_fetched_id = first_id_on_first_page
            self.write_last_fetched_id(self.current_last_fetched_id, self.previous_last_fetched_id)

    def read_last_fetched_id(self):
        try:
            with open(self.last_id_file, 'r') as file:
                lines = file.readlines()
                if lines:
                    return int(lines[0].strip())
        except FileNotFoundError:
            return None

    def write_last_fetched_id(self, current_id, previous_id):
        with open(self.last_id_file, 'w') as file:
            file.write(f"{current_id}\n")
            if previous_id is not None:
                file.write(f"{previous_id}\n")

    def process_data(self, data):
        for model in data['models']:
            if self.previous_last_fetched_id and model['id'] <= self.previous_last_fetched_id:
                return True  # Stop processing if we have reached the last fetched ID
            if model['type'] == 'domain':
                self.url_list.append(model['url'])
            else:
                self.ip_list.append(model['url'])
        return False

    def write_to_files(self, url_file='domain.txt', ip_file='ipv4.txt'):
        with open(url_file, 'w') as domain_file:
            domain_file.write("type=string\n")
            for url in self.url_list:
                domain_file.write(url + '\n')

        with open(ip_file, 'w') as ip_file:
            for ip in self.ip_list:
                ip_file.write(ip + '\n')

def main():
    url_template = 'https://www.usom.gov.tr/api/address/index?page={}'
    last_id_file = 'last_fetched_id.txt'
    usom_fetcher = USOMFetcher(url_template, last_id_file)
    
    usom_fetcher.fetch_data()
    usom_fetcher.write_to_files()
    
    print("URLs and IP addresses have been written to domain.txt and ipv4.txt respectively.")

if __name__ == "__main__":
    main()
