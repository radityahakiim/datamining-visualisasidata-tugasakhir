import matplotlib.pyplot as plt
import pandas as pd

# Membaca dataset dari file CSV
df = pd.read_csv('ptjaya.csv')

# Menghapus spasi di awal dan akhir nama kolom
df.columns = df.columns.str.strip()

# Cetak nama kolom
print(df.columns)

# Cetak beberapa baris pertama dari dataset
print(df.head())

# Menampilkan ringkasan statistik
print(df.describe())

# Visualisasi Histogram Pendapatan
plt.figure(figsize=(8, 6))
plt.hist(df['Pendapatan'], bins=10, edgecolor='black')
plt.xlabel('Pendapatan (Rupiah)')
plt.ylabel('Jumlah Karyawan')
plt.title('Distribusi Pendapatan Karyawan')
plt.show()

# Scatter Plot Pendapatan vs. Jabatan
plt.figure(figsize=(8, 6))
plt.scatter(df['Jabatan'], df['Pendapatan'])
plt.xlabel('Jabatan')
plt.ylabel('Pendapatan (Rupiah)')
plt.title('Pendapatan vs. Jabatan')
plt.show()

# Box Plot Pendapatan per Jabatan
plt.figure(figsize=(8, 6))
plt.boxplot([df[df['Jabatan']=='Manajer']['Pendapatan'],
             df[df['Jabatan']=='Analis']['Pendapatan'],
             df[df['Jabatan']=='Staff']['Pendapatan']], labels=['Manajer', 'Analis', 'Staff'])
plt.ylabel('Pendapatan (Rupiah)')
plt.title('Pendapatan per Jabatan')
plt.show()
