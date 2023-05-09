#------------------------------
# POLIMORPHISM
#------------------------------

# Class
class Cat:
    def __init__(self):
        self.nama = "Meong"
        self.tipe = "Anggora"

    def forward(self):
        print("Kucing berlari...")

# Class
class Bird:
    def __init__(self):
        self.nama = "Erago"
        self.tipe = "Elang"

    def forward(self):
        print("Burung terbang...")

def melaju(objek):
    objek.forward()     # memanggil kelas yang mempunyai nama method yang sama

meong = Cat(); erago = Bird()

melaju(meong)
melaju(erago)

print()
# Exercise
# Setelah class mobil, buatlah satu class baru bernama motor
# Terapkan konsep Polimorphism yang sudah dipelajari dengan membuat satu fungsi umum bernama menampung()

class Mobil:
    def __init__(self):
        pass

    def InjekGas(self):
        print("Mobil di injak gasnya berjalan !....")

    def Silakan(self):
        print("Ini di ambil dari class mobil")

class Motor:
    def __init__(self):
        pass
    
    def InjekGas(self):
        print("Motor di putar gasnya berjalan !....")

    def ambil(self):
        Mobil().Silakan()

def menampung(object):
    object.InjekGas()

avanza = Mobil(); vario = Motor()
menampung(avanza)
menampung(vario)

vario.ambil()


