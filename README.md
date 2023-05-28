# K-means_clustering_algorithm
Kmeans algoritması, veri kümesini, her veri noktasının yalnızca bir gruba ait olduğu, K adet önceden tanımlanmış, birbiriyle örtüşmeyen alt gruba (küme) bölmeye çalışan yinelemeli bir algoritmadır. Küme içi veri noktalarını mümkün olduğunca benzer hale getirmeye ve aynı zamanda kümeleri mümkün olduğunca farklı (uzak) tutmaya çalışır. Veri noktaları ile kümenin ağırlık merkezi (o kümeye ait tüm veri noktalarının aritmetik ortalaması) arasındaki mesafenin karesi toplamı minimumda olacak şekilde veri noktalarını bir kümeye atar. Kümeler içinde ne kadar az varyasyona sahip olursak, veri noktaları aynı küme içinde o kadar homojen (benzer) olur.

İlk olarak, pandas kütüphanesini ve sklearn.cluster modülünden KMeans sınıfını içe aktarıyoruz.
Excel dosyasını pd.read_excel fonksiyonunu kullanarak bir veri çerçevesine yüklüyoruz ve df değişkenine atıyoruz.
Kullanmak istediğimiz özellikleri (sütunları) seçiyoruz ve features listesine atıyoruz.
Seçilen özelliklere göre verileri df[features].values ifadesiyle bir dizi olarak alıyoruz ve X değişkenine atıyoruz.
K-means algoritmasını uygulamak üzere bir KMeans nesnesi oluşturuyoruz. n_clusters parametresiyle küme sayısını belirtiyoruz. Bu örnekte k = 3 olarak ayarlanmış.
K-means algoritmasını verilere uyguluyoruz. kmeans.fit(X) ifadesiyle eğitim gerçekleştiriliyor.
K-means algoritmasının her bir veri noktasını hangi küme etiketine atadığını kmeans.labels_ özelliği ile alıyoruz ve bu etiketleri df veri çerçevesine yeni bir sütun olarak ekliyoruz.
Düzenlenmiş verileri df.to_excel yöntemiyle yeni bir Excel dosyasına yazıyoruz. index=False parametresi, indeks sütununu kaydetmemizi engeller.
Son olarak, oluşturulan Excel dosyasının adını new.xlsx olarak belirterek bir çıktı mesajı veriyoruz.
Bu şekilde, k-means kümeleme algoritması uygulanır ve her veri noktası bir küme etiketiyle etiketlenerek düzenlenmiş veriler yeni bir Excel dosyasına yazılır.
