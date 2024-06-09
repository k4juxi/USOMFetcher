# USOMFetcher
Bu projede USOM'un API'ını kullanarak zararlı IP ve Domainler ayrı ayrı .txt dosyalara yazılarak çıktılar üretiyor. Ve son fetch edilen ID ve son fetch edilen ID'den önceki ID de "last_fetched_id.txt" içerisinde bulunmaktadır. Böylece günde 1 defa çalışacak şekilde schedule edilirse önceki last fetch id'den sonraki IoC'leri günlük olarak alıp güvenlik sistemleriniz de kullanabilirsiniz.

