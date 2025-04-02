#======================
# Lambda function
#======================

# fungsi kecil tidak memiliki nama
# bisa memiliki parameter, tapi hanya memilik 1 ekspersi/statement
# syntax --> lambda parameter: expression

#regular function
def kali(angka1, angka2):
    return angka1 * angka2
print(f'regular function: {kali(3,4)}')

# # Lambda function
kali_lambda = lambda angka1, angka2: angka1*angka2 # Parameternya angka1 dan angka2

print(f'Lambda Function: {kali_lambda(3,4)}')

# soal: buat fungsi bernama kuadrat dengan parameter angkka yang akan mengembalikan nilai 
# berupa hasi kuadratnya
kuadrat_lambda = lambda angka1: angka1**2
print(f'Lambda function kuadrat: {kuadrat_lambda(3)}')

# soal 2: buat fungsi dengan lambda function menampilkan huruf pertama dari sebuah kata
# dimana parameternya adalah kata

# contoh salah
kata_pertama = lambda kata : kata[0]
print(f'Lambda kata: {kata_pertama("cakep")}')

get_initial = lambda kata: kata[0]
print(get_initial("Asyraf"))

# soal buat fungsi dengan lambda function dimana parameternya adalah angka
# kemudaian akan menampilkan apakah genap atau ganjil

# ganjil_genap = lambda angka: print('genap') if angka % 2 == 0 else print('ganjil')
# print(f'hasil perhitungan dari lambda: {ganjil_genap(24)}')

# # bisa juga ditulis dengan:
# bilangan_lambda = lambda angka: 'Genap' if angka % 2 ==0 else 'Ganjil'
# print(bilangan_lambda(5))



# soal

# list_angka = [1, 2, 3, 4, 5]
# # hasilkan [1,4,9,16,25]

# cara Haris dengan list comperhension
# list_angka = [1, 2, 3, 4, 5]
# list_angka_kuadrat = [i**2 for i in list_angka]
# print(list_angka_kuadrat)



# pake cara looping statement
# list_kuadrat = []
# for angka in list_angka:
#     hasil = angka**2
#     list_kuadrat.append(hasil)

# print(list_kuadrat)

# # cara list comperhension
# list_kuadrat = [angka**2 for angka in list_angka]
# print(list_kuadrat)

#==========================
# map
# biasa dipakai untuk mengubah nilai/bentuk dari data-data yang ada di collection data types
# syntax --> map(function, list)

# def kuadrat(angka):
#     return angka**2

# list_angka = [1, 2, 3, 4, 5]
# print(f'Hasil dengan map - regular function:', list(map(kuadrat, list_angka)))
# print(f'Hasilkan dengan map - lambda function', list(map(lambda x: x**2, list_angka)))


# =========================
# map dari kopian, lebih lengkap
#===========================================
# MAP
# Biasa dipakai untuk mengubah nilai/bentuk dari data-data yang ada di collection data types
# syntax --> map(function, list)

# def kuadrat(angka):
#     return angka**2

list_angka = [1, 2, 3, 4, 5]
# print('Hasil dengan Map - Regular Function:', list(map(kuadrat, list_angka)))
# print('Hasil dengan Map - Lambda Function:', list(map(lambda x: x**2, list_angka)))
print(f'hasil dengan map {list(map(lambda x: x**3, list_angka))}')
# #-------------------------
# # Soal:
# list_angka = [1, 2, 3, 4, 5]
# # Hasilkan [1, 3, 5] dari list angka tersebut

# print(list_angka[::2])

# # Cara mas asyraf
# list_ganjil = list(map(lambda x:x, list_angka[::2]))
# print(list_ganjil)

# # Looping statement
# list_ganjil=[]
# for angka in list_angka:
#     if angka%2 != 0:
#         list_ganjil.append(angka)

# print('Hasil loop:', list_ganjil)

# # List Comprehension
# list_ganjil = [angka for angka in list_angka if angka%2 != 0]
# print('Hasil list comprehension:', list_ganjil)


# # soal
# list_angka = [1, 2, 3, 4, 5]
# # hasilkan [1,3,4] dari list angka tersebut

## Filter
#============================================
# FILTER
# Biasa kita pakai untuk menyaring nilai/data 
# dari data-data dalam collection data types
# jumlah item berkurang, tetapi nilai/bentuk datanya tidak berubah
# syntax -> filter(function, list)
# soal

list_angka = [1, 2, 3, 4, 5]
# hasilkan [1,3,5] dari list angka tersebut
print('Hasil Filter:', list(filter(lambda x: x%2 != 0, list_angka)))

# =======================
# recursive function
# sebuah fungsi utk memanggil dirinya sendiri dalam fungsi tersebut

# def countdown(angka):
#     print(angka)
#     angka = angka - 1

#     if angka > 0:
#         countdown(angka)
# countdown(5)
