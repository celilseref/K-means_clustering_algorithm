import pandas as pd
from sklearn.cluster import KMeans

# Excel dosyasını okuyup verileri bir veri çerçevesine yükleme
print("Excel dosyası okunuyor...")
df = pd.read_excel('2D_clustering_data.xlsx')

# Kullanmak istediğiniz özellikleri seçme (örneğin, 'Özellik1' ve 'Özellik2')
features = ['x', 'y','color']
print("Seçilen özellikler: ", features)

# Seçilen özelliklere göre verileri alıp bir dizi oluşturma
X = df[features].values

# K-means algoritmasını uygulama
k = 3  # Küme sayısı
kmeans = KMeans(n_clusters=k)
print("K-means algoritması uygulanıyor...")
kmeans.fit(X)

# Küme etiketlerini alıp veri çerçevesine ekleme
df['Kume'] = kmeans.labels_
print("Kümeler oluşturuldu.")

# Düzenlenmiş verileri yeni bir Excel dosyasına yazma
print("Düzenlenmiş veriler yeni Excel dosyasına yazılıyor...")
df.to_excel('new.xlsx', index=False)
print("Yeni Excel dosyası oluşturuldu: new.xlsx")
