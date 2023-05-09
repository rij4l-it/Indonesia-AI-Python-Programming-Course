
# Latihan Variable dan Data Type

email = 'rij4l.it@gmail.com'
print(email)
print(type(email))

angka = 10
print('')
print(angka)

angka = 100
print('')
print(angka)
print(type(angka))
angka = float(angka) # rubah type data
print(type(angka))

angka = 0.67
print('')
print(angka)
print(type(angka))

angka1, angka2, mail = 10, 0.1, 'rij4l1314@gmail.com'
print('')
print(angka1)
print(angka2)
print(mail)

angka3 = angka4 = angka5 = 100
print('')
print(angka5)

'''
CONSTANTA
dengan cara pemberian nama variable dengan huruf besar semua
'''
PI = 3.14
GRAVITY = 9.8

# Naming
nama_variable = "latihan 2"
NAMA_VARIABLE = "LATIHAN 2 AJA"
print('')
print(nama_variable)
print(NAMA_VARIABLE)

# Ceil
a = 8.567
b = a.__ceil__()
print('')
print(b)

# Round
a = 8.5
b = a.__round__()
print('')
print(b)

# String
s = "Belajar String"
print('')
print(s)
print(type(s))

s = ''' 
    Belajar string multiline
    contohnya seperti ini
    coba bisa kan
'''
print('')
print(s)
print(type(s))

s = "Belajar String"
s = s.lower()
print('')
print(s)

s = "Belajar String"
s = s.upper()
print('')
print(s)

s = "Belajar String"
s = s.replace("String", "Coding")
print('')
print(s)

nama = "Budi"
s = "nama saya adalah {}".format(nama)
print('')
print(s)
s = f"nama saya adalah {nama}"
print('')
print(s)

print('')
# Boolean
b = True
print(type(b))

print(b == 1)
print(b == 0)

print(type(b == 1))
print('')

print(True and True) # and / &
print(False and True) 
print(False and False)
print(False or True) # or / |

print('')

# List, Tuple, Dictionary
l = [1, 0.4, 'data']
print(l)
print(type(l))
print(l, "merupakan tipe data", type(l))

t = (2, 4.4, 'data2')
print('')
print(t)
print(type(t))
print(t, "merupakan tipe data", type(t))

d = {'data1':1, 'data2':'isi2'}
print('')
print(d)
print(type(d))
print(d, "merupakan tipe data", type(d))
print('')
print('')

# Start Exercise
# Buatlah 2 variable yang memuat string
# Variable 1 memuat "Hello, "
# Variable 2 memuat "Python!"
# Lalu gabungkan kedua string tersebut dan tampung di variable hasil seperti ini
# hasil = variable1 + variable2
# Pastikan string yang ada bersifat upper-case
# Lalu cek apa Data Type dari variable hasil tersebut!

variable1 = "Hello"
variable2 = "Python!"
hasil = f"hasil = {variable1} + {variable2}"
hasil = hasil.upper()
print(hasil)
print(type(hasil))