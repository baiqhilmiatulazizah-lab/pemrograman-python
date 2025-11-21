#PROGRAM PENENTUAN NILAI DAN TEMPAT BILANGAN
# menggnakan fungsi try_except untuk menangani kesalahan (error), jika user input non-angka
print("\nAPLIKASI PENENTUAN NILAI   DAN TEMPAT BILANGAN")
# meminta input bilangan dari user
try:
    angka = int(input("\nMasukkan Bilangan:"))

    # penentuan nilai tempat dari ratusan juta sampai satuan  
    if 0 <= angka <= 999999999:

        #ambil nilai ratusan juta
        ratusanjuta = angka // 100000000
        #hitung sisa setelah ratusan juta diambil
        sisaratusanjuta = angka % 100000000

        #ambil nilai puluhan juta dari sisa ratusan juta
        puluhanjuta = sisaratusanjuta // 10000000
        #hitung sisa setelah puluhan juta diambil
        sisapuluhanjuta = sisaratusanjuta % 10000000

        #ambil nilai jutaan dari sisa puluhan juta 
        jutaan = sisapuluhanjuta // 1000000
        #hitung sisa setelah jutaan diambil
        sisajutaan = sisapuluhanjuta % 1000000

        #ambil nilai ratusan ribu dari sisa jutaan
        ratusanribu = sisajutaan // 100000
        #hitung sisa setelah ratusanribu diambil
        sisaratusanribu = sisajutaan % 100000

        #ambil nilai puluhan ribu dari sisa ratusan ribu
        puluhanribu =  sisaratusanribu // 10000
        #hitung sisa setelah puluhanribu diambil
        sisapuluhanribu = sisaratusanribu % 10000

        # ambil nilai ribuan dari puluhan ribu
        ribuan =  sisapuluhanribu // 1000
        # hitung sisa setelah diambil ribuannya
        sisaribuan = sisapuluhanribu % 1000

        # ambil nilai ratusan dari sisa ribuan
        ratusan = sisaribuan // 100
        # hitung sisa setelah diambil ratusannya
        sisaratusan = sisaribuan % 100

        #ambil nilai puluhan dari sisa ratusn
        puluhan = sisaratusan // 10
        #sisa terakhir adalah satuan
        satuan = sisaratusan % 10

        # menampilkan hasil sesuai dengan nilai tempat
        print(f"\nAnda memasukkan bilangan {angka} dimana:")
        print(f"{ratusanjuta} merupakan ratusan juta")
        print(f"{puluhanjuta} merupakan puluhan juta")
        print(f"{jutaan} merupakan jutaan")
        print(f"{ratusanribu} merupakan ratusan ribu")
        print(f"{puluhanribu} merupakan puluhan ribu")
        print(f"{ribuan} merupakan ribuan")
        print(f"{ratusan} merupakan ratusan")
        print(f"{puluhan} merupakan puluhan")
        print(f"{satuan} merupakan satuan")

    else:
        print("harap masukkan bilangan antara 0-999999999.")

except ValueError:
    print("input tidak valid! harap masukkan angka.")