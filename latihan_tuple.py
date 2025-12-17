# Tuple digunakan untuk menyimpan beberapa item dalam satu variabel.
# Tuple adalah kumpulan yang terurut dan tidak dapat diubah .
# Tuple ditulis dengan tanda kurung ()
# saya mau menulis tuple dalam variabel mahasiswa
mahasiswa = ("Hilmi", "Nazila", "Williyana", "Shafwa", "Riza", "Glish", "Aulia", "Lila")
# INDEKS        0         1          2           3        4        5       6        7
# INDEKS -      -8        -7         -6          -5       -4       -3      -2       -1
print (mahasiswa)
# Panjang Tuple
# Untuk menentukan berapa banyak item yang dimiliki sebuah tuple, gunakan fungsi len ()
print(len(mahasiswa))

# Buat tuple dengan satu item
mahasiswa = ("Hilmi")
print(mahasiswa)
# tuple juga bisa berisi tipe data yang berbeda
mahasiswa = ("Hilmi", 28, True, "Informatika")
print(mahasiswa)
# Tipe Data Tuple adalah "tuple"
print(type(mahasiswa))
# mengecek apakah sebuah item ada dalam tuple
mahasiswa = ("Hilmi", "Nazila", "Williyana", "Shafwa", "Riza", "Glish", "Aulia", "Lila")
if "Hilmi" in mahasiswa:
    print("Ya, 'Hilmi' ada dalam tuple mahasiswa")

print ("---AKSES TUPLE---")
# Tuple di akses berdasarkan nomor indeksnya
# saya mau mengakses item ke dua dari tuple
mahasiswa = ("Hilmi", "Nazila", "Williyana", "Shafwa", "Riza", "Glish", "Aulia", "Lila")
print(mahasiswa[1])
# indeks negatif
print(mahasiswa[-2])
# rentang indeks
print(mahasiswa[0:4])
# rentang indeks negatif
print(mahasiswa[-4:-1])

print("---MEMPERBARUI TUPLE---")
# Tuple tidak dapat diubah setelah dibuat, tetapi ada cara untuk memperbarui tuple.
# Karena tuple bersifat immutable, kita tidak bisa langsung mengubah elemen.
# Namun, kita bisa mengubah tuple menjadi list, memperbarui elemen, lalu mengubahnya kembali menjadi tuple.
# mengubah item tuple, konversi dulu tuple menjadi list
mahasiswa_list = list(mahasiswa)
mahasiswa_list[4] = "Dewi"
mahasiswa = tuple(mahasiswa_list)
print(mahasiswa)
# menambah item ke tuple
mahasiswa_list = list(mahasiswa)
mahasiswa_list.append("Dewi")
mahasiswa = tuple(mahasiswa_list)
print(mahasiswa)
# menambah tuple ke tuple
mahasiswa_baru = ("Allia","Riza", "Lita")
mahasiswa += mahasiswa_baru
print(mahasiswa)

# menghapus item dari tuple (konversi dulu ke list)
mahasiswa_list = list(mahasiswa)
mahasiswa_list.remove("Lita")
mahasiswa = tuple(mahasiswa_list)
print(mahasiswa)
# Kita juga dapat menghapus tuple sepenuhnya menggunakan kata kunci del
# del mahasiswa
# print (mahasiswa) # ini akan menyebabkan error karena tuple sudah dihapus

print ("---UNPACKING/MENGURAI TUPLE---")
# unpacking tuple
TEKNOLOGI = ("Jaringan", "Komputer", "Software")
jaringan, komputer, software = TEKNOLOGI
print(jaringan)
print (komputer)
print (software)
# menggunakan arterisk *
# jika jumlah variabel kurang dari jumlah item tuple, gunakan asterisk * pada variabel terakhir
TEKNOLOGI = ("Jaringan", "Komputer", "Software", "Hardware", "Brainware")
jaringan, *komputer = TEKNOLOGI
print(jaringan)
print (komputer)

print ("---PERULANGAN TUPLE---")
# perulangan for
mahasiswa = ("Hilmi", "Nazila", "Williyana", "Shafwa", "Riza", "Glish", "Aulia", "Lila")
for h in mahasiswa:
    print(h)
# perulangan for merujuk pada nomor indeks
for h in range(len(mahasiswa)):
    print(mahasiswa[h])
# menggunakan perulangan while
h = 0
while h < len(mahasiswa):
    print(mahasiswa[h])
    h += 1

print ("---MENGGABUNGKAN TUPLE---")
# saya mau menggabungkan tiga tuple
yokkbisa = ("Lulua", "Tia","Lia","Hilmia")
tgl_lahir = (7, 4, 1, 28)
Bulan = ("Februari", "September", "April", "Februari")

tuple_gabungan = yokkbisa + tgl_lahir + Bulan
print(tuple_gabungan)

# mengalikan tuple
yokkbisa = ("Lulua", "Tia","Lia","Hilmia")
thistuple = yokkbisa * 2
print(thistuple)

print ("---METODE COUNT DAN INDEX DALAM TUPLE---")
# METODE Count () dalam tuple
# metode ini digunakan untuk menghitung berapa kali sebuah item muncul dalam tuple
TEKNOLOGI = ("Jaringan", "Komputer", "Software", "Hardware", "Brainware", "Jaringan")
print(TEKNOLOGI.count("Jaringan"))

# metode index ()
# digunakan untuk menemukan indeks dari item ke lima yang cocok
print(TEKNOLOGI.index("Brainware"))