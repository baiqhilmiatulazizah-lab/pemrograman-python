# python list / daftar
# list adalah koleksi data atau item yang berurutan dan dapat diubah juga dapat diduplikat
# list dalam python dibuat dengan tanda kurung siku []
# list digunakan untuk menyimpan beberapa data atau item dalam satu variabel

# contoh
# bentuk listnya saya gunakan kumpulan merk hp dalam variabel mylist
mylist = ["samsung", "redmi", "oppo", "vivo", "infinix", "poco", "advan","lenovo"] 
# indeks   =   0         1        2       3        4         5       6        7
# indeks negatif =  -8       -7       -6      -5       -4        -3      -2       -1
print ("mylist = ", mylist)

#item dalam list juga bisa di duplikat
mylist = ["samsung", "redmi", "oppo", "vivo", "infinix", "poco", "advan","samsung","lenovo"] 
print (mylist)

# untuk menentukan dan mengetahui jumlah item di dalam list kita bisa menggunakan fungsi len()
print (len(mylist))

#item dalam list juga dapat berupa tipe data apapun
# contoh 
list1 = ["hilmi", "nazila"] #string
list2 = [28, 27, 23] #integer
list3 = [True, False, False] #boolean
print(list1)
print(list2)
print(list3)
print (list1 + list2 + list3)
# atau bisa langsung dicampur
campuran = ("hilmi", 28, 2, True, "februari")
print (campuran)

# Dari sudut pandang Python, list didefinisikan sebagai objek dengan tipe data 'list':
# kita bisa melihatnnya dengan menggunakan fungsi type ()
print (type(mylist))

# Kita juga dapat menggunakan konstruktor list() saat membuat daftar baru.
mylist = list (("samsung", "redmi", "oppo", "vivo", "infinix", "poco", "advan","lenovo"))
print (mylist)

print ("---LIST AKSES---")
# saya mau mengakses item ke dua dari list di atas
print (mylist [1])

# pengindeksan negatif
# Pengindeksan negatif berarti mulai dari akhir
# -1 mengacu pada item terakhir, -2 mengacu pada item kedua terakhir, dan seterusnya.
# contoh
# akses item ke dua terakhir dari list di atas
print (mylist[-2])

# kita juga bisa memeriksa apakah suatu item sudah ada dalam list menggunakan kata kunci in
if "samsung" in mylist:
    print("ya, item samsung ada dalam mylist")

print ("---UBAH/GANTI ITEM LIST---")
# saya mau mengubah item ke dua dari list di atas menjadi iphone
mylist[1] = "iphone"
print (mylist)
# mengubah item ke tiga dan ke empat jadi realme dan nokia
mylist [2:4] = ["realme", "nokia"]
print (mylist)

print ("---MENAMBAH ITEM DALAM LIST---")
# Gunakan insert () untuk menambah item dalam list sesuai indeks
mylist.insert(2, "huawei")
print (mylist)
# Gunakan append () untuk menambah item ke akhir list
mylist.append("asus")
print (mylist)
# gunakan extend() untuk menambahkan item dari list lain ke list saat ini
laptop = ["acer", "dell", "hp", "axioo"]
mylist.extend(laptop)
print (mylist)

print ("---MENGHAPUS ITEM DALAM LIST---")
# Gunakan remove() untuk menghapus item tertentu
# saya mau menghapus item "infinix" pada list di atas
mylist.remove("infinix")
print (mylist)
# gunakan pop () untuk menghapus item berdasarkan indeks
# saya mau menghapus item ke tiga dari list di atas
mylist.pop(2)
print(mylist)
# gunakan clear () untuk menghapus seluruh item / mengosongkan list
mylist.clear()

print ("---PERULANGAN LIST---")
# perulangan for
laptop = ("acer", "dell", "hp", "axioo")
for h in laptop:
    print(h)

# perulangan melalui nomor indeks
laptop = ("acer", "dell", "hp", "axioo")
for h in range(len(laptop)):
    print(laptop[h])

# perulangan while
laptop = ("acer", "dell", "hp", "axioo")
i = 0
while i < len(laptop):
    print(laptop[i])
    i += 1

# perulangan list comprehension
# Sebuah perulangan singkat for yang akan mencetak semua item dalam sebuah daftar:
laptop = ("acer", "dell", "hp", "axioo")
[print(h) for h in laptop]

print ("---PEMAHAMAN LIST---")
# List comprehension menawarkan sintaks yang lebih singkat ketika kita ingin membuat daftar baru berdasarkan item" dari list yang sudah ada.
# Contoh:
# Berdasarkan list laptop yang ada di atas, kita menginginkan list baru dengan laptop yang namanya mengandung huruf "a".
# Tanpa list comprehension, kita harus menulis for pernyataan dengan uji kondisional di dalamnya:
laptop = ("acer", "dell", "hp", "axioo")
newlist = []
for h in laptop:
    if "a" in h:
        newlist.append(h)
print(newlist)
# atau kita bisa melakukannya dengan satu baris kode
laptop = ("acer", "dell", "hp", "axioo")
newlist = [h for h in laptop if "a" in h]
print(newlist)

print ("---MENGURUTKAN LIST---")
# kita bisa mengurutkan list dengan fungsi sort()
# Objek List memiliki sort() metode yang akan mengurutkan daftar secara alfanumerik
# mengurutkan secara alfanumerik atau alfabetis dari depan
laptop = ["acer", "dell", "hp", "axioo"]
laptop.sort()
print(laptop)
# untuk mengurutkan secara alfanumerik dari belakang
laptop.sort(reverse=True)
print(laptop)
# urutkan daftar secara numerik dari depan/menaik
numbers = [23, 28, 27, 26, 30]
numbers.sort()
print(numbers)

# urutkan daftar secara numerik dari belakang/menurun
numbers.sort(reverse=True)
print(numbers)

# sesuaikan fungsi pengurutan
# kita dapat menyesuaikan fungsi kita sendiri dengan menggunakan argumen kata kunci key = function
# Fungsi ini akan mengembalikan angka yang akan digunakan untuk mengurutkan daftar (angka terendah terlebih dahulu):
# contohnya, saya mau mengurutkan daftar berdasarkan seberapa dekat angka tersebut dengan 28
def myfunc(n):
    return abs(n - 28)
numbers = [23, 28, 27, 26, 30]
numbers.sort(key = myfunc)
print (numbers)

# pengurutan peka terhadap huruf besar/kecil
# secara sederhana, sort() akan mengurutkan daftar secara peka terhadap huruf besar/kecil
laptop = ["acer", "Dell", "hp", "Axioo"]
laptop.sort()
print(laptop)

# Untungnya kita dapat menggunakan fungsi bawaan sebagai fungsi utama saat mengurutkan daftar.
# Jadi, jika kitamenginginkan fungsi pengurutan yang tidak peka terhadap huruf besar/kecil, gunakan str.lower sebagai fungsi kunci:
laptop = ["acer", "Dell", "hp", "Axioo"]
laptop.sort(key=str.lower)
print (laptop)

# urutan terbalik
laptop = ["acer", "Dell", "hp", "Axioo"]
laptop.reverse()
print(laptop)

print ("---SALIN LIST---")
# gunakan metode copy ()
laptop = ["acer", "dell", "hp", "axioo"]
laptop2 = laptop.copy()
print(laptop2)
# Gunakan metode list()
laptop2 = list(laptop)
print(laptop2)
# Gunakan operator slice.
# kita juga dapat membuat salinan list dengan menggunakan :operator (slice).
laptop2 = laptop[:]
print(laptop2)

print ("---MENGGABUNGKAN LIST---")
# gunakan operator +
laptop = ["acer", "dell", "hp", "axioo"]
laptop2 = ["lenovo", "asus", "microsoft"]
laptop3 = laptop + laptop2
print (laptop3)

# Cara lain untuk menggabungkan dua list adalah dengan menambahkan semua item dari list2 ke list1, satu per satu:
laptop = ["acer", "dell", "hp", "axioo"]
laptop2 = ["lenovo", "asus", "microsoft"]
# gunakan fungsi for
for merk in laptop2:
    laptop.append(merk)
print("merk : ", laptop)