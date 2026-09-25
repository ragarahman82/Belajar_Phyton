#Perulangan digunakan ketika kita ingin menjalankan kode berulang kali.
for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(1,11):
    print(i)

for i in range(11,1):
    print(i)

#range(start, stop, step)
for i in range(1, 11, 2):
    print(i)

for i in range(10, 0, -1):
    print(i)

#Nah, sekarang kita gabungkan materi lama (if) dengan materi baru (for).
for i in range(1, 11):
    if i % 2 == 0:
        print(i)