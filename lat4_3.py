#------------------------------
# INHERITANCE
#------------------------------

# Parent class
class Animal:           # parent bisa juga sebagai child dari parent yang lain

    def __init__(self):
        self.tipe = "Mamalia"
        self.kecepatan = "Lambat"

    def grow(self):
        print("Mamalia ini bertumbuh...")


# Child class
class Cat(Animal):
    
    def __init__(self, nama, tipe):
        
        super().__init__()          # mengakses ini parent (animal)

        self.nama = nama
        self.tipe = tipe

    def run(self):
        print(f"Kucing {self.nama} ini berlari.....")

class Dog(Animal):      # Bisa banyak child class
    pass

kinako = Cat(nama="Kinako", tipe="Anggora")
minto = Cat(nama="Minto", tipe="Persia")

print(kinako.kecepatan)     # mengakses variable di class parent
print(kinako.tipe)          # mengakses variable di class parent dgn nama variable yg sama dengan child yang sudah di modified (mamalia = Anggora)

kinako.run()
minto.run()

kinako.grow() # mengakses fungsi di class parent
minto.grow()


print()
# Exercise
# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki parent class bernama Kendaraan
# Pastikan parent class tersebut memiliki setidaknya 2 attributes dan 2 methods yang akan diturunkan ke child class
# Jangan lupa menggunakan super() pada child class

# Parent class
class Kendaraan:

    def __init__(self):
        self.merk = "Toyota"
        self.tipe = "Minibus"

    def seat(self):
        print("Mobil ini berkapasita penumpang 7 orang")

# Child class
class Mobil(Kendaraan):
    def __init__(self, warna):
        
        super().__init__()

        self.tipe = "Avanza"
        self.warna = warna
        self.transmisi = "Manual"

    def rem(self, speed):
        print(f"Mobil {self.tipe} melakukan pengereman, pada kecepatan {speed}")

    def gas(self):
        print("Mobil menambah kecepatan")

Mobil = Mobil(warna = "Silver")
print(Mobil.warna)
Mobil.rem('80 km/jam')

print(Mobil.merk)
Mobil.seat()

