# USOMFetcher
Bu proje üzerinde geçmişte bir takım çalışmalar yapmıştım. Fakat iş yoğunluğundan ötürü bir türlü fırsat bulamamıştım. Bu sabah (Github:@ziyadnz Link: https://github.com/ziyadnz/USOM-Malicious-Links) Ziya'nın LinkedIn gönderisinde gördüğüm projenin(Ellerine sağlık güzel olmuş.), geçmişte kafamda olan yapısını yazıp tamamladım. 

Bu projede USOM'un API'ını kullanarak zararlı IP ve Domainler ayrı ayrı .txt dosyalara yazılarak çıktılar üretiyor. Ve son fetch edilen ID ve son fetch edilen ID'den önceki ID de "last_fetched_id.txt" içerisinde bulunmaktadır. Böylece günde 1 defa çalışacak şekilde schedule edilirse önceki last fetch id'den sonraki IoC'leri günlük olarak alıp güvenlik sistemleriniz de kullanabilirsiniz.

