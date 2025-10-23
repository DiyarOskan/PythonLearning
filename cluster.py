import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, calinski_harabasz_score
import matplotlib.pyplot as plt

# Mesafe tablosunu okuma
mesafe_tablosu = pd.read_excel(
    r"C:\Users\ASUS\OneDrive - Kadir Has University\Masaüstü\mesafe.xlsx",
    sheet_name="mesafe-(adalar)",
    index_col=0
)


# DataFrame'i matrix'e çevirme
mesafe_matrix = mesafe_tablosu.values

# Hiyerarşik kümeleme
hc = linkage(mesafe_matrix, method='ward')

# Dendrogram çizimi
plt.figure(figsize=(12, 8))
dendrogram(hc, labels=mesafe_tablosu.index.tolist())
plt.title("İstanbul İlçeleri Dendrogramı")
plt.xlabel("İlçeler")
plt.ylabel("Mesafe")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# K-means kümeleme
k = 5
km = KMeans(n_clusters=k, n_init=25, random_state=42)
kumeler = km.fit_predict(mesafe_matrix)

# Kümeleri yazdırma
print("Kümeler:")
print(kumeler)

# Kümeleme kalitesi
silhouette_avg = silhouette_score(mesafe_matrix, kumeler)
calinski_harabasz = calinski_harabasz_score(mesafe_matrix, kumeler)

print(f"\nKümeleme Kalite Metrikleri:")
print(f"Silhouette Skoru: {silhouette_avg:.4f}")
print(f"Calinski-Harabasz İndeksi: {calinski_harabasz:.4f}")

# Her ilçeyi hangi kümeye ait olduğunu gösteren tablo
ilce_kumeleri = pd.DataFrame({
    'İlçe': mesafe_tablosu.index,
    'Kümeler': kumeler
})
print("\nİlçe-Küme Eşleşmeleri:")
print(ilce_kumeleri)

# Farklı küme sayıları için kalite metriklerini karşılaştırma
print("\nFarklı Küme Sayıları için Karşılaştırma:")
k_values = range(2, 8)
silhouette_scores = []
calinski_scores = []

for k_val in k_values:
    kmeans = KMeans(n_clusters=k_val, n_init=25, random_state=42)
    cluster_labels = kmeans.fit_predict(mesafe_matrix)

    silhouette_avg = silhouette_score(mesafe_matrix, cluster_labels)
    calinski_harabasz_val = calinski_harabasz_score(mesafe_matrix, cluster_labels)

    silhouette_scores.append(silhouette_avg)
    calinski_scores.append(calinski_harabasz_val)

    print(f"k={k_val}: Silhouette={silhouette_avg:.4f}, Calinski-Harabasz={calinski_harabasz_val:.4f}")

# Grafik çizimi
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(k_values, silhouette_scores, 'bo-')
plt.xlabel('Küme Sayısı (k)')
plt.ylabel('Silhouette Skoru')
plt.title('Silhouette Skoruna Göre Optimal k Değeri')
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(k_values, calinski_scores, 'ro-')
plt.xlabel('Küme Sayısı (k)')
plt.ylabel('Calinski-Harabasz İndeksi')
plt.title('Calinski-Harabasz İndeksine Göre Optimal k Değeri')
plt.grid(True)

plt.tight_layout()
plt.show()

# Her bir nokta için silhouette skorlarını hesaplama (isteğe bağlı)
from sklearn.metrics import silhouette_samples

silhouette_vals = silhouette_samples(mesafe_matrix, kumeler)

# Her küme için ortalama silhouette skoru
ilce_kumeleri['Silhouette_Skoru'] = silhouette_vals
print("\nKümelere Göre Silhouette Skorları:")
for i in range(k):
    cluster_silhouette = silhouette_vals[kumeler == i]
    print(f"Küme {i}: Ortalama Silhouette = {cluster_silhouette.mean():.4f} (N={len(cluster_silhouette)})")