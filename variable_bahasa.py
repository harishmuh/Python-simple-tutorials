# # Variable

# # ==================
# # Variable
# # ==================
# # variable adalah sebuah fitur dalam bahasa pemrograman
# # Fungsi: untuk menyimpan suatu nilai/data

# # Variable bisa dianalogikan sebagai box
# # - Box tersebut mempunyai nama
# # - Box tersebut bisa menyimpan nilai
# # - Pada umumnya box berisi hanya 1 nilai/data

# # nama = 'Harish'
# # print('nama saya adalah', nama)

# # nama = 'Bobby'
# # print('nama saya adalah', nama)

# # Trivia
# # Untuk comment: ctrl + /
# # untuk memilih next occurence: ctrl d

# # usia = 29 # variable bisa menyimpan angka
# # print('usia adalah', usia)

# # =====================
# # Cara penamaan variable
# # ======================

# # Cara yg benar
# # namasiswapurwadhika = 'Annisa'
# # print(namasiswapurwadhika)

# # Camel case
# # namaSiswaPurwadhika = 'Banu'
# # print(namaSiswaPurwadhika)

# # Snake case
# # namasiswapwdk = 'Reza'
# # print(namasiswapwdk)

# # Contoh yang diawali dengan underscore
# _namasiswapwdk = 'Tono'
# print(_namasiswapwdk)

# # =============================
# # Cara penamaan yang salah
# # =============================

# # Tidak boleh diawali angka
# 2namasiswabandung = 'rexi'
# print(2namasiswabandung)

# Tidak boleh memuat tanda baca
# mahasiswapwdk? = 'rexa'
# print(mahasiswapwdk?)

# Tidak boleh memuat spasi
# mahasiswa pwdk = 'Joko'
# print(mahasiswa pwdk)


# =========
# Data types
# =========

# string
# Menggunakan tanda petik/kutip, bisa petik 1 atau petik 2
# data_str = 'bagas'
# print('nilainya adalah', data_str)
# print('Tipe datanya adalah', type(data_str))

# Integer 
# Bilangan bulat
# data_int = 10
# print('nilainya adalah', data_int)
# print('Tipe datanya adalah', type(data_int))
# # Float
# data_float = 10.000 # Hanya bernilai 10.0 tapi tipenya float
# data_float2 = .45
# print('Nilainya adalah', data_float)
# print('tipe datanya adalah', type(data_float))
# print('Nilainya adalah', data_float2)
# print('tipe datanya adalah', type(data_float2))

# # Boolean
# data_boolean = True
# print('Nilainya adalah', data_boolean)
# print('tipe datanya adalah', type(data_boolean))

# data_boolean = False
# print('Nilainya adalah', data_boolean)
# print('tipe datanya adalah', type(data_boolean))

# data_boolean = 'False' # tipe string
# print('Nilainya adalah', data_boolean)
# print('tipe datanya adalah', type(data_boolean))

# None
# data_none = None
# print('nilainya adalah', data_none)
# print('type datanya adalah', type(data_none))

# Variable yg menyimpan lebih dari satu nilai
# data = 10, 20
# print('nilainya adalah', data)
# print('tipe datanya adalah', data)

# Unpacking
# data_1, data_2 = 10, 20
# print('data 1',data_1)
# print('data 2',data_2)

# ====================
# Collection data type
# ====================

# ===== List
# ditandai dengan kurung siku []
# bersifat mutabel atau bisa diubah
# data_list = [10,20]
# print('nilainya adalah', data_list)
# print('tipe datanya adalah', type(data_list))

# data_list = [10, 12.5, True, 'Halo']
# print('Nilainya adalah', data_list)
# print('tipe datanya adalah', type(data_list))

# data_list[0] = 'Joko'
# print('Nilainya adalah', data_list)


# ===== Tuple
# Tuple ditandai dengan kurung biasa ()
# Tuple bisa menampung banyak tipe data
# data_tuple = (10, 15.6, True, 'Hi')
# # print('nilainya adalah', data_tuple)
# # print('tipe data', type(data_tuple))
# data_tuple[3] = 'Why' # Tupple tidak bisa diubah

# ==== Set
# Set ditandai dengan kurung kurawal {}
# Set adalah himpunan # Tidak bisa ada duplikat
# Set tidak bisa indexing
# Set bisa ditambah nilainya, tapi tidak bisa berurutan
# data_set = {10, 23.5, False, 'Banteng'}
# print('nilainya adalah', data_set)
# print('tipe datanya adalah', type(data_set))

# ==== Dictionary
# Punya key dan value
# data_dict = {'nama': 'Banu', 'kelas': 'Data sains', 'umur': 25}
# print('nilainya adalah', data_dict)
# print('tipe datanya adalah', type(data_dict))

# =======================
# Mathematical operations (arithmethic operator)
# =======================
angka_1 = 10
angka_2 = 3
angka_3 = 5.5

# Penjumlahan
# hasil = angka_1 + angka_2
# print('Hasil penjumlahan', angka_1, '+', angka_2, '=', hasil)

# Pengurangan
# hasil = angka_1 - angka_2
# print('Hasil pengurangan', angka_1, '-', angka_2, '=', hasil)

# Perkalian
# hasil = angka_1 * angka_3
# print('Hasil perkalian', angka_1, '*', angka_3, '=', hasil)
# print('tipe datanya adalah', type(hasil))

# Pembagian
# hasil = angka_1 / angka_2
# print('Hasil pembagian', angka_1, '/', angka_2, '=', hasil)
# print('tipe datanya adalah', type(hasil))

# Floor division (//)
# hasil = angka_1 // angka_2
# print('Hasil floor division', angka_1, '//', angka_2, '=', hasil)
# print('tipe datanya adalah', type(hasil)) # Hasil tipe integer

# Modulus (%)
# hasil = angka_1 % angka_2
# print('Hasil modulus', angka_1, '%', angka_2, '=', hasil)
# print('tipe datanya adalah', type(hasil)) # Sisa hasil pembagian

# pangkat (**)
# hasil = angka_1 ** angka_2
# print('Hasil pangkat', angka_1, '**', angka_2, '=', hasil)
# print('tipe datanya adalah', type(hasil))

# nilai = 5000000
# print('nilainya adalah', nilai)
# print('Tipe datanya adalah', type(nilai))

# nilai = 5e6 # Setara dengan 5 x 10**6
# print('nilainya adalah', nilai)
# print('tipe datanya adalah', type(nilai)) 

# ==== Assignment operator
# x = 3
# x = x + 3
# print('nilai x adalah', x)

# x += 3 # setara dengan x = x + 3
# print('nilai x adalah', x)

# x -= 2 # setara dengan x = x - 2
# print('nilai x adalah', x)

# x %= 2 # setara dengan x = x % 2
# print('nilai x adalah', x) # 1

# ======================
# Python function for arithmethics
# math : adalah library untuk melakukan fungsi matematika
import math

angka = 12.35

# # floor (pembulatan ke bawah)
# hasil = math.floor(angka)
# print(hasil)

# pow (pangkat)
# hasil = math.pow(angka, 4)
# print('Hasil pangkat 4 nya adalah', hasil)

# # sqrt (akar kuadrat)
# hasil = math.sqrt(angka)
# print('Hasil akar kuadratnya nya adalah', hasil)

# fabs (nilai absolut)
# hasil = math.fabs(-15.7)
# print('Hasil absolut dari -15,7 adalah', hasil)

# pi (nilai pi)
# hasil = math.pi
# print('bilangan pi adalah', hasil)

# Luas lingkaran
# radius = 7
# luas_lingkaran = math.pi * radius **2
# print('luas lingkaran adalah', luas_lingkaran)

#============== urutan operasi aritmatika (PEMDAS)
# Parentheses (di dalam tanda kurung)
# Multipication/Division 
# addition/substraction

# nilai = (2+3) * 5 **2 # setara 125
# print(nilai) 

# =============================
# Casting
# ==============================

# A. Mengubah dari string menjadi integer
# Contoh 1
# nilai_awal = '123'
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = int(nilai_awal)
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# contoh 2
# nilai_awal = '123abc' ## akan error karena ada 'abc'
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = int(nilai_awal)
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# contoh 3
# nilai_awal = '123.45' # error karena mengandung titik
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = int(nilai_awal)
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# B. Mengubah dari string menjadi float
# contoh B1
# nilai_awal = '123' # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = float(nilai_awal)
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))


# contoh B2
# nilai_awal = '123.45' # error karena mengandung titik
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# C. Mengubah dari integer jadi float
# contoh C1
# nilai_awal = 123 # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = float(nilai_awal)
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # D. Mengubaj dari float menjadi integer
# nilai_awal = 123.54 # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = int(nilai_awal) # setara 123 # ngambil floor division/pembulatan ke bawah
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # E. Mengubah dari integer jadi string
# # contoh E1
# nilai_awal = 123 # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = str(nilai_awal)
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # F. Mengubah dari float jadi string
# nilai_awal = 123.54 # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = str(nilai_awal) # setara 123 # ngambil floor division/pembulatan ke bawah
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # G. Mengubah boolean jadi int
# # Contoh 1
# nilai_awal = True # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = int(nilai_awal) # setara 1
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # Contoh 2
# nilai_awal = False # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = int(nilai_awal) # setara 0
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # H. Mengubah dari integer jadi boolean
# # contoh 1
# nilai_awal = 0 # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = bool(nilai_awal) # jadi False, selain 0 jadi True
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # contoh 2
# nilai_awal = 1 # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = bool(nilai_awal) # jadi True, selain 0 jadi True
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # I. Mengubah dari string jadi boolean
# # contoh 1
# nilai_awal = 'asyraf' # bisa
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = bool(nilai_awal) # jadi True, selain 0 jadi True
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# # contoh 2
# nilai_awal = ''       # jika tidak terdapat karakter (blank) dalam string maka bernilai False        
# print('Nilai awal:', nilai_awal, 'dengan tipe data', type(nilai_awal))

# nilai_akhir = bool(nilai_awal)
# print('Nilai akhir:', nilai_akhir, 'dengan tipe data', type(nilai_akhir))

# ======================== User input

# meminta inputan dari user dan langsung dicetak tanpa di assign ke variable
#print((input('Masukkan nama: ')))

# Meminta inputan dari user dan dimasukkan ke dalam variable
# umur = input('Masukkan usia: ')
# print('umur Anda adalah: ', umur, 'tahun')


# ============== Latihan input 
# buat suatu program yang meminta inputan dari user, 
# kemudian akan ditampilkan pada layar usia user 10 tahun yang akan datang
# input --> masukkan usia: 15
# output --> umur anda 10 tahun yang akan datang adalah 25 tahun

# jawaban
# umur = input('Masukkan usia: ') # hasil inputan bentuknya adalah string
# umur_10 = float(umur) + 10
# print('umur Anda 10 tahun yang akan datang adalah: ', umur_10, 'tahun')

# ===============================================


# ========================== 
# String
# ===========================

# penggunaan tanda kutip atau tanda petik dalam string

# kutipSatu = 'Halo, saya "Batman"'
# print(kutipSatu) 

# kutipDua = "Hi, I'am Superman"
# print(kutipDua)

# kutipTiga = '''Cicak di "dinding"
# diam-diam merayap
# datang seekor 'nyamuk'
# '''
# print(kutipTiga)

# # Penggunaan escape character

# # untuk menyisipkan karakter yang illegal atau membuat baris baru/tab/backspace
# # single quote (\')
# print('I\'m Batman')

# # New line (\n)
# print('Saya sedang belajar Data Science. \nSaya sedang mengambil kelas di Purwadhika')

# # Tab (\t)
# print('|nama\t\t| Usia\t\t| Domisili\t\t')

# # Backspace (/b)
# print('Burger\b dan hotdog')

# # Backslash (\\)
# print('Saya ingin makan hotdog\\burger')

# ========
# string function and method

kalimat = 'Saya senang belajar Data Science dan berenang'

# len (jumlah karakter)
# panjangString = len(kalimat)
# print('Banyaknya karakter', panjangString)

# Index (mencari index dari suatu substring di dalam string)
# substring = 'nang'
# indexString = kalimat.index(substring)
# print('Kata', substring, 'muncul pada index ke', indexString)

substring = 'nang'
indexString = kalimat.index(substring, 10) # Mencari  indeks setela index ke 10
print('Kata', substring, 'muncul pada index ke', indexString)

# substring = 'nang'
# indexString = kalimat.index(substring, 10)      # mencari index dari kata nang setelah index ke 10
# print('Kata', substring, 'muncul pada indeks ke:', indexString)

# split # memisahkan

# kalimat = 'Saya senang belajar Data Science dan berenang'

# split_spasi = kalimat.split(' ') # ada spasi
# print('Hasil split berdasarkan spasi', split_spasi)

# split_a = kalimat.split('a')
# print('Hasil split berdasarkan huruf a', split_a)

# splitting = kalimat.split()
# print('Hasil split by default', splitting)

# split_data = kalimat.split('data')              # karena tidak ada kata 'data', maka ditampilkan utuh
# print('Hasil split by default', split_data)

# Fungsi Lower dan upper
#jadi_huruf_kecil =kalimat.lower() # huruf kecil semua
# print('fungsi lower:', jadi_huruf_kecil)
# #jadi_huruf_besar =kalimat.upper() # huruf besar semua
# print('Fungsi upper:', jadi_huruf_besar )

# Fungsi capitalize (mengubah string menjadi huruf besar hanya pada awal kalimat)
# print(kalimat.capitalize())

# # Fungsi title (mengubah string menjadi huruf besar pada setiap awal kata)
# print(kalimat.title())

# =====================================
# String Slicing dan Indexing
kalimat = 'Data Science'

# Indexing
# print(kalimat[0]) # karakter huruf ke 0 (pertama) --> D
# print(kalimat[5]) # karakter huruf ke 5 (pertama) --> S
# print(kalimat[11]) # karakter huruf ke 11 (pertama) --> e
# print(kalimat[-1]) # karakter huruf ke (-1) (pertama) --> e
# print(kalimat[-3]) # karakter huruf ke (-3) (pertama) --> n

# Slicing [start:stop:step] --> stop: exclusif, tidak termasuk
# print(kalimat[0:4]) # Mengambil katakter dari index ke-0 hingga index ke 3
# print(kalimat[:4]) # Mengambil katakter dari index ke-0 hingga index ke 3
# print(kalimat[5:8]) # Mengambil katakter 'Sci' dari index ke-5 hingga index ke 7
# print(kalimat[5:11])    # mengambil karakter dari index ke-5 hingga index ke-10
# print(kalimat[5:-1])    # mengambil karakter dari index ke-5 hingga index ke (-2)
# print(kalimat[5:12])    # mengambil karakter dari index ke-5 hingga index ke-11
# print(kalimat[5:])      # mengambil karakter dari index ke-5 hingga terakhir
# print(kalimat[:])       # mengambil karakter dari awal hingga terakhir
# print(kalimat[::2])     # mengambil karakter dari awal hingga terakhir, step maju per 2 langkah
# print(kalimat[::-1])    # mengambil karakter dari awal hingga terakhir, step mundur per 1 langkah
# print(kalimat[5:-5])    # mengambil karakter dari index ke-5 hingga index ke-6 (-6)

# ==================================================
# String Concatenation

# nama_depan = 'Michael'
# nama_belakang = 'Jordan'
# nama_lengkap = nama_depan + nama_belakang
# print(nama_lengkap)

# nama_lengkap = nama_depan + ' ' + nama_belakang
# print(nama_lengkap)

# hobi = nama_lengkap + ' hobi bermain basket'
# print(hobi)

# usia = 30
# # usia_pemain = nama_lengkap + 'berumur' + usia + ' tahun' # --> Error karena usia masih integer
# # print(usia_pemain)

# usia_pemain = nama_lengkap + ' berumur ' + str(usia) + ' tahun' # --> Error karena usia masih integer
# print(usia_pemain)

# bintang = '*'
# banyak_bintang = bintang*5
# print(banyak_bintang)

# ====================================
# string formatting

# usia = 30
# status = 'menikah'
# gaji = 500000.345

# print('saya berumur', usia, 'tahun') # data tidak harus bertipe sama
# print('saya berumur ' + str(usia) + ' tahun') # tipe data harus sama
# print('Saya berumur', usia, 'tahun dan saya sudah', status)
# print('Saya berumur {} tahun dan saya sudah {}'.format(usia, status))
# print('Saya berumur {umur} tahun dan saya sudah {kondisi}'.format(kondisi=status, umur=usia))
# print(f'Saya berumur {usia} tahun dan saya sudah {status} serta memiliki gaji {gaji:,.2f}')


# ===================================
# check string

# in/not in

kalimat = 'Saya senang belajar Data Science'

# print('Data' in kalimat) # True
# print('science' in kalimat) # False
# print('senang' not in kalimat) # False
# print('sedih' not in kalimat) # True

# # count (menghitung banyaknya substring di dalam string)
# print(f"Banyaknya huruf a ada {kalimat.count('a')} buah")
# print(f"Banyaknya huruf nang ada {kalimat.count('nang')} buah")
# print(f"Banyaknya huruf a ada {kalimat.count('data')} buah")

# # endswith
# print(kalimat.endswith('ce')) # True
# print(kalimat.endswith('nce')) # True
# print(kalimat.endswith('science')) # False


# Is 
# kalimat = 'Saya senang belajar Data Science'

# print(kalimat.isdigit()) # Mengecek apa karakter hanya berupa digit/angka # False
# print(kalimat.isalpha()) # mengecek apakah karakter dalam string hanya berupa alfabet
# print(kalimat.isalnum()) # mengecek apakah karakter dalam string hanya berupa alfabet atau angka
# print(kalimat.isspace()) # mengecek apakah karakter dalam string hanya berupa spasi

# kata = "Boeing"

# print(kata.isalpha()) # True
# print(kata.isalnum()) # True

# kata = "Boeing737"
# print(kata.isalpha())   # False
# print(kata.isalnum())   # True
# print(kata.isdigit())   # False

# angka = '1234'
# print(angka.isdigit())  # True
# print(angka.isalnum())  # True

# space = ' '
# print(space.isspace())
