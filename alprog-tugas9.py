# suhu celcius ( 2 digit nim terakhir )
# suhu dalam fahranheit
# suhu dalam kelvin
# suhu dalam reamur

nilai = float(input("masukan nilai dalam celcius :"))

hasil = nilai * 9/5 + 32
print (" nilai dalam fahrenheit :", hasil)

nilai = float(input("masukan nilai dalam fahrenheit :"))

hasil = nilai * 5/9 + 273.15
print (" nilai dalam kelvin :", hasil)

nilai = float(input("masukan nilai dalam kelvin :"))

hasil = nilai % (28 - 273.15) * 4/5
print (" nilai dalam reamur :", hasil)