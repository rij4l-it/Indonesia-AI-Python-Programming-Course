#------------------------------
# CONDITION
#------------------------------
jumlah_penumpan = 3

if jumlah_penumpan > 10 :
    pass # Untuk membypass isi dari kondisi klo tidak di isi nti next codingnya bisa error

if jumlah_penumpan < 10 :
    pass

print("Di Luar Condition")
print('')

if jumlah_penumpan > 10 :
    print('Mobil siap berjalan')

if jumlah_penumpan < 10 :
    print('Mobil masih menunggu penumpang...')

print('')
score = 78

if score > 75:
    print('Lulus')
elif score < 10:
    print('Tidak Lulus')

if score >=85:
    print('Predikat A / Memuaskan')
elif score >=75:
    print('Predikat B / Bagus')
else:
    print('TIdak Lulus')

print('')

# NESTED IF ( if di dalam if )
kelas = 3
score = 90

if kelas > 1:
    if score >=85:
        print('Predikat A / Memuaskan')
    elif score >=75:
        print('Predikat B / Bagus')
    else:
        print('TIdak Lulus')
else:
    if score > 80:
        print('Predikat A / Bagus')
    else:
        print('Tidak Lulus')

print('')

# Input data
num = float(input('Masukan Angka : '))
if num >= 0:
    if num == 0:
        print('Nol')
    else:
        print('Angka Positif')
else:
    print('Angka Negatif')

print('')

# Exercise
# Buatlah satu logika kondisi yang menentukan jika harga laptop sekian maka 
# saya akan mempertimbangkan lagi jika harga handphone sekian maka saya akan beli keduanya atau tidak
# Gunakan teknik NESTED IF!

#harga_laptop = 0
#harga_handphone = 0
#print("Saya akan beli laptopnya.")

laptop = float(input('Masukan harga laptop : '))
hp = float(input('Masukan harga hp : '))

if hp < 3000000 :
    if laptop >= 5000000:
        print('Saya akan beli laptopnya')
    else:
        print('saya akan beli keduanya')
else:
    if laptop >= 5000000:
        print('Saya akan beli laptopnya')
    else:
        print('saya akan mempertimbangkan')

