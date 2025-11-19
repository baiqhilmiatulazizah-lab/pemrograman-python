#belajar casting tipe data pada python
#casting > proses mengubah satu tipe data ke tipe data yang lain
#tipe data : int, float, str, bool

## INTEGER
print ("\n ====INTEGER====")

dataint = 27
print("data:", dataint, ",type =", type(dataint))

datafloat = float(dataint)
datastr = str(dataint)
databool = bool(dataint) #akan false jika nilai = 0
print("data:", datafloat, ",type =", type(datafloat))
print("data:", datastr, ",type =", type(datastr))
print("data:", databool, ",type =", type(databool))

## FLOAT
print ("\n ====FLOAT====")
datafloat = 2.8
print("data:", datafloat, ",type =", type(datafloat))

dataint = int(datafloat)
datastr = str(datafloat)
databool = bool(datafloat) #akan false jika nilai = 0
print("data:", dataint, ",type =", type(dataint))
print("data:", datastr, ",type =", type(datastr))
print("data:", databool, ",type =", type(databool))

## STRING
print ("\n ====STRING====")
datastr = "28"
print("data:", datastr, ",type =", type(datastr))

dataint = int(datastr) # string harus angka | akan error kalo string berupa huruf atau karakter
datafloat = float(datastr) # string harus angka | akan error kalo string berupa huruf atau karakter
databool = bool(datastr) # akan false jika string kosong
print("data:", dataint, ",type =", type(dataint))
print("data:", datafloat, ",type =", type(datafloat))
print("data:", databool, ",type =", type(databool))

## BOOLEAN
print ("\n ====BOOLEAN====")
databool = True
print("data:", databool, ",type =", type(databool))

dataint = int(databool)
datafloat = float(databool)
datastr = str(databool) 
print("data:", dataint, ",type =", type(dataint))
print("data:", datafloat, ",type =", type(datafloat))
print("data:", datastr, ",type =", type(datastr))




