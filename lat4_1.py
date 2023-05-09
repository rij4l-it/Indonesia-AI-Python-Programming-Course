#------------------------------
# CLASS
#------------------------------

class Cat:
    '''
    Ini adala class untuk membuat object kucing
    Melalui class ini kita bisa mendefinisikan nama dan juga tipe dari kucing yang kita buat
    '''
    spesies = 'kucing'

    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

    def run(self, speed):
        print(f"Kucing {self.nama} berlari dengan {speed}")
    
    def play(self):
        print(f"Kucing {self.nama} bermain dengan kucing lainnya...")
    
    def eat(self):
        pass

# Membuat objek
Kinako = Cat(nama='Kinako', tipe='Anggora')
Minto = Cat(nama='Minto', tipe='Persia')

print(Kinako)
print(Minto)

print(Kinako.nama)
print(Kinako.tipe)

Kinako.run('cepat')
Kinako.play()

print(Kinako.__doc__)

print(f"Kinako adalah seekor {Kinako.__class__.spesies}")

print(f"{Kinako.nama} merupakan kucing jenis {Kinako.tipe}")


'''
class Employee():
    
    # Ini adalah Class untuk memanipulasi data employee
    # Melalui kelas ini kita bisa memanipulasi data yang ada seperti baca, hapus dan tambah
    

    def __init__(self, lokasi_file):

        self.data_employee = open(f'{lokasi_file}', mode='r', encoding='utf-8')
        self.data_per_sesi = 10

    def baca_data(self):

        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee

    def hapus_data(self, baris, kolom):

        del self.data_employee[baris][kolom]

    def tambah_data(self, data_baru):

        nama, gaji, posisi, jabatan, domisili = data_baru
        self.data_employee.append([nama, gaji, posisi, jabatan, domisili])

# Membuat objek
it = Employee(lokasi_file='./karyawan_IT.xls')
marketing = Employee(lokasi_file='./karyawan_marketing.xls')
product = Employee(lokasi_file='./karyawan_product.xls')

'''

# Abstract Object
class RandomForest():
    pass


print()
# Exercise
# Buatlah satu class Mobil yang bisa digunakan untuk mencetak beragam tipe mobil
# Pastikan class tersebut memiliki setidaknya 3 attributes dan 3 methods

class Mobil:
    def __init__(self, warna):
        #pass
        self.tipe = "Avanza"
        self.warna = warna
        self.transmisi = "Manual"

    def rem(self, speed):
        print(f"Mobil {self.tipe} melakukan pengereman, pada kecepatan {speed}")

    def gas(self):
        print("Mobil menambah kecepatan")

    def parkir(self):
        print("Mobil sedang parkir")

Mobil = Mobil(warna = "Silver")
print(Mobil.warna)
Mobil.rem('80 km/jam')
Mobil.parkir()


''''''