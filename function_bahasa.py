#=======================
# Function
#=======================

# Blok kode terorganisir
# dapat menerima input dan menghasilkan output
# serta dapat digunakan berulang kali

#============================
# regular function
# def nama_fungsi()
    # blok kode

# def tambah(angka1, angka2):
#     return angka1 + angka2
# print(tambah(2,5))
# print(tambah(100,200))

#============================
# Fungsi tanpa input(parameter) dan tanpa output (return)

# def greetings():
#     print('Selamat pagi!')

# # memanggil fungsi 
# greetings()

# # Soal buat fungsi menu yang akan menampilkan
# # menu utama
# # 1. cek kuota
# # 2. isi pulsa
# # 3. exit


# def menu():
#     print('''Menu Utama
# 1. Cek kuota
# 2. Isi Pulsa
# 3. Exit''')
    
# menu()

#=======================================
# fungsi dengan input (parameter) tetapi tanpa output

# def perkenalan(nama, domisili, usia):
#     print(f'Halo, nama saya adalah {nama}')
#     print(f'Saya berdomisli di kota {domisili}')
#     print(f'Saya berumur {usia} tahun')

# perkenalan('Imam', 'Binjai', 23) # harus berurutan

# # jika tidak ingin berurutan 
# perkenalan(usia=23, nama='ika', domisili='Bandung')

# soal: buat fungsi bernama oscar dengan parameter 
# nama aktor, film, dan tahunnya
# outputnya
#'Pemenang aktor terbaik pada tahun 2016 adalah Leonarnod di caprio pada film the revenant'

# def oscar(name, film, year):
#     '''
#     Fungsi ini menampilkan aktor peraih oscar sesuai dengan tahun dan nama filmnya

#     args:
#         nama (str): nama aktor
#         film (str): film yang diproduksi oleh sang aktor
#         tahun (int): tahun diproduksinya film

#     return:
#         none
#     '''
#     print(f'Pemenang aktor terbaik pada tahun {year} adalah {name} pada film the {film}')

# oscar('di caprio', 'the revenant', 2016)
# oscar('Cillian', 'Oppenheimer', 2023)
    
# ============================
# Fungsi dengan input (parameter) dan dengan output (return)
    
# def tambah(angka1, angka2):     # dengan input dan output
#     hasil = angka1 + angka2
#     return hasil                # pake return jika kita ingin menghasilkan suatu nilai
#                                 # agar bentuknya aritmatika bisa operasi matematika

# def tambah2(angka1, angka2):
#     hasil = angka1 + angka2
#     print(hasil)

# print(tambah(3,5))              # 8 adalah integer
# print(tambah2(3,5))             # 8 adalah print hasil

# print(tambah(3,5)-3)
# print(tambah2(3,5)-3)           #hasilnya error, none type tidak bisa operasi matematika


# soal: buat fungsi dengan parameter angka1 dan angka2, dimana fungsi tersebut
# mengembalikan 4 buah nilai
# 1. Hasil penjumlahannya, 2 hasil pengurangannya, 3 hasil perkaliannya, 4 hasil pembagiannya

# def operasi_math(angka1,angka2):
#     hasil_tambah = angka1 + angka2
#     hasil_kurang = angka1 - angka2
#     hasil_kali = angka1 * angka2
#     hasil_bagi = angka1 / angka2 
#     return hasil_tambah, hasil_kurang, hasil_kali, hasil_bagi
# #hasil_semua = hasil_tambah, hasil_kurang, hasil_kali, hasil_bagi
# #print(operasi_math(10,2))
# #print(hasil_semua)

# # bisa juga di unpacking
# hasil_tambah, hasil_kurang, hasil_kali, hasil_bagi = operasi_math(10,2)
# print('Hasil baginya adalah', hasil_bagi)

# =========
# Default parameter

# jika kita tidak memasukkan argument saat fungsi dipanggil
# maka fungsinya sudah memiliki nilai default untuk parameter tersebut

# def greetings(nama='Rahasia', usia=0, domisili='Indonesia'):
#     print(f'Halo, nama saya adalah {nama}, saya berusia {usia} dan domisili saya di {domisili}')


# greetings('Mazaya', 22, 'Bandung')
# greetings('Ridwan', 24)
# greetings('Banu')
# greetings(usia=25)

# def greetings(nama='Rahasia', usia=0, domisili='Indonesia'):
#     if nama == 'Rahasia':
#         print('Saya tidak ingin memberitahukan nama saya')
#     elif usia == 0:
#         print(f'Nama saya adalah {nama}. Saya tidak ingin menyampaikan usia saya')
#     elif domisili == 'Indonesia':
#         print(f'Nama saya adalah {nama}. Domisili saya tidak diketahui')
#     else:
#         print(f'Halo, nama saya adalah {nama}, saya berumur {usia} tahun dan berasal dari {domisili}')

# greetings('Iki', 23, 'Bandung')
# greetings(usia=20, domisili='Bandung')
# greetings('Aga')
# greetings('Arya', 19)

# ==========================================
# Global variable

# variable yang didefinisikan di luar fungsi
# Nilainya berlaku sepanjang proram masil dijalankan
# Dapat diakses dimanapun baik di dalam maupun di luar fungsi

# Kasus 2
# x = 100             # ini adalah variabel lokal

# def get_result():
#     print(x)        # ini adalah variabel global
#     a = 200         # ini adalah variabel lokal
#     return a+5

# get_result()
# print(get_result()) # Mencetak variable global dan variable lokal
# print(type(get_result()))
# print(a)

# Kasus 3
x = 100         # Ini adalah variabel global

def get_result():
    a = x + 20  # x-nya adalah variabel global, a-nya adalah variabel lokal
    return a

print('kasus 3',get_result())

# Kasus 4
x = 100         # Ini adalah variabel global

def get_result():
    a = x + 20          # x yang disini juga merupakan variabel lokal
    x = 10              # x ini adalah variabel local
    return a

# print(get_result())   # error --> karena x local dipanggil terlebih dahulu baru didefinikan

# Kasus 5
x = 100         # Ini adalah variabel global

def get_result():
    x = 10              # x ini adalah variabel local
    a = x + 20          # x yang disini juga merupakan variabel lokal
    return a

print(get_result())
x = 100         # Ini adalah variabel global

def get_result():
    x = 20          # ini adalah variabel local
    x = x + 20      # x ini adalah variabel local
    return x

print(get_result())     
print(x)                # ini adalah variabel global

# Cara 2
# x = 100         # Ini adalah variabel global

# def get_result():
#     global x        # ini adalah variabel global, mengambil nilai x dari global variabel
#     x = x + 20      # x ini adalah variabel global, sehingga nilai x di global akan ikut berubah
#     return x

# print(get_result())
# print(x)            # nilai x = 120 ditimpa dari x = x + 20 = 100 + 20

# =========

# CALLBACK FUNCTION 
# Suatu fungsi yang menerima argumen berupa fungsi lain

# def kalkulator(operator, angka1, angka2):
#     hasil = operator(angka1, angka2)
#     return hasil

# def tambah(angka1, angka2):
#     return angka1 + angka2

# def kurang(angka1, angka2):
#     return angka1 - angka2

# def kali(angka1, angka2):
#     return angka1 * angka2

# def bagi(angka1, angka2):
#     return angka1 / angka2

# print(kalkulator(tambah, 2, 5))
# print(kalkulator(kali, 4, 6))
#------------------------------------------

#------------------------------------------
# CALLING OTHER FUNCTION (CALL STACK)
# Fungsi yang digunakan dalam fungsi lainnya

# def area(panjang, lebar):
#     return panjang * lebar

# def volume(panjang, lebar, tinggi):
#     return area(panjang, lebar) * tinggi

# print(area(2,5))
# print(volume(2,5,4))

# def tampilkan(jawaban):
#     print(f'Jawabannya adalah {jawaban}')

# def print_volume(panjang, lebar, tinggi):
#     jawaban = area(panjang, lebar) * tinggi
#     tampilkan(jawaban)

# print_volume(2,4,5)
