#pengulangan for


hp = ["samsung", "redmi", "oppo", "vivo", "infinix", "poco", "advan","lenovo"] #array (kalau dalam mtk matrix)
for android in hp:
    print(android)

  #pengulangan for

ibuKota =["Mataram", "Selong", "Praya", "Gerung", "Tanjung", "Taliwang", "Sumbawa Besar", "Dompu", "Woja"] #array

kata = "Selong"
print(kata[2])
print(ibuKota[0])
print(ibuKota[1])
print(ibuKota[2])
print(ibuKota[3])
print(ibuKota[4])

for huruf in kata:
    print(huruf)

print("---pengulangan For---")
for kota in ibuKota:
    print("Ibu Kota ", kota)

print("---Akhir pengulangan For---")

print("---Pengurutan Sort pada Array")

ibuKota.sort(reverse = True)
print(ibuKota)
print("---------------")
print("----Mengganti nilai array---")
ibuKota[0] = "Toya"
print(ibuKota)

print("---Tambbah Nilai Array---") #append
ibuKota.append("Sikur")
print(ibuKota)

print("---Menambah nilai dengan indeks---") #insert
ibuKota.insert(2, "Suela")
print(ibuKota)