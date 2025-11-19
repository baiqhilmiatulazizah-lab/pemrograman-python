# PROGRAM PENENTUAN NILAI DAN TEMPAT BILANGAN
# menggunakan fungsi try_except untuk menangani kesalahan (error), jika user input non-angka

# meminta input bilangan dari user
try:
    angka = int(input("\nMasukkan Bilangan (maksimal 4 digit) : "))

    # penentuan nilai tempat
    # membatasi jumlah angka yang dimasukkan
    # jumlah angka ga boleh lebih dari dari 4 digit
    if 0 <= angka <= 9999:

        # ambil nilai ribuan
        ribuan = angka // 1000
        # hitung sisa setelah diambil ribuannya
        sisaribuan = angka % 1000

        # ambil nilai ratusan dari sisaribuan
        ratusan = sisaribuan // 100
        # hitung sisa setelah diambil ratusannya
        sisaratusan = sisaribuan % 100

        # ambil nilai puluhan dari sisaratusan
        puluhan = sisaratusan // 10
        # sisa terakhir adalah satuan
        satuan = sisaratusan % 10

        # menampilkan hasil sesuai dengan nilai tempat
        print(f"\nAnda memasukkan bilangan {angka} dimana:")
        print(f"{ribuan} merupakan ribuan")
        print(f"{ratusan} merupakan ratusan")
        print(f"{puluhan} merupakan puluhan")
        print(f"{satuan} merupakan satuan")

    else:
        print("Harap masukkan bilangan antara 0 dan 9999 saja.")

except ValueError:
    print("Input tidak valid! Harap masukkan angka saja.")
