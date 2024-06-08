import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn3

# Mengatur seed untuk reproduktifitas
np.random.seed(42)

# Data tentang jenis perilaku agresif dan frekuensi kejadian
data_agresif = {
    "Jenis Perilaku Agresif": [
        "Ngebut", 
        "Melanggar Lampu Merah", 
        "Memotong Jalur", 
        "Berkendara Sambil Main HP", 
        "Tidak Menggunakan Helm",
        "Membuntuti Terlalu Dekat",
        "Mengklakson Berlebihan",
        "Berkendara di Jalur Lawan",
        "Berkendara dengan Kecepatan Tidak Stabil",
        "Balapan Liar"
    ],
    "Frekuensi Kejadian": np.random.randint(50, 200, size=10),
    "Usia (Tahun)": np.random.randint(15, 25, size=10),
    "Potensi Kejadian per Bulan (Jiwa)": np.random.randint(5, 20, size=10)
}

# Data tentang potensi kecelakaan dan frekuensi kejadian
data_kecelakaan = {
    "Potensi Kecelakaan": [
        "Kecelakaan Tabrak Depan", 
        "Kecelakaan Tabrak Samping", 
        "Kecelakaan Serempetan", 
        "Kecelakaan Tabrak Belakang", 
        "Cidera Kepala",
        "Kecelakaan Beruntun",
        "Kecelakaan Karena Panik",
        "Kecelakaan Tabrak Depan",
        "Kecelakaan Karena Kehilangan Kendali",
        "Kecelakaan Parah"
    ],
    "Frekuensi Kejadian": np.random.randint(30, 150, size=10),
    "Usia (Tahun)": np.random.randint(15, 25, size=10),
    "Potensi Kejadian per Bulan (Jiwa)": np.random.randint(5, 20, size=10)
}

# Data tentang faktor penyebab dan frekuensi kejadian
data_penyebab = {
    "Faktor Penyebab": [
        "Keinginan untuk cepat sampai", 
        "Tidak sabar menunggu", 
        "Kurang disiplin", 
        "Distraksi", 
        "Mengabaikan keselamatan",
        "Tidak menjaga jarak aman",
        "Mengungkapkan frustrasi",
        "Kebut-kebutan",
        "Kurangnya kontrol emosi",
        "Adrenalin dan tantangan"
    ],
    "Frekuensi Kejadian": np.random.randint(40, 180, size=10),
    "Usia (Tahun)": np.random.randint(15, 25, size=10),
    "Potensi Kejadian per Bulan (Jiwa)": np.random.randint(5, 20, size=10)
}

# Data tentang upaya pencegahan dan frekuensi penerapan
data_pencegahan = {
    "Upaya Pencegahan": [
        "Edukasi tentang bahaya ngebut dan pentingnya keselamatan", 
        "Peningkatan disiplin berlalu lintas", 
        "Penegakan hukum yang lebih ketat", 
        "Kampanye bahaya penggunaan HP saat berkendara", 
        "Penyuluhan tentang pentingnya penggunaan helm",
        "Edukasi tentang jarak aman",
        "Kampanye tentang ketenangan saat berkendara",
        "Penegakan hukum yang lebih ketat",
        "Pelatihan pengendalian emosi",
        "Operasi razia dan edukasi"
    ],
    "Frekuensi Penerapan": np.random.randint(20, 100, size=10),
    "Usia (Tahun)": np.random.randint(15, 25, size=10),
    "Potensi Kejadian per Bulan (Jiwa)": np.random.randint(5, 20, size=10)
}

# Membuat DataFrames
df_agresif = pd.DataFrame(data_agresif)
df_kecelakaan = pd.DataFrame(data_kecelakaan)
df_penyebab = pd.DataFrame(data_penyebab)
df_pencegahan = pd.DataFrame(data_pencegahan)

# Menampilkan DataFrames
print("Tabel Jenis Perilaku Agresif dan Frekuensi Kejadian")
print(df_agresif)
print("\nTabel Potensi Kecelakaan dan Frekuensi Kejadian")
print(df_kecelakaan)
print("\nTabel Faktor Penyebab dan Frekuensi Kejadian")
print(df_penyebab)
print("\nTabel Upaya Pencegahan dan Frekuensi Penerapan")
print(df_pencegahan)

# Analisis deskriptif
print("\nAnalisis Deskriptif")
print("Jenis Perilaku Agresif")
print(df_agresif.describe())

print("\nPotensi Kecelakaan")
print(df_kecelakaan.describe())

print("\nFaktor Penyebab")
print(df_penyebab.describe())

print("\nUpaya Pencegahan")
print(df_pencegahan.describe())

# Visualisasi Data
sns.set(style="whitegrid")

# Visualisasi Frekuensi Kejadian Perilaku Agresif
plt.figure(figsize=(12, 6))
sns.barplot(x="Frekuensi Kejadian", y="Jenis Perilaku Agresif", data=df_agresif, palette="viridis")
plt.title("Frekuensi Kejadian Jenis Perilaku Agresif")
plt.xlabel("Frekuensi Kejadian")
plt.ylabel("Jenis Perilaku Agresif")
plt.show()

# Visualisasi Potensi Kecelakaan
plt.figure(figsize=(12, 6))
sns.barplot(x="Frekuensi Kejadian", y="Potensi Kecelakaan", data=df_kecelakaan, palette="magma")
plt.title("Frekuensi Kejadian Potensi Kecelakaan")
plt.xlabel("Frekuensi Kejadian")
plt.ylabel("Potensi Kecelakaan")
plt.show()

# Visualisasi Faktor Penyebab
plt.figure(figsize=(12, 6))
sns.barplot(x="Frekuensi Kejadian", y="Faktor Penyebab", data=df_penyebab, palette="coolwarm")
plt.title("Frekuensi Kejadian Faktor Penyebab")
plt.xlabel("Frekuensi Kejadian")
plt.ylabel("Faktor Penyebab")
plt.show()

# Visualisasi Upaya Pencegahan
plt.figure(figsize=(12, 6))
sns.barplot(x="Frekuensi Penerapan", y="Upaya Pencegahan", data=df_pencegahan, palette="plasma")
plt.title("Frekuensi Penerapan Upaya Pencegahan")
plt.xlabel("Frekuensi Penerapan")
plt.ylabel("Upaya Pencegahan")
plt.show()

# Visualisasi Hubungan antara Usia dan Frekuensi Kejadian untuk Semua Data
plt.figure(figsize=(14, 8))

plt.subplot(2, 2, 1)
sns.scatterplot(x="Usia (Tahun)", y="Frekuensi Kejadian", data=df_agresif)
plt.title("Usia vs Frekuensi Kejadian (Perilaku Agresif)")
plt.xlabel("Usia (Tahun)")
plt.ylabel("Frekuensi Kejadian")

plt.subplot(2, 2, 2)
sns.scatterplot(x="Usia (Tahun)", y="Frekuensi Kejadian", data=df_kecelakaan)
plt.title("Usia vs Frekuensi Kejadian (Kecelakaan)")
plt.xlabel("Usia (Tahun)")
plt.ylabel("Frekuensi Kejadian")

plt.subplot(2, 2, 3)
sns.scatterplot(x="Usia (Tahun)", y="Frekuensi Kejadian", data=df_penyebab)
plt.title("Usia vs Frekuensi Kejadian (Faktor Penyebab)")
plt.xlabel("Usia (Tahun)")
plt.ylabel("Frekuensi Kejadian")

plt.subplot(2, 2, 4)
sns.scatterplot(x="Usia (Tahun)", y="Frekuensi Penerapan", data=df_pencegahan)
plt.title("Usia vs Frekuensi Penerapan (Upaya Pencegahan)")
plt.xlabel("Usia (Tahun)")
plt.ylabel("Frekuensi Penerapan")

plt.tight_layout()
plt.show()

# Histogram Frekuensi Kejadian Perilaku Agresif
plt.figure(figsize=(10, 6))
sns.histplot(df_agresif["Frekuensi Kejadian"], bins=10, kde=True, color='blue')
plt.title("Distribusi Frekuensi Kejadian Perilaku Agresif")
plt.xlabel("Frekuensi Kejadian")
plt.ylabel("Jumlah Kejadian")
plt.show()

# Pie Chart Potensi Kecelakaan
plt.figure(figsize=(8, 8))
plt.pie(df_kecelakaan["Frekuensi Kejadian"], labels=df_kecelakaan["Potensi Kecelakaan"], autopct='%1.1f%%', startangle=140, colors=sns.color_palette("coolwarm", 10))
plt.title("Distribusi Potensi Kecelakaan")
plt.axis('equal')
plt.show()

# Diagram Venn Faktor Penyebab
plt.figure(figsize=(10, 6))
venn3(subsets=(10, 10, 10, 10, 10, 10, 10), set_labels=("Keinginan untuk cepat sampai", "Tidak sabar menunggu", "Kurang disiplin"))
plt.title("Diagram Venn Faktor Penyebab")
plt.show()

# Analisis Statistik
print("\nAnalisis Statistik")

# Menghitung rata-rata usia untuk setiap jenis perilaku agresif
mean_usia_agresif = df_agresif["Usia (Tahun)"].mean()
print(f"Rata-rata Usia untuk Perilaku Agresif: {mean_usia_agresif}")

# Menghitung rata-rata frekuensi kejadian untuk setiap jenis potensi kecelakaan
mean_frek_kecelakaan = df_kecelakaan["Frekuensi Kejadian"].mean()
print(f"Rata-rata Frekuensi Kejadian untuk Potensi Kecelakaan: {mean_frek_kecelakaan}")

# Menghitung standar deviasi frekuensi kejadian untuk faktor penyebab
std_frek_penyebab = df_penyebab["Frekuensi Kejadian"].std()
print(f"Standar Deviasi Frekuensi Kejadian untuk Faktor Penyebab: {std_frek_penyebab}")

# Menghitung median frekuensi penerapan untuk upaya pencegahan
median_frek_pencegahan = df_pencegahan["Frekuensi Penerapan"].median()
print(f"Median Frekuensi Penerapan untuk Upaya Pencegahan: {median_frek_pencegahan}")

# Analisis korelasi antara usia dan frekuensi kejadian pada perilaku agresif
correlation_agresif = df_agresif[["Usia (Tahun)", "Frekuensi Kejadian"]].corr()
print("\nKorelasi antara Usia dan Frekuensi Kejadian (Perilaku Agresif):")
print(correlation_agresif)

# Visualisasi korelasi antara usia dan frekuensi kejadian pada perilaku agresif
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_agresif, annot=True, cmap="coolwarm")
plt.title("Korelasi antara Usia dan Frekuensi Kejadian (Perilaku Agresif)")
plt.show()

# Analisis korelasi antara usia dan frekuensi kejadian pada potensi kecelakaan
correlation_kecelakaan = df_kecelakaan[["Usia (Tahun)", "Frekuensi Kejadian"]].corr()
print("\nKorelasi antara Usia dan Frekuensi Kejadian (Potensi Kecelakaan):")
print(correlation_kecelakaan)

# Visualisasi korelasi antara usia dan frekuensi kejadian pada potensi kecelakaan
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_kecelakaan, annot=True, cmap="magma")
plt.title("Korelasi antara Usia dan Frekuensi Kejadian (Potensi Kecelakaan)")
plt.show()

# Analisis korelasi antara usia dan frekuensi kejadian pada faktor penyebab
correlation_penyebab = df_penyebab[["Usia (Tahun)", "Frekuensi Kejadian"]].corr()
print("\nKorelasi antara Usia dan Frekuensi Kejadian (Faktor Penyebab):")
print(correlation_penyebab)

# Visualisasi korelasi antara usia dan frekuensi kejadian pada faktor penyebab
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_penyebab, annot=True, cmap="coolwarm")
plt.title("Korelasi antara Usia dan Frekuensi Kejadian (Faktor Penyebab)")
plt.show()

# Analisis korelasi antara usia dan frekuensi penerapan pada upaya pencegahan
correlation_pencegahan = df_pencegahan[["Usia (Tahun)", "Frekuensi Penerapan"]].corr()
print("\nKorelasi antara Usia dan Frekuensi Penerapan (Upaya Pencegahan):")
print(correlation_pencegahan)

# Visualisasi korelasi antara usia dan frekuensi penerapan pada upaya pencegahan
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_pencegahan, annot=True, cmap="plasma")
plt.title("Korelasi antara Usia dan Frekuensi Penerapan (Upaya Pencegahan)")
plt.show()

