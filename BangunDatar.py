# Membuat Program/Aplikasi Penentu Luas dan Keliling Bangun Datar
print("\n======PROGRAM PENGHITUNG LUAS DAN KELILING BANGUN DATAR======")
Nama = input("\nMasukkan Nama Anda: ")
print("Halo", Nama)
print("Dalam program ini, Anda akan menghitung luas dan keliling bangun datar.")

# Menampilkan daftar bangun datar
# Menggunakan list (for loops)
print("\nDAFTAR BANGUN DATAR")
BangunDatar = ["1. Persegi", "2. Persegi Panjang", "3. Segitiga", "4. Lingkaran"]
for item in BangunDatar:
    print (item)

# Menggunakan fungsi (def) untuk menulis rumus dari masing-masing bangun datar yang terdaftar
def Persegi():
    print("Anda memilih Persegi")
    sisi = float(input("Masukkan sisi persegi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas Persegi:", luas)
    print("Keliling Persegi:", keliling)
def Persegi_Panjang():
    print("Anda memilih Persegi Panjang")
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang:", luas)
    print("Keliling Persegi Panjang:", keliling)
def Segitiga():
    print("Anda memilih Segitiga")
    alas = float(input("Masukkan panjang alas segitiga: "))
    tinggi = float(input("Masukkan tinggi segitiga: "))
    sisi_miring = float(input("Masukkan sisi_miring segitiga: "))
    luas = 0.5 * alas * tinggi
    keliling = alas + tinggi + sisi_miring
    print("Luas Segitiga:", luas)
    print("Keliling Segitiga:", keliling)
def Lingkaran():
    print("Anda memilih Lingkaran")
    jari_jari = float(input("Masukkan jari-jari lingkaran: "))
    luas = 3.14 * jari_jari * jari_jari
    keliling = 2 * 3.14 * jari_jari
    print("Luas Lingkaran:", luas)
    print("Keliling Lingkaran:", keliling)

# Meminta pengguna memilih bangun datar terdaftar yang akan dihitung luas dan kelilingnya
# Menggunakan control flow percabangan (if-elif-else)
pilih = input("\nSilahkan Pilih Bangun Datar (1-4): ")
if pilih == "1":
   Persegi()
elif pilih == "2":
   Persegi_Panjang()
elif pilih == "3":
   Segitiga()
elif pilih == "4":
   Lingkaran()
else:
   print("\nInput tidak valid. Silahkan pilih bangun datar dari 1-4.")

# Bertanya ke pengguna mau hitung lagi atau tidak. Kalo ya, program akan jalan lagi
# Kalo tidak, ucapkan terimakasih
# Di sini berlaku perulangan while
while True:
   hitung_lagi = input("\nApakah Anda ingin menghitung lagi? (ya/tidak): ")
   if hitung_lagi == "ya":
       pilih = input("\nSilahkan Pilih Bangun Datar (1-4): ")
       if pilih == "1":
           Persegi()
       elif pilih == "2":
           Persegi_Panjang()
       elif pilih == "3":
           Segitiga()
       elif pilih == "4":
           Lingkaran()
       else:
           print("\nInput tidak valid. Silahkan pilih bangun datar dari 1-4.")
   elif hitung_lagi == "tidak":
       print("Okey, Terima kasih telah menggunakan program ini :)")
       break
   else:
       print("Input tidak valid. Silahkan jawab dengan 'ya' atau 'tidak'.")