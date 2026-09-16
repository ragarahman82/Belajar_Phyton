#str    → teks, int    → bilangan bulat, float  → bilangan desimal, bool   → True / False, bool   → True / False

nama = "Raga"       # str
umur = 20           # int
tinggi = 170.5      # float
mahasiswa = True    # bool

#String
nama = "Raga"

print(type(nama))

#Integer
umur = 20
jumlah = 100
tahun = 2026

print(type(umur))
print(type(jumlah))
print(type(tahun))

#Float
tinggi = 170.5
berat = 60.5
harga = 15000.75

print(tinggi)
print(type(tinggi))
print(type(berat))
print(type(harga))

#Boolean
mahasiswa = True
sudah_lulus = False

print(mahasiswa)
print(sudah_lulus)

#Sekarang kita gabungkan semua tipe data diatas menjadi satu program sederhana, contohnya seperti ini:
nama = "Raga"
umur = 20
tinggi = 170.5
mahasiswa = True

print(nama)
print(umur)
print(tinggi)
print(mahasiswa)

#ini wajib kamu kuasai antara perbedaan ini
umur = 20  #int
umur = "20"  #str

#string > int
angka = int("20")

#int > string
angka = str(20)

#string > float
angka = float("20.5")

#int > float
angka = float(20)