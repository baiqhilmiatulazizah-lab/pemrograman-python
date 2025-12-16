#elif statement

#jika nilai > 85 maka mendapat nilai A
#jika nilai >= 75 maka mendapat nilai B
#jika nilai >= 65 maka mendapat nilai C
#jika nilai >= 55 maka mendapat nilai D
#jika nilai < 55 maka mendapat nilai E

nilai = input("\nMasukkan nilai anda: ") #string input

if(type(nilai) == str and not nilai.isdigit()): #fungsi untuk mengecek inputan bukan angka
    print("Error!!! Anda memasukkan huruf atau simbol")
elif(int(nilai) > 85 and int(nilai) <= 100): #rentang nilai 86 - 100
    print("Anda mendapat nilai A")
elif(int(nilai) >= 75 and int(nilai) <= 85): #rentang nilai 75 - 85
    print("Anda mendapat nilai B")
elif(int(nilai) >= 65 and int(nilai) < 75): #rentang nilai 65 - 74
    print("Anda mendapat nilai C")
elif(int(nilai) >= 55 and int(nilai) < 65): #rentang nilai 55 - 64
    print("Anda mendapat nilai D")
elif(int(nilai) < 55 and int(nilai) >= 0): #rentang nilai 0 - 54
    print("Anda mendapat nilai E")
else:
    print("Error!!! Masukkan nilai 0 - 100")