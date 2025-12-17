#contiune statement digunakan untuk mengendalikan perulangan
#jika contiune dieksekusi, maka kondisi saat ini dihentikan dan akan dilanjutkan ke kondisi selanjutnnya
#seperti contoh dibawah ini aku tentuin kondisinya dengan a habis dibagi 2
#sehingga yang di eksekusi kemungkinan hanya angka yang ga habis dibagi 2 (angka ganjil)
a = 0
while a < 20:
  a += 1
  if a % 2 == 0:
    continue
  print(a)