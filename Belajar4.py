# Casting adalah perubahan dari satu type ke tipe lain

print("======Integer======")
data_int = 0
print("data = ", data_int, "type = ",type(data_int))

data_float = float (data_int)
data_string = str (data_int)
data_bool = bool(data_int)
data_complex = complex(data_int)
print("data = ", data_float, "type = ",type(data_float))
print("data = ", data_string, "type = ",type(data_string))
print("data = ", data_bool, "type = ",type(data_bool))
print("data = ", data_complex, "type = ",type(data_complex))

print("======Float======")
data_float = 9.5
print("data = ", data_float, "type = ",type(data_float))

data_int = int (data_float)
data_string = str (data_float)
data_bool = bool(data_float)
data_complex = complex(data_float)
print("data = ", data_int, "type = ",type(data_int))
print("data = ", data_string, "type = ",type(data_string))
print("data = ", data_bool, "type = ",type(data_bool))
print("data = ", data_complex, "type = ",type(data_complex))

print("======String======")
data_string = 0
print("data = ", data_string, "type = ",type(data_string))

data_int = int (data_string)
data_float = str (data_string)
data_bool = bool(data_string)
data_complex = complex(data_string)
print("data = ", data_int, "type = ",type(data_int))
print("data = ", data_float, "type = ",type(data_float))
print("data = ", data_bool, "type = ",type(data_bool))
print("data = ", data_complex, "type = ",type(data_complex))

print("======BOOL======")
data_bool = True
print("data = ", data_bool, "type = ",type(data_bool))

data_int = int (data_bool)
data_float = float (data_bool)
data_string = str(data_bool)
data_complex = complex(data_bool)
print("data = ", data_int, "type = ",type(data_int))
print("data = ", data_float, "type = ",type(data_float))
print("data = ", data_string, "type = ",type(data_string))
print("data = ", data_complex, "type = ",type(data_complex))


# input user 

data = input("Masukkan data :")
print("data = ",data,"type = ", type(data))
#data masukan pasti string


#jika mengambil integer maka,

angka = int(input("masukkan angka :"))
angka = float(input("masukkan angka :"))
print("data =", angka,"type =", type(angka))


#untuk ke bo0lean

biner = bool(int(input("masukkan nilai boolean :")))

print("data = ", biner,"type = ", type(biner))

#operasi Aritmatika

a = 10
b = 3

#operasi tambah 
hasil = a + b
print(a,'+',b,'=',hasil)

#operasi kurang 
hasil = a - b
print(a,'-',b,'=',hasil)

#operasi kali
hasil = a * b
print(a,'*',b,'=',hasil)

#operasi bagi 
hasil = a / b
print(a,'/',b,'=',hasil)

#operasi eksponensial
hasil = a ** b
print(a,'**',b,'=',hasil)

#operasi modulus (sisa pembagian)
hasil = a % b
print(a,'%',b,'=',hasil)

#operasi floor division( kebalikan modulus, nilai dibulatkan kebawah) 
hasil = a // b
print(a,'//',b,'=',hasil)

#prioritas operasi

x = int(input('x= ')) 
y = int(input('y= ')) 
z = int(input('z= ')) 

hasil = x ** y * z + x / y - y % z // x
print(x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=',hasil)


#Latihan Perhitungan
# konversi temperatur

print("\nPROGRAM KONVERSI TEMPERATUR\n")

celcius = float(input('masukan suhu dalam celcius '))
print('suhu =' ,celcius, 'Celcius')

#reamur 
reamur = (4/5) *celcius
print('reamur = ',reamur,'Reamur')

#Fahrenhit
fahrenhit = ((9/5) * celcius) + 32
print('fahrenhit = ', fahrenhit,'fahrenhhit ')

#Kelvin 
kelvin = celcius + 273
print('kelvin = ', kelvin,'K')


#Tugas 
# 1. Konversi kan Fahrenhit ke Kelvin 
print('1.Konversi Fahrenhit ke Kelvin')

Fahrenhit = float(input('Masukan nilai suhu '))
print('suhu = ', Fahrenhit,'F')

Kelvin = ((5/9) * (Fahrenhit-32)) + 273
print('Kelvin = ', Kelvin,'K')

#2. Konversikan Kelvin ke Fahrenhit
print('2. Konversi Kelvin ke Fahrenhit')

Kelvin = float(input('masukkan nilai suhu '))
print('suhu = ', Kelvin,'K')

Fahrenhit = ((9/5)*(Kelvin - 273)) + 32 
print('Fahrenhit = ', Fahrenhit,'F')
