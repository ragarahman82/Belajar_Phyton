teman = ["Andi", "Budi", "Citra"]

print(teman[0])
print(teman[1])
print(teman[2])

#menggunakan list dengan loop 
buah = ["Apel", "Jeruk", "Mangga"]

for item in buah:
    print(item)


#Len() : untuk mengetahui berapa banyak data yang ada di dalam list.
buah = ["Apel", "Jeruk", "Mangga"]

print(len(buah))

#Insert : untuk menambahkan data ke dalam list pada posisi tertentu.
buah = ["Apel", "Mangga"]

buah.insert(1, "Jeruk")

print(buah)

#pop() : untuk menghapus data dari list berdasarkan index.
buah = ["Apel", "Jeruk", "Mangga"]

buah.pop(1)

print(buah)

#sort() : untuk mengurutkan data di dalam list.
angka = [5, 2, 8, 1, 3]

angka.sort()

print(angka)

