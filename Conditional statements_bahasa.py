# =====================
# Conditional statements
# =====================

# Boolean --> Tipe data yang punya nilai berupa True or False
# print(True)
# print(False)

# ===========================
# Comparison operators:

# print('5>3:', 5 > 3) # lebih besar dari --> True
# print('5<3:', 5 < 3) # lebih besar dari --> True
# print('5>= 6:', 5>= 6) # lebih besar sama dengan --> false
# print('5<= 5:', 5<= 5) # lebih kecil sama dengan --> True
# print('5!= 5:', 5!= 5) # tidak sama dengan --> false
# print('5== 5:', 5== 5) # tidak sama dengan --> false
# print('5 == 5:', 5 == 5)                            # sama dengan --> True
# print('Ridwan == ridwan:', 'Ridwan' == 'ridwan')    # False
# print('a < b:', 'a' < 'b')                          # True (berdasarkan nilai ASCII)
# print('A > a:', 'A' > 'a')                          # False (berdasarkan nilai ASCII)
# print('1 > a:', 1 > 'a')                          # Error karena int tidak bisa dibandingkan dengan str


########################################
# Logical Operators: and, or, not

# ======== and
# and --> semua kondisi harus bernilai True untuk menghasilkan output True
# and --> akan false jika salah satu outputnya False

# print('True and True:', True and True) # True
# print('True and False:', True and False)  # False
# print('True and True:', False and False) # False

# ========= or
# Or --> Akan bernilai True, jika salah satu kondisi bernilai True
# print('True or True:', True or True) # True
# print('True and False:', True or False)  # True
# print('True and True:', False or False) # False

# print('True and True and True:', True and True and True) # True
# print('True and False and True:', True and False and True) # False
# print('True or False or True:', True or False or True) # True
# print('False or False or False:', False or False or False) # False
# print('False or False and True:', False or False and True) # False

# ========== Not
# Memberikan nilai kebalikannya
# print('not True', not True)
# print('not False', not False)

# print(5<3 and 7>8)

# a = 5
# b = 'apple'

# print(a == 5 or b != 'apple')

# =================================
# conditional statement
# =================================

# Conditional Statement
# - program akan melakukan suatu tugas, jika suatu kondisi terpenuhi atau bernilai True
# - definisi: suatu statement yang melibatkan suatu kondisi untuk menentukan tugas apa yang akan dijalankan
# - dimana tugas tersebut hanya akan dikerjakan jika dan hanya jika
# - kondisi yang dievaluasi menghasilkan output True

# Analogi
# jika saya lapar, maka saya makan
# jika saya haus, maka saya minum

# =====================
# IF statement
# ====================

#======================================================
# IF statement
# Jika kondisi terpenuhi (bernilai True), maka tugas akan dikerjakan oleh program
# Jika kondisi tidak terpenuhi (bernilai False), maka program tidak akan menjalankan perintah

# Contoh 1
# if True:
#     print('program akan dijalankan')

# Contoh 2
# if False:
#     print('Program akan dijalankan')

# contoh 3
# age = 17

# if age >= 17:
#     print(f'Usia anda {age} tahun. Pengajuan SIM anda diterima')
#     print('Silahkan hubungi kantor polisi terdekat')

# print('Program berakhir') # bukan bagian dari if statement karena tidak menggunakan indentasi


# contoh 4
# nilai_1 = 10
# nilai_2 = 20

# if nilai_1 > 15 or nilai_2 > 15: # False or True --> True # maka dijalankan
#     hasil = nilai_1 + nilai_2
#     print(hasil)


# Latihan:  Seorang warga Indonesia akan dapat beasiswa jika IELTSnya diatas 6

# input_ielts = float(input('Berapa nilai IELTS anda?')) # Input itu selalu string # Maka di casting jadi float/integer

# if input_ielts > 6:
#     print('nilai IELTS anda:', input_ielts)
#     print('Selamat anda mendapatkan beasiswa')

# ====================================================
# IF ELSE statement

# Jika kondisi pada IF bernilai True, maka statement True di jalankan
# Jika kondisi pada IF tidak terpenuhi, maka statement pada else yang akan dijalankan
# age = 15

# if age >= 17:
#     print(f'Usia anda {age} tahun. Pengajuan SIM Anda diterima')
#     print('Silakan hubungi kantor polisi terdekat')
# else:
#     print('Usia Anda belum memenuhi persyaratan')
#     print('Tunggu hingga usia Anda mencapai 17 tahun')

'''
Soal: Buatlah aplikasi yang meminta inputan sebuah angka dari seorang user
# Kemudian aplikasi akan menampilkan output:
# angka yang anda masukkan adalah bilangan GANJIL, jika angka bernilai ganjil
# angka yang anda masukkan adalah bilangan GENAP, jika angka bernilai genap
# angka yang anda masukkan adalah TIDAK VALID, jika angka lebih kecil atau sama dengan 0
'''
# Soal
# input_angka =int(input('Masukkan angka!'))

# if input_angka <= 0:
#     print('Angka TIDAK VALID')
# else:
#     if input_angka % 2 == 0:
#         print('Angka bernilai GENAP')
#     else:
#         print('Angka bernilai Ganjil')

# ===========================================
# IF ELIF ELSE Statement

# - Jika kondisi pada IF bernilai True, maka statement pada IF akan dijalankan
# - Jika kondisi pada IF bernilai False, maka kondisi pada ELIF akan dievaluasi
# - Jika kondisi pada ELIF bernilai True, maka statement pada ELIF akan dijalankan
# - Jika kondisi pada ELIF bernilai False, maka statement pada ELSE yang akan dijalankan
# - Hanya salah satu kondisi yang dijalankan

# kasus 1
# if True:
#     print('ini adalah statement di IF')
# elif False:
#     print('ini adalah statement di ELIF')
# else:
#     print('ini adalah statement di ELSE')

# Kasus 2
# if False:
#     print('Ini adalah statement pada IF')
# elif True:
#     print('Ini adalah statement pada ELIF')
# else:
#     print('Ini adalah statement pada ELSE')


# # Kasus 3
# if False:
#     print('Ini adalah statement pada IF')
# elif False:
#     print('Ini adalah statement pada ELIF')
# else:
#     print('Ini adalah statement pada ELSE')

# Kasus 4
# if True:
#     print('Ini adalah statement pada IF')
# elif True:
#     print('Ini adalah statement pada ELIF')
# else:
#     print('Ini adalah statement pada ELSE')

# Kasus 5 # Kedua if dijalankan
# print('Kasus 5')
# if True:
#     print('Ini adalah statement pada IF 1')
# if True:
#     print('Ini adalah statement pada IF 2')
# else:
#     print('Ini adalah statement pada ELSE')

'''
Soal 
Jika score 90 atau lebih, maka grade A
    score 80 - 89 maka grade B
    score 70 - 79 maka grade C
    score 60 - 69 maka grade D
    score dibawah 60 maka grade #
'''

# score = float(input('Masukkan score anda: '))

# if score < 0 or score > 100:
#     print('nilai tidak valid')
# else:
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'E'
#     print(f'nilai Anda {score}. Anda mendapatkan grade {grade}')


'''
Latihan
Buatlah sebuah program 'Suit' yang apabila anda memasukkan input:
input 1, maka anda memilih 'batu'
input 2, maka anda memilih 'gunting'
input 3, maka anada memilih 'kertas'

'''
# input_suit = float(input('Masukkan angka 1,2, atau 3: '))

# if input_suit != 1 and input_suit !=2 and input_suit !=3:
#     print('Input anda Tidak Valid')
# else:
#     if input_suit == 1:
#         print('Anda memilih batu')
#     elif input_suit == 2:
#         print('Anda memilih gunting')
#     elif input_suit == 3:
#         print('Anda memilih kertas')
