import pandas as pd
import re

# Membaca data dan melewati baris yang rusak
df = pd.read_csv('data_group.csv', encoding='latin1', on_bad_lines='skip')

df.head()

# Hapus baris yang kosong
df = df.dropna(subset=['text'])  # Ganti 'text_column' dengan nama kolom teks Anda

# Fungsi untuk membersihkan teks
def clean_text(text):
    # Hanya menyisakan huruf, angka, dan tanda baca
    return re.sub(r'[^a-zA-Z0-9.,!? ]+', '', text)

# Terapkan fungsi ke kolom teks
df['cleaned_text'] = df['text'].apply(clean_text)

# Tampilkan data yang sudah dibersihkan
df.head()

# Simpan ke file CSV baru
df.to_csv('cleaned_data_group.csv', index=False)

print("Pembersihan selesai. Data disimpan di 'cleaned_data_group.csv'")