#Pengambilan keputusan dengan if dan else
angka = 8
angka = 7

if angka % 2 == 0:
    print("maka angka genap")
else:
    print("maka angka ganjil")

umur = 18

if umur >= 17:
    print("Sudah cukup umur")
else:
    print("Belum cukup umur")

x = 10

if x > 5:
    print("A")
else:
    print("B")

#IF → kondisi benar, ELSE → kondisi salah
#Tapi bagaimana kalau kita punya lebih dari 2 kondisi? maka kita gunakan ELIF (else if) untuk menambahkan kondisi lain. Contohnya seperti ini:
nilai = 85

if nilai >= 90:
    print("Nilai A")
elif nilai >= 80 and nilai <= 89:
    print("Nilai B")
elif nilai >= 70 and nilai <= 79:
    print("Nilai C")
elif nilai >= 60 and nilai <= 69:
    print("Nilai D")
elif nilai >= 50:
    print("Nilai E")
else:
    print("Nilai D atau E")

#sekarang masuk operator perbandingan, operator perbandingan digunakan untuk membandingkan dua nilai. Operator perbandingan akan menghasilkan nilai boolean True atau False. Berikut adalah operator perbandingan yang umum digunakan:
#1. Sama dengan (==)
umur = 20

if umur >= 17:
    print("Boleh membuat KTP")
else:
    print("Belum cukup umur")

#Sekarang kita naik satu tingkat: operator logika.
#and
umur = 20 #true
punya_ktp = True #true

if umur >= 17 and punya_ktp:
    print("Boleh mendaftar")
else:
    print("Tidak boleh mendaftar")

umur = 20 #true
punya_ktp = False #false

if umur >= 17 and punya_ktp:
    print("Boleh mendaftar")
else:
    print("Tidak boleh mendaftar")

#or
hari = "Minggu"

if hari == "Sabtu" or hari == "Minggu":
    print("Hari libur")
else:
    print("Hari kerja")

#not
login = False

if not login:
    print("Silakan login")
else:
    print("Selamat datang")
