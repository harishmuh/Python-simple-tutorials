# =====================
# Collection data types
# =====================

# ===========
# [list] 
# ===========
# Kurung siku
# List seperti box, dapat menerima item/elements berbagai tipe data (int, string, float, boolean, list)
# Dapat menampung nilai yang duplicat
# Mutable artinya item dalam list dapat diubah/ditambah/dikurangi
# Punya index, berurutan, jadi bisa dilakukan indexing dan slicing

# =============

# 1. dapat menerima item/elements berbagai tipe data
# list_contoh = ['hello', 3, 2, 1, True]
# # print(list_contoh)

# list_dalam_list = ['hello', 1, 2, 3, False, [4,5,6], list_contoh]
# # print(list_dalam_list)

# # # =========================
# # # 2. dapat menampung nilai yang sama atau duplicates
# # list_contoh_1 = ['hello', 3, 2, 1, True, 6, 6, 6]
# # print(list_contoh_1)

# # ===========================
# # 3. Berurutan, jadi bisa dilakukan indexing dan slicing
# list_dalam_list = ['hello', 1, 2, 3, False, [4,5,6], list_contoh]

# # indexing
# print('index ke 0:', list_dalam_list[2])

# # slicing
# print(list_dalam_list[::2])

# ================================
# # 4. mutable, item list dapat diganti/diubah

# list_dalam_list = ['hello', 1, 2, 3, False, [4,5,6], list_contoh]
# # list_dalam_list[0] = 'hi'
# # print(list_dalam_list) # ['hi', 1, 2, 3, False, [4, 5, 6], ['hello', 3, 2, 1, True]]

# # mengubah list dalam list
# list_dalam_list[5][1] = '30'
# print(list_dalam_list) # ['hello', 1, 2, 3, False, [4,30,6], list_contoh]

#================================================
# Membership Operator
# Mengecek apakah suatu nilai ada di dalam list (in & not in)

# list_contoh = ['Hello', 3, 2, False, True, [10, 20, 30], 6, 6, 6]

# print('Hello' in list_contoh)           # True
# print(20 in list_contoh)                # False
# print(20 in list_contoh[5])             # True
# print([10, 20, 30] in list_contoh)      # True
# print(6 in list_contoh)                 # True
# print(1 in list_contoh)                 # True, nilai True pada list dianggap 1
# print(0 in list_contoh)                # True, nilai False pada list dianggap 0

#=========================================
# Mengecek index pada list

# Hello pada indeks ke-0
# # print(list_contoh.index(20))          # error --> 20 tidak ada di dalam list 
# print(list_contoh.index(6))             # menampilkan indeks yang pertama ditemui: ke-6
# print(list_contoh.index(0))             # nilai False dianggap sebagai 0
# print(list_contoh.index(1))             # nilai True dianggap sebagai 1
# print(list_contoh.index([10, 20, 30]))  # [10, 20, 30] pada indeks ke-5
# print(list_contoh[5].index(20))         # 20 pada indeks ke-1 pada list_contoh[5]
# print(list_contoh[list_contoh.index([10, 20, 30])].index(20))         # 20 pada indeks ke-1 pada list_contoh[5]
# print([10, 20, 30].index(20))           # 20 pada indeks ke-1 pada [10, 20, 30]

# #==================================================
# Indirect Assignment

# a = 100
# b = 200

# a = b

# a = 500

# print(a)
# print(b)

#-----------------------

# list_a = [10, 20, 30, 40]

# list_b = list_a

# print('List_a awal:', list_a)
# print('List_b awal:', list_b)

# list_b[-1] = 100
# print('List_b akhir:', list_b)
# print('List_a akhir:', list_a)

#-------------------------
# Gunakan .copy() agar list_a yang awal tidak ikut berubah
# print('------.copy()------')
# list_a = [10, 20, 30, 40]

# list_b = list_a.copy()

# print('List_a awal:', list_a)
# print('List_b awal:', list_b)

# list_b[-1] = 100
# print('List_b akhir:', list_b)          # Item pada indeks terakhir di list_b berubah
# print('List_a akhir:', list_a)          # Item pada indeks terakhir di list_a TIDAK ikut berubah

# ======================================
# List concatenating
# ======================================



#==============================================
# Menambahkan item/element ke dalam list

# append: menambah 1 item ke dalam list

# Contoh 1
# mobil = ['toyota', 'vw', 'honda']
# unit_baru = 'lamborghini'

# mobil.append(unit_baru)         # tidak bisa diassign ke variabel
# print(mobil)
# print(len(mobil))

# # Contoh 2
# mobil = ['toyota', 'vw', 'honda']
# unit_baru = ['lamborghini', 'nissan']

# mobil.append(unit_baru)         
# print('Menggunakan append:', mobil)            #['lamborghini', 'nissan'] masuk ke dalam mobil sebagai list utuh (1 item)
# print(len(mobil))     

# # Contoh 3
# # mobil = ['toyota', 'vw', 'honda']

# # mobil.append('lamborghini', 'nissan')      # error --> karena hanya meminta 1 argumen kita masukkan 2     
# # print(mobil)          
# # print(len(mobil))

# ===================

#----------------------------------------
# extend: menambahkan item-item pada list sebagai item-item tersendiri dalam list baru

# Contoh 1
# mobil = ['toyota', 'vw', 'honda']
# unit_baru = ['lamborghini', 'nissan']

# mobil.extend(unit_baru)         
# print('Menggunakan extend:', mobil)            #['lamborghini', 'nissan'] masuk ke dalam mobil sebagai item tersendiri
# print(len(mobil)) 

#-------------------------------------
# insert: menyelipkan sebuah item di dalam list

# # Contoh 1
# mobil = ['toyota', 'vw', 'honda']
# unit_baru = ['lamborghini', 'nissan']

# mobil.insert(0 ,unit_baru)         
# print('Menggunakan insert:', mobil)   # ['lamborghini', 'nissan'] diselipkan pada indeks ke-0 sebagai 1 list utuh   
# print(len(mobil))


# Latihan harish
# ================
# num = []
# for i in range(1, 10, 2):
#     num.append(i)
# print(num)

# list_angka = []
# for i in range(5):
#     list_angka.append(10**i)
# print(list_angka)


# ==================================
# Tuple

# ditandai ()
# Mirip dengan list dapat menyimpan item dengan berbagai macam tipe data
# Bisa memiliki item yang duplikat
# Memiliki urutan, bisa dilakukan indexing dan slicing
# Immutable, item dalam tuple tidak bisa diganti

#----------------------------------
# Bisa duplikat dan bermacam-macam tipe data
# tuple_contoh = ('Hello', 3, 2, 1, True, [10, 20, 30], 6, 6, 6)
# print(tuple_contoh)

# Bisa dilakukan indexing dan slicing
# print(tuple_contoh[1])              # 3
# print(tuple_contoh[1:5])            # (3, 2, 1, True)

# Immutable
# tuple_contoh[1]='Hai'               # error --> 'tuple' object does not support item assignment
# tuple_contoh[5] = [10, 20, 40]      # error

# tuple_contoh[5][1] = 30             # bagian ini mengubah list

# ======================================
# Seandainya kita ingin mengubah item dalam tuple
# 1. ubah tuple menjadi list
# list_contoh = list(tuple_contoh)
# print(list_contoh)

# # 2. ubah nilainya
# list_contoh[1]='Hai' 
# print(list_contoh)

# # 3. mengembalikan list menjadi tuple
# tuple_contoh = tuple(list_contoh)
# print(tuple_contoh)
# ==================

#---------------------------------
# Menambahkan item pada dictionary

# dict_contoh = {
#     'Nama': ['Ridwan', 'Boni'],
#     'Usia': [25, 23],
#     'Program': 'Data Science',
#     'Status': 'rahasia',
# }

# # cara 1 - satu per satu
# dict_contoh['Hobi'] = ['Membaca', 'Berenang']
# print(dict_contoh)

# # cara 2 - satu atau lebih
# dict_contoh.update({'Domisili':'Bandung', 'Cita-cita': ['Data Scientist', 'Data Analyst']})
# print(dict_contoh)

# # del (menghapus 1 item)
# del dict_contoh['Status']
# print(dict_contoh)

#======================================================
# Dictionary awal:
# my_dict = {
#     'susu': {'merk': 'ultra', 'harga': 5000},
#     'mie instant': {'merk': 'indomie', 'harga': 3000},
#     'minyak': {'merk': 'bimoli', 'harga': 36000}
# }

# while True:
#     print('''Pilihan Menu
#     1. Menambahkan produk
#     2. Menghapus produk
#     3. Keluar program
#     ''')

#     pilihan = input('Masukkan menu (1/2/3): ')

#     if pilihan=='1':
#         produk = input('Masukkan produk: ')
#         merk_produk = input('Masukkan merk: ')
#         harga_produk = int(input('Masukkan harga: '))
#         my_dict.update({produk:dict(merk=merk_produk, harga=harga_produk)})
#         print('Input data berhasil:', produk, ':', my_dict[produk])
#         print(my_dict)
#     elif pilihan=='2':
#         produk = input('Masukkan produk yang ingin dihapus: ')
#         del my_dict[produk]
#         print(my_dict)
#     elif pilihan=='3':
#         print('Terima kasih')
#         break
#     else:
#         print('Masukan inputan yang benar')


#=====================================================
# Soal 
# buat program terdiri dari 2 menu
# menu pertama untuk menambahkan item ke dictionary
# sedangkan menu kedua untuk menghapus item dalam dictionary
# item yang ditambahkan atau dihapus sesuai dengan inputan user

# # dictionary awal:
# my_dict = {
#     'susu': {'merk': 'ultra', 'harga': 5000},
#     'mie instant': {'merk': 'indomie', 'harga': 3000},
#     'minyak': {'merk': 'bimoli', 'harga': 36000}
# }

# while True:
#     print('''Pilihan menu
# 1. Menambahkan produk
# 2. Menghapus produk
# 3. keluar program
#       ''')
#     pilihan = input('Pilih menu (1/2/3): ')

#     if pilihan == '1':
#         produk = input('Masukkan produk: ')
#         merk_produk = input('Masukkan merk: ')
#         harga_produk = int(input('Masukkan harga: '))
#         my_dict[produk] = dict(merk=merk_produk, harga=harga_produk)
#         print(my_dict)
#     elif pilihan == '2':
#         produk = input('Masukkan produk yang akan dihapus: ')
#         del my_dict[produk]
#         print(my_dict)
#     elif pilihan == '3':
#         print('Terima kasih')
#         break
#     else:
#         print('Masukkan inputan yang benar')

#=====================================================


#===================================================
# SET

# ditandai dengan kurung kurawal {}
# Dapat menyimpan item dengan berbagai macam tipe data
# Tidak bisa menyimpan data duplikat
# Tidak memiliki urutan sehingga tidak bisa dilakukan indexing
# Mutable
# Biasa digunakan untuk membuang duplikat

# -------------------------------------
# # Tidak bisa duplikat (harus unik)
# set_contoh = {'Hello', 3, 2, 1, True, 6, 6, 6}
# print(set_contoh)

# # Tidak memiliki urutan jadi tidak bisa diindexing
# # set_contoh[3]   # error

# # Tetapi masih bisa dilooping
# for i in set_contoh:
#     print(i)

# #--------------------------------
# # Menghitung jumlah item pada set
# print(set_contoh)
# print(len(set_contoh))

# #-------------------------------------------------
# Menghapus item pada set

# set_contoh = {2.5, True, 10, 'Hello', 3.5, 5, 'Hai', 10}
# print('Kondisi awal:', set_contoh)

# # remove
# set_contoh.remove('Hai')
# print('setelah remove("Hai"):', set_contoh)

# # discard
# set_contoh.discard(10)
# print('setelah discard(10):', set_contoh)

# # pop (menghilangkan 1 item secara acak)
# set_contoh.pop()
# print('setelah pop():', set_contoh)

# # clear
# set_contoh.clear()

#================================
#------------------------------------------------------
# issubset, issuperset

# prima = {3, 5, 7}
# ganjil = {1, 3, 5, 7, 9}
# genap = {2, 4, 6}

# # mengecek apakah suatu himpunan merupakan himpunan bagian
# print('Prima issubset ganjil:', prima.issubset(ganjil))

# # mengecek superset
# print('Ganjil issuperset prima:', ganjil.issuperset(prima))

# # mengecek apakah kedua itemnya tidak beririsan
# print('Ganjil isdisjoint genap:', ganjil.isdisjoint(genap))

# =================================================
# zip

# soal
# list_harga = [20000, 15000, 10000]
# list_buah = ['apel', 'jeruk', 'mangga']

# output 
# harga apel 20000
# harga jeruk 15000
# harga mangga 10000

#=== cara ke 1
# x = 0
# for i in list_buah:
#     print(f'harga {i} {list_harga[x]}')
#     x += 1 
#==== cara pake enumerate
# for index, buah in enumerate(list_buah):
#     print(f'harga {buah} {list_harga[index]}')
#======= cara pake zip

# list_harga = [20000, 15000, 10000]
# list_buah = ['apel', 'jeruk', 'mangga']
