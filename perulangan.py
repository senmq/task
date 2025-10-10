# Soal 1
teman = ["Aldi", "Budi", "Citra", "Dewi", "Eka"]

for nama in teman:
    print(nama)

# Maka akan menampilkan nama baru yang ditambahkan

# Soal 2
i = 1
while i <= 20:
    if (i % 2 == 0):
        print(i)

    i += 1

# Maka akan terjadi perulangan secara terus menerus

# Soal 3
r = float(input("Masukkan jari-jari: "))
def luas_lingkaran(r):
    PI = 3.14
    luas = PI * (r * r)
    print(luas)

luas_lingkaran(r)

# 314.0

# Soal 4
daftar_teman = ["Aldi", "Budi", "Citra", "Dewi", "Eka"]
def sapa_semua(daftar_teman):
    for nama in daftar_teman:
        print(f"Halo, {nama}!")

sapa_semua(daftar_teman)

# Hasil: Rina Doni Sari Andi Lina

# Soal 5
nilai = [80, 75, 90, 85, 70]
def rata_rata(daftar_nilai):
    hasil = sum(daftar_nilai) / len(daftar_nilai)
    print("Rata-rata nilai siswa adalah:", hasil)

rata_rata(nilai)

# 80.0
