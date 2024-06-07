import pandas as pd
import numpy as np

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


