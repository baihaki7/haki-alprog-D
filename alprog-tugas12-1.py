# Program pengecekan rentang angka dengan logika boolean
print ("RENTANG ANGKA BAIHAKI")
print("======Try Thiss=======")
# Rentang angka
nim_awal = 24  # NIM awal
nim_akhir = 28  # NIM akhir

# input dari pengguna
print(f"Masukkan angka antara {nim_awal} dan {nim_akhir}:")
angka = int(input("Angka: "))

# Mengecek apakah angka dalam rentang NIM
hasil = nim_awal <= angka <= nim_akhir

# Output hasil
print("\nHasil Operasi Logika Boolean:")
print(f"Jika nilai akhir di OR-kan dengan True maka: {nim_akhir or True}")
print(f"Jika nilai akhir di OR-kan dengan False maka: {nim_akhir or False}")
print(f"Jika hasil di AND-kan dengan True maka: {hasil and True}")
print(f"Jika hasil di AND-kan dengan False maka: {hasil and False}")
print(f"Jika hasil di XOR-kan dengan True maka: {hasil ^ True}")
print(f"Jika hasil di XOR-kan dengan False maka: {hasil ^ False}")