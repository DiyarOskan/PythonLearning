# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
from sklearn.metrics import silhouette_score, calinski_harabasz_score
from scipy.spatial.distance import squareform

# 1. Veriyi oku
best_guess_df = pd.read_excel(
    r"C:\Users\ASUS\OneDrive - Kadir Has University\Masaüstü\ilceler_arasi_sure_matrisleri.xlsx",
    sheet_name="best guess",
    index_col=0
)

# Simetrik matris
best_guess_df = (best_guess_df + best_guess_df.T) / 2
print("Veri Boyutu:", best_guess_df.shape)
print("\nİlk 5 Satır:")
print(best_guess_df.head())


# 2. Simetrik mesafe matrisini kontrol et ve numpy array'e çevir
mesafe_matrix = best_guess_df.values
print(f"\nMesafe Matrisi Boyutu: {mesafe_matrix.shape}")

# Matrisin simetrik olup olmadığını kontrol et
is_symmetric = np.allclose(mesafe_matrix, mesafe_matrix.T)
print(f"Matris simetrik mi?: {is_symmetric}")

# 3. Hiyerarşik Kümeleme (HC) uygulama
print("\n" + "=" * 50)
print("HİYERARŞİK KÜMELEME ANALİZİ")
print("=" * 50)

# Linkage metodları
methods = ['average', 'centroid']
Z_dict = {}

for method in methods:
    print(f"\n{method.upper()} linkage ile kümeleme yapılıyor...")

    # Mesafe matrisini üst üçgen formata (condensed) çevir
    # squareform: Simetrik matrisi üst üçgen vektör formatına çevirir
    condensed_dist = squareform(mesafe_matrix)

    # Hiyerarşik kümeleme - artık doğru formatta
    Z = linkage(condensed_dist, method=method)
    Z_dict[method] = Z

    print(f"{method} linkage tamamlandı")

# 4. Dendrogram görselleştirme
fig, axes = plt.subplots(1, 2, figsize=(20, 8))

for idx, method in enumerate(methods):
    plt.sca(axes[idx])
    dendrogram(Z_dict[method],
               labels=best_guess_df.index.tolist(),
               orientation='top',
               leaf_rotation=90,
               leaf_font_size=10)
    plt.title(f'Dendrogram - {method.capitalize()} Linkage')
    plt.xlabel('İlçeler')
    plt.ylabel('Mesafe')

plt.tight_layout()
plt.show()

# 5. Küme sayılarını değerlendirme
print("\n" + "=" * 50)
print("KÜME KALİTE DEĞERLENDİRMESİ")
print("=" * 50)

# Farklı küme sayıları için değerlendirme
kume_sayilari = range(2, 20)

results = []

for method in methods:
    print(f"\n--- {method.upper()} LINKAGE SONUÇLARI ---")

    for k in kume_sayilari:
        # Küme atamalarını al
        kumeler = fcluster(Z_dict[method], k, criterion='maxclust')

        # Kalite metriklerini hesapla
        # Mesafe matrisi kullanarak silhouette skoru hesapla
        si_score = silhouette_score(mesafe_matrix, kumeler, metric='precomputed')
        chi_score = calinski_harabasz_score(mesafe_matrix, kumeler)

        results.append({
            'method': method,
            'kume_sayisi': k,
            'silhouette': si_score,
            'calinski_harabasz': chi_score
        })

        print(f"Küme Sayısı: {k:2d} | Silhouette: {si_score:.4f} | Calinski-Harabasz: {chi_score:.4f}")

# Sonuçları DataFrame'e çevir
results_df = pd.DataFrame(results)

# 6. En iyi kümeleme yapısını seçme
print("\n" + "=" * 50)
print("EN İYİ KÜMELEME SONUÇLARI")
print("=" * 50)

# Her metod için en iyi sonuçları bul
best_results = []

for method in methods:
    method_results = results_df[results_df['method'] == method]

    # Silhouette için en iyi (en yüksek)
    best_si = method_results.loc[method_results['silhouette'].idxmax()]

    # Calinski-Harabasz için en iyi (en yüksek)
    best_chi = method_results.loc[method_results['calinski_harabasz'].idxmax()]

    best_results.append({
        'method': method,
        'best_silhouette_k': best_si['kume_sayisi'],
        'best_silhouette_score': best_si['silhouette'],
        'best_calinski_k': best_chi['kume_sayisi'],
        'best_calinski_score': best_chi['calinski_harabasz']
    })

# En iyi sonuçları göster
best_df = pd.DataFrame(best_results)
print(best_df)

# Genel en iyi kümeleme yapısını seç
overall_best_si = results_df.loc[results_df['silhouette'].idxmax()]
overall_best_chi = results_df.loc[results_df['calinski_harabasz'].idxmax()]

print(f"\nGENEL EN İYİ SONUÇLAR:")
print(
    f"En iyi Silhouette: {overall_best_si['method']} linkage, {overall_best_si['kume_sayisi']} küme, Skor: {overall_best_si['silhouette']:.4f}")
print(
    f"En iyi Calinski-Harabasz: {overall_best_chi['method']} linkage, {overall_best_chi['kume_sayisi']} küme, Skor: {overall_best_chi['calinski_harabasz']:.4f}")

# 7. Metriklerin görselleştirilmesi
fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Silhouette skorları
for method in methods:
    method_data = results_df[results_df['method'] == method]
    axes[0].plot(method_data['kume_sayisi'], method_data['silhouette'],
                 marker='o', label=method, linewidth=2)

axes[0].set_xlabel('Küme Sayısı')
axes[0].set_ylabel('Silhouette Skoru')
axes[0].set_title('Silhouette Skorları - Küme Sayısına Göre')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Calinski-Harabasz skorları
for method in methods:
    method_data = results_df[results_df['method'] == method]
    axes[1].plot(method_data['kume_sayisi'], method_data['calinski_harabasz'],
                 marker='s', label=method, linewidth=2)

axes[1].set_xlabel('Küme Sayısı')
axes[1].set_ylabel('Calinski-Harabasz Skoru')
axes[1].set_title('Calinski-Harabasz Skorları - Küme Sayısına Göre')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 8. Seçilen en iyi kümeleme için detaylı sonuç
print("\n" + "=" * 50)
print("SEÇİLEN EN İYİ KÜMELEME DETAYLARI")
print("=" * 50)

# Örnek olarak Silhouette skoru en yüksek olanı seçelim
best_method = overall_best_si['method']
best_k = overall_best_si['kume_sayisi']

final_kumeler = fcluster(Z_dict[best_method], best_k, criterion='maxclust')

# İlçe-küme eşleştirmeleri
ilce_kume_eslesme = pd.DataFrame({
    'İlçe': best_guess_df.index,
    'Küme': final_kumeler
})

print(f"Seçilen yapı: {best_method} linkage, {best_k} küme")
print("\nİlçe-Küme Dağılımı:")
print(ilce_kume_eslesme)

# Küme başına ilçe sayıları
kume_dagilimi = ilce_kume_eslesme['Küme'].value_counts().sort_index()
print(f"\nKüme Başına İlçe Sayıları:")
for kume, sayi in kume_dagilimi.items():
    print(f"Küme {kume}: {sayi} ilçe")

# Kümelere göre ilçeleri göster
print(f"\nKümelere Göre İlçeler:")
for kume_no in range(1, best_k + 1):
    kume_ilceler = ilce_kume_eslesme[ilce_kume_eslesme['Küme'] == kume_no]['İlçe'].tolist()
    print(f"Küme {kume_no} ({len(kume_ilceler)} ilçe): {', '.join(kume_ilceler)}")

# 9. 14-18 küme aralığı için detaylı analiz
print("\n" + "=" * 60)
print("14-18 KÜME ARALIĞI DETAYLI ANALİZ")
print("=" * 60)

# Her metod için 14-18 küme aralığını analiz et
for method in methods:
    print(f"\n{'=' * 40}")
    print(f"{method.upper()} LINKAGE - 14-18 KÜME ANALİZİ")
    print(f"{'=' * 40}")

    for k in range(14, 19):  # 14, 15, 16, 17, 18
        # Küme atamalarını al
        kumeler = fcluster(Z_dict[method], k, criterion='maxclust')

        # İlçe-küme eşleştirmeleri
        ilce_kume_eslesme = pd.DataFrame({
            'İlçe': best_guess_df.index,
            'Küme': kumeler
        })

        # Kalite metriklerini hesapla
        si_score = silhouette_score(mesafe_matrix, kumeler, metric='precomputed')
        chi_score = calinski_harabasz_score(mesafe_matrix, kumeler)

        print(f"\n--- {k} KÜME ---")
        print(f"Silhouette: {si_score:.4f} | Calinski-Harabasz: {chi_score:.4f}")

        # Küme başına ilçe sayıları
        kume_dagilimi = ilce_kume_eslesme['Küme'].value_counts().sort_index()
        print(f"Küme Dağılımı: {dict(kume_dagilimi)}")

        # Her küme için ilçeleri göster
        for kume_no in range(1, k + 1):
            kume_ilceler = ilce_kume_eslesme[ilce_kume_eslesme['Küme'] == kume_no]['İlçe'].tolist()
            if kume_ilceler:  # Küme boş değilse
                print(f"  Küme {kume_no:2d} ({len(kume_ilceler):2d} ilçe): {', '.join(kume_ilceler)}")

# 14-18 küme aralığı için kesim mesafelerini hesapla ve yazdır
print("\n" + "=" * 60)
print("14-18 KÜME ARALIĞI KESİM MESAFELERİ")
print("=" * 60)

for method in methods:
    print(f"\n{method.upper()} linkage dendogram kesim mesafeleri:")

    for k in range(14, 19):  # 14, 15, 16, 17, 18
        # k küme için kesim mesafesini bul
        Z = Z_dict[method]

        # Hiyerarşik kümeleme yapısından kesim mesafesini hesapla
        # k küme için kesim noktası
        kume_atamalari = fcluster(Z, k, criterion='maxclust')

        # Kesim mesafesini bulmak için:
        # 1. Tüm birleşme mesafelerini al
        mesafeler = Z[:, 2]

        # 2. k küme için kesim noktası: (n-k). birleşme
        n = len(best_guess_df.index)  # toplam örnek sayısı
        kesim_noktasi = n - k  # k küme için (n-k). birleşme

        # 3. Kesim mesafesi
        if kesim_noktasi < len(mesafeler):
            kesim_mesafesi = mesafeler[kesim_noktasi]
        else:
            kesim_mesafesi = mesafeler[-1]

        print(f"  {k} küme için kesim mesafesi: {kesim_mesafesi:.4f}")