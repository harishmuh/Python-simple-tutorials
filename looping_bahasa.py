#================================
# Looping statement
#================================
# Tujuan: mengeksekusi suatu bagian kode secara berulang

# Menampilkan 3 baris yg sama secara manual
# print('Saya sedang belajar Data Science')
# print('Saya sedang belajar Data Science')
# print('Saya sedang belajar Data Science')

# Cara looping
# for i in range(5): # Print 5 kali
#     print('Saya sedang belajar data science')

# ================================================
# While loop - Mengulang selama kondisi masih benar
# ================================================
# Selama kondisi masih terpenuhi
# maka looping akan terus dijalankan
# Looping akan berhenti ketika kondisinya sudah bernilai false

# infinite loop
# Why: program jalan terus--> diberikan kondisi yg selalu bernilai True ---> HARUS DIHINDARI

# x = 1
# while x <=5: # Akan terus berjalan karena kondisinya selalu True, x = 1 # HARUS DIHINDARI
#     print('Saya sedang belajar data sains') # Cara berhenti: Ctrl + C

# Contoh while
nyawa = 3
while nyawa > 0:
    print("Main game...")
    nyawa -= 1  # kurangi 1 nyawa setiap kali

# Contoh while 1
# x = 1
# while x <= 5:
#     print('Saya sedang belajar data science')
#     x = x + 1

# Contoh while 2 
# angka = 1
# while angka <= 3:
#     print(f'Angka: {angka}')
#     angka += 1

#contoh while 3 # hasilnya 2,3,4
# angka = 1
# while angka <= 3:
#     angka += 1
#     print(f'Angka: {angka}')

# =========================================
# WHILE ELSE statement
# =========================================
# angka = 0
# while angka < 3:
#     print(f'saya sedang belajar data sains sesi ke - {angka + 1}')
#     angka = angka + 1
# else:
#     print('saya mau istirahat')

'''
# Soal:dengan menggunakan loop
# Tampilkan angka genap sampai 14
''''

# # Cara 1
# angka = 0
# while angka < 15:
#     if angka % 2 == 0:
#         print(angka, end = ' ')
#     angka = angka + 1
# print()

# cara 2
# angka = 2
# while angka < 15:
#     print(angka, end = ' ')
#     angka = angka + 2


# ==================
# For Loop
# ==================
# Loop akan dijalankan selama item atau elemen 
# di dalam collection data types atau iterables masih ada
# Mengulang sejumlah yang sudah pasti
# Sederhananya: lakukan ini untuk setiap item dalam daftar

teman = ["Andi", "Budi", "Citra"]
for nama in teman:
    print("Halo", nama)

# Output:
# Halo Andi
# Halo Budi
# Halo Citra

# =====================
# Looping dalam list
# =====================

# Contoh 1
# for i in [2,4,6,8]:
#     print(f'angka dalam list: {i}')

# contoh 2
# list_angka = [2,4,6,7,9]
# for value in list_angka:
#     print(value)

# contoh 3
# list_angka = [1,2,3,4,5]
# for value in list_angka[1:4]: # mulai dari Index 1 hingga index sebelum 4
#     print(f'Nilai: {value}')

# contoh 4
# list_angka = [3, 6, 9, 12, 15]
# for value in list_angka:
#     print('saya sedang belajar') # akan ke print 5 kali sesuai jumlah item di dalam list

# contoh 4.5
# list_angka = [3, 6, 9, 12, 15]
# for value in list_angka:
#     print(f'saya sedang belajar DS sebanyak {value} jam') # akan ke print 5 kali sesuai jumlah item di dalam list

# contoh 5
# list_peralatan = ['buku', 'tas', 'pensil']
# for peralatan in list_peralatan:
#     print(f'Saya membawa {peralatan}')

# contoh 6
# for loop untuk menjumlahkan seluruh angka di dalam list
# list_angka = [2, 5, 7, 9, 14, 23, 35, 61, 78, 100]

# total = 0
# for angka in list_angka:
#     total += angka          # setara dengan total = total + angka

# print(f'Totalnya adalah: {total}') 

#========================================================
# Looping pada range (start, stop, step)
#========================================================

# by default start dari 0, step per 1 langkah
# stop tidak termasuk

# print('range(5)')
# for value in range(5): # range(stop): start=0, stop=5, step=1
#     print(value)

# print('range(2,5)')
# for value in range(2,5):     # range(start, stop): start=2, stop=5, step=1 
#     print(value)

# print('range(2,10,3)')
# for value in range(2,10,3):     # range(start, stop, step): start=2, stop=10, step=3 
#     print(value)

# print('range(3,0,-1)')
# for value in range(3,0,-1):     # range(start, stop, step): start=3, stop=0, step=-1
#     print(value)

'''
Soal dengan menggunakan for loop, tampilkan output sebagai berikut
output
list = [1, 4, 9, 16, 25]
'''
# list = [1, 4, 9, 16, 25]
# for i in range(1,6):
#     print(i**2, end=' ')

'''
# Soal 2: Dengan menggunakan for loop, tampilkan output sebagai berikut
# # Output:
# # Angka 1 bukan kelipatan 3
# # Angka 2 bukan kelipatan 3
# # Angka 3 kelipatan 3
# # Angka 4 bukan kelipatan 3
# # Angka 5 bukan kelipatan 3
# # Angka 6 kelipatan 3
'''
# for i in range(1,7):
#     if i%3==0:
#         print(f'Angka {i} kelipatan 3')
#     else:
#         print(f'Angka {i} bukan kelipatan 3')

'''
# soal 3: buat for loop dengan menggunakan range jika diketahui list berikut
# list_buah = ['jeruk', 'apel', 'mangga'] 
# Output: 
# buah ke 1 adalah jeruk
# buah ke 2 adalah apel
# buah ke 3 adalah mangga
'''
# list_buah = ['jeruk', 'apel', 'mangga']
# for i in range(len(list_buah)):
#     print(f'Buah ke-{i+1} adalah {list_buah[i]}')

# ========================
# Looping pada tuple
# ========================
# tuple_buah = ('mangga', 'apel', 'pisang')
# for buah in tuple_buah:
#     print(buah)

'''
soal
my_tuple = (['mangga', 10000], ['apel', 15000], ['pisang', 20000])'
Output
Buah mangga harganya 10000
'''
my_tuple = (['mangga', 10000], ['apel', 15000], ['pisang', 20000])
# for buah in my_tuple:
#     print(f'Buah {buah[0]} harganya {buah[1]}')

# Cara unpacking
# for nama, harga in my_tuple:
#     print(f'buah {nama} harganya {harga}')

# ========================
# Enumerate
# ========================

# Enumerate
# Mengeluarkan index dan value

list_buah = ['jeruk', 'apel', 'mangga']
# for buah in enumerate(list_buah):
#     print(buah)

# for id, buah in enumerate(list_buah):
#     print(f'Buah ke - {id+1} adalah {buah}')

# =============================
# Looping pada dictionary
# ==============================


myDict = {
    'toyota': 'inova',
    'honda': 'civic',
    'daihatsu' : 'sigra'
}

# Output hanya berupa key
# for mobil in myDict:
#     print(mobil) 

# Output berupa values
# for value in myDict.values():
#     print(value)

# Output berupa key and value
# for x,y in myDict.items():
#     print(x,y)

'''
# Soal: dengan menggunakan for loop pada dictionary
# myDict = {
#      'toyota': 'innova',
#      'honda': 'civic',
#      'daihatsu': 'sigra'
# }
# Tampilkan output:
# Brand toyota mengeluarkan tipe innova
# Brand honda mengeluarkan tipe civic
# Brand daihatsu mengeluarkan tipe sigra

'''
# Cara 1
# for merk, mobil in myDict.items():
#     print(f'Brand {merk} mengeluarkan tipe {mobil}')
# Cara 2
# for item in myDict.items():
#      print(f'Brand {item[0]} mengeluarkan tipe {item[1]}')

# ===================
# Looping pada string
# ===================

# Kita melakukan looping pada setiap karakter

# kalimat = 'kita manusia'

# for char in kalimat: # Print per huruf untuk setiap huruf di 'kalimat'
#     print(char)

# for char in kalimat: # print 'kalimat'
#     print(char, end='')

# =======================================================
# Break, continue, pass (loop control statement)
#========================================================
# Break--> keluar dari sistem looping # stop
# continue --> lanjut 

# =======================================================
# Break - berhenti total dari loop meskipun belum selesai
# =======================================================
# Sederhananya: Jika menemukan suatu kondisi yang dicari, berhenti dari loop sekarang juga

# # Break
# # Kamu sedang mencari teman bernama "Juliana". Saat ketemu, berhenti cari meskipun ada nama lain
# teman = ["Dewi", "Diandra", "Lutfi", "Michael", "Juliana", "Fatimah", "Andi"]
# for nama in teman:
#     if nama == "Juliana":
#         print("Ketemu Juliana!")
#         break
#     print("Bukan Juliana:", nama)

# Break
# kalimat = 'Saya senang bermain bola'
# for char in kalimat:
#     if char == 'm':
#         break
#     print(char, end ='')
# print()

# Contoh lain (Break)
# Berhenti ketika bertemu batu merah
list_batu = ['kuning', 'hijau', 'ungu', 'merah', 'biru']
# for batu in list_batu:
#     if batu == 'merah':
#         print('Stop ada batu merah, berhenti!')
#         break # Stop looping
#     print(f'melangkah diatas batu {batu}')

# =========================================================
# Continue - Lewati satu langkah, lanjut ke yang berikutnya
# =========================================================
# Sederhananya, jika menemukan kondisi tertentu, lewati bagian ini dan langsung ke item berikutnya

# Continue
# for batu in list_batu:
#     if batu == 'hijau':
#         print('Batu hijau, lewati saja')
#         continue # skip batu hijau
#     print(f'melangkah diatas batu {batu}')

# Sapa semua teman kecuali "Lufti"
# teman = ["Dewi", "Diandra", "Lutfi", "Michael", "Juliana", "Fatimah", "Andi"]
# for nama in teman:
#     if nama == "Lutfi":
#         continue # Lewati
#     print("Halo", nama)

# ===============================
# Pass - Tidak melakukan apa-apa
# ===============================
# Digunakan saat belum tau ingin menulis apa, tapi secara sintask harus diisi

# Pass
# for angka in range(1, 6):
#     if angka == 3:
#         pass  # tidak melakukan apa-apa
#     print("Angka:", angka)

# Pass
# for batu in list_batu:
#     if batu == 'ungu':
#         pass # Do nothing
#     print(f'melangkah diatas batu {batu}')
# # batu ungu diabaiakan, Program berjalan seperti biasa

'''
Soal:
Buatlah program Python yang meminta pengguna untuk memasukkan password (misal password = '123'). 


Program harus:
-Meminta pengguna memasukkan password berulang kali hingga benar.
-Jika password yang dimasukkan salah, tampilkan pesan: "Password salah, ulangi inputan".
-Jika password yang dimasukkan benar, tampilkan pesan: "Password benar" dan hentikan program.
Gunakan perulangan while True dan pernyataan break.
'''
# Jawaban
# password = 123

# while True:
#     pwd = int(input('Masukkan password: '))
#     if pwd == password:
#         print('Password benar')
#         break
#     print('Password salah, ulangi inputan')

# ================
# Nested loop
# ================

# Nested loop adalah loop di dalam loop
# Cara berjalan:
# Loop luar akan dijalankan 
# Lalu loop dalam akan jalan sepenuhnya (diselesaikan) untuk setiap langkah loop luar

# kelas = ["Data science", "Web Development", "Digital Marketing"] # outer loop
# for nama_kelas in kelas:
#     print("Masuk ke kelas", nama_kelas)
#     for siswa in range(1, 3):  # siswa 1 dan 2 # Inner loop
#         print(f"  Siswa ke-{siswa} di kelas {nama_kelas}")

# for suap in range(1,4):
#     print(f'ini adalah suapan ke - {suap}')
#     for lauk in ['nasi', 'rendang', 'daun nangka', 'sambal']:
#         print(f'lauknya adalah {lauk}')

