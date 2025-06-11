# #=========================================
# # FUNCTION
# #=========================================

# # Blok kode terorganisir yang memiliki nama,
# # dapat menerima input dan dapat menghasilkan output,
# # serta dapat digunakan berulang kali

# #=========================================
# # REGULAR FUNCTION
# # def nama_fungsi():
# #   blok_kode

# def tambah(angka1, angka2):
#     return angka1 + angka2

# print(tambah(2,5))
# print(tambah(100,200))
# print(tambah(500,1000))

# #===========================================
# # Fungsi tanpa input (parameter) dan tanpa output (return)

# def greetings():
#     print('Selamat Pagi')
#     print('Hari ini kita akan belajar fungsi')

# # untuk memanggil fungsi
# greetings()             # cara yan benar untuk memanggil fungsi tanpa input dan tanpa output
# greetings()

# # jika kita print
# print(greetings())      # ketika dicetak, akan memunculkan hasil eksekusi statement dan juga mencetak None

# # Soal: Buat fungsi bernama menu yang akan menampilkan
# # Menu Utama
# # 1. Cek kuota
# # 2. Isi pulsa
# # 3. Exit

# def menu():
#     print('''Menu Utama
# 1. Cek kuota
# 2. Isi pulsa
# 3. Exit''')
    
# menu()

# #------------------------------------------------
# # Fungsi dengan input (parameter) tetapi tanpa output (return)

# def perkenalan(nama, domisili, usia):
#     print(f'Halo, nama saya adalah {nama}')
#     print(f'Saya berasal dari {domisili}')
#     print(f'Saya berumur {usia} tahun')

# perkenalan('Imam', 'Binjai', 23)
# perkenalan('Usamah', 'Bogor', 21)
# perkenalan('Boni', 24, 'Bandung')       # harus berurutan

# # jika ingin tidak berurutan, maka harus disebutkan parameternya terlebih dahulu
# perkenalan(usia=23, nama='Ika', domisili='Bandung')

# # Soal: Buat fungsi bernama Oscar dengan parameter 
# # nama aktor, film, dan tahunnya
# # Outputnya:
# # 'Pemenang aktor terbaik pada tahun 2016 adalah Leonardo Di Caprio pada film The Revenant'

# def Oscar(nama, film, tahun):
#     '''
#     Menampilkan aktor peraih oscar sesuai dengan tahun dan nama filmnya

#     Args:
#         nama (str): nama aktor 
#         film (str): film yang dimainkan oleh sang aktor
#         tahun (int): tahun diproduksinya film

#     Return:
#         None
#     '''
#     print(f'Pemenang aktor terbaik pada tahun {tahun} adalah {nama} pada film {film}')

# Oscar('Leonardo Di Caprio', 'The Revenant', 2016)

# #------------------------------------------------
# # Fungsi dengan input (parameter) dan dengan output (return)

# def tambah(angka1, angka2):         # dengan input dan output
#     hasil = angka1 + angka2
#     return hasil

# def tambah2(angka1, angka2):        # dengan input, tanpa output
#     hasil = angka1 + angka2         # by default return None  
#     print(hasil)  

# print(tambah(3,5))      # 8 adalah integer
# print(tambah2(3,5))     # 8 adalah hasil print

# print(tambah(3,5) - 3)
# print(tambah2(3,5) - 3) # error, NoneType tidak bisa dilakukan operasi aritmatika dengan integer

# # Sebaiknya menggunakan return untuk mengembalikan suatu nilai

# # Soal: Buat fungsi dengan parameter angka1 dan angka2, dimana fungsi tersebut
# # mengembalikan 4 buah nilai:
# # 1. Hasil penjumlahannya
# # 2. Hasil pengurangannya
# # 3. Hasil perkaliannya
# # 4. Hasil pembagiannya

# def aritmatika(angka1, angka2):
#     tambah = angka1 + angka2
#     kurang = angka1 - angka2
#     kali = angka1 * angka2
#     bagi = angka1 / angka2
#     return tambah, kurang, kali, bagi

# tambah, kurang, kali, bagi = aritmatika(10,2)
# print('Hasil baginya adalah', bagi)

# #--------------------------------------------
# # DEFAULT PARAMETER

# # Jika kita tidak memasukkan argument saat function dipanggil
# # maka fungsinya sudah memiliki nilai default untuk parameter tersebut

# def greetings(nama='Rahasia', usia=0, domisili='Indonesia'):
#     print(f'Halo, nama saya adalah {nama}, saya berumur {usia} tahun dan berasal dari {domisili}')

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

# #-------------------------------------------------------------
# # GLOBAL VARIABEL

# # Variabel yang didefinisikan di luar fungsi
# # Nilainya berlaku sepanjang program masih dijalankan
# # Dapat diakses dimanapun baik di dalam maupun di luar fungsi

# x = 100                 # ini adalah variabel global

# def get_result():
#     print(x+2)          # x-nya adalah variabel global
#     return x+5          # x-nya adalah variabel global

# get_result()
# print(get_result())
# print(x)

# #------------------------------------------------------
# # LOCAL VARIABLE

# # Variabel yang didefinisikan di dalam fungsi
# # Nilainya hanya berlaku di dalam fungsi tersebut
# # Ketika fungsinya selesai dijalankan, maka nilainya akan hangus atau dimusnahkan

# # Kasus 1
# x = 100         # ini adalah global variabel

# def get_result():
#     x = 25      # ini adalah local variabel
#     print(x)    # x-nya menggunakan local variabel

# get_result()    # 25
# print(x)        # 100 --> x-nya menggunakan global variabel

# # Kasus 2
# x = 100             # ini adalah variabel lokal

# def get_result():
#     print(x)        # ini adalah variabel global
#     a = 200         # ini adalah variabel lokal
#     return a+5

# get_result()
# print(get_result())
# print(type(get_result()))
# # print(a)          # error --> karena variabel a hanya didefinisan sebagai variabel lokal

# Kasus 3
# x = 100         # Ini adalah variabel global

# def get_result():
#     a = x + 20  # x-nya adalah variabel global, a-nya adalah variabel lokal
#     return a

# print(get_result())

# # Kasus 4
# x = 100         # Ini adalah variabel global

# def get_result():
#     a = x + 20          # x yang disini juga merupakan variabel lokal
#     x = 10              # x ini adalah variabel local
#     return a

# # print(get_result())   # error --> karena x local dipanggil terlebih dahulu baru didefinikan 

# # Kasus 5
# x = 100         # Ini adalah variabel global

# def get_result():
#     x = 10              # x ini adalah variabel local
#     a = x + 20          # x yang disini juga merupakan variabel lokal
#     return a

# print(get_result())

# # Kasus 6
# x = 100         # Ini adalah variabel global

# def get_result():
#     x = x + 20      # x ini adalah variabel local
#     return x

# # print(get_result())   # error --> karena nilai x pada 'x + 20' belum didefinisikan  

# # Agar kasus 6 tidak mengalami error dapat dilakukan 2 cara
# # Cara 1
# x = 100         # Ini adalah variabel global

# def get_result():
#     x = 20          # ini adalah variabel local
#     x = x + 20      # x ini adalah variabel local
#     return x

# print(get_result())     
# print(x)                # ini adalah variabel global

# Cara 2
#x = 100         # Ini adalah variabel global

# def get_result():
#     global x        # ini adalah variabel global, mengambil nilai x dari global variabel
#     x = x + 20      # x ini adalah variabel global, sehingga nilai x di global akan ikut berubah
#     return x

# print(get_result())
# print(x)            # nilai x = 120 ditimpa dari x = x + 20 = 100 + 20

#-----------------------------------------------
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


