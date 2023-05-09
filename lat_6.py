#------------------------------
# FUNCTION
#------------------------------

# function Non parameter
def halo_dunia():
    var = "Halo Python, Halo dunia..."
    print(var)

halo_dunia()

print('')

# function parameter
def selamat_datang(nama):
    var = f'Halo {nama}, welcome!'
    print(var)

selamat_datang('rijal')

def selamat_datang(nama, dari):
    var = f'Halo {nama}, dari {dari}!'
    print(var)

selamat_datang('rijal', 'jakarta')
selamat_datang(dari='jogja', nama='budi')

def selamat_datang(*daftar_nama):
    var = 'Halo '
    for nama in daftar_nama:
        var += nama + ', '
    
    var += 'Welcome'
    print(var)

selamat_datang('satu', 'dua', 'tiga')

print('')

# function Anonim
double = lambda x : x * 2

print(double(5))

print('')

# Bonus = Docstring
def selamat_datang(nama):
    '''
    Ini adalah function untuk menyapa
    nama yang telah ada pada parameter
    '''
    var = f'Halo {nama}, welcome!'
    print(var)

selamat_datang('rijal')
print(selamat_datang.__doc__) # mencetak string comment

# Bonus Scope & Return
a = 2
b = 1
x = 100

def operasi(a, b, c=1): # nilai c diberikan secara default jika pada pemanggilan fungsi tidak di cantumkan.
    op1 = a + b
    op2 = op1 // c

    print('a di dalam function:', a) # nilai scope di dalam function
    print('b di dalam function:', b)

    print(x)

    return op2 # memberikan nilai balik

hasil = operasi(a=10, b=5, c=3)
print(hasil)

print('a di luar function:', a) # nilai scope di luar function
print('b di luar function:', b)

print('')

# Exercise
# Buatlah fungsi yang akan mengevaluasi apakah modulus dari hasil kali 2 angka yang diterima bernilai 0 atau tidak
# Gunakan statement return untuk mengembalikan nilai tersebut lalu cetak hasilnya
# Beri nama cek_modulus() pada fungsi tersebut
print('Exercise')

angka1 = 12
angka2 = 8

def cek_modulus(a, b):
    a *= 2
    b *= 2
    y = a % b

    return y

hasil = cek_modulus(12, 8)
print('Modulus dari 12 dan 8 adalah = ', hasil)
