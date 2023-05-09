#------------------------------
# ENCAPSULATION
#------------------------------

class Mobil:
    def __init__(self, plat):

        self.__plat = plat
        self.__tipe = "Avanza"
        self.__bensin= 40 # liter            

    # getter
    def lihatMaksimumBensin(self):
        print(f"Maksimum bensin yaitu: {self.__bensin} liter")

    # setter
    def aturMaksimumBensin(self, bensin): 
        self.__bensin = bensin

avanza = Mobil(plat="B 7185 XC")
avanza.lihatMaksimumBensin()

avanza.__bensin = 100
avanza.lihatMaksimumBensin() # bensin tetap 40 tidak dapat di rubah kecuali dengan setter

avanza.aturMaksimumBensin(100) # setter - dirubah jadi 100
avanza.lihatMaksimumBensin() # getter

'''
Berguna juga untuk project team, jika source code di sharing dan yang punya tidak mau nilai variablenya
di ubah ubah
'''

print()
# Exercise
# Kembangkanlah class Mobil yang sudah dibuat sebelumnya agar memiliki fungsi setter & getter
# Pastikan fungsi tersebut memungkinkan kita untuk memodifikasi semua attributes yang dimiliki oleh class tersebut

class Mobil_lat:
    def __init__(self, warna):
        self.__tipe = "Avanza"
        self.__warna = warna
        self.__transmisi = "Manual"

    # getter
    def LiatTransmisi(self):
        print(f"Mobil {self.__tipe} ber-transmisi {self.__transmisi}")

    # setter
    def UbahTransmisi(self, transmisi):
        self.__transmisi = transmisi

Mobil_lat = Mobil_lat("Black")
Mobil_lat.LiatTransmisi()

Mobil_lat.__transmisi = "Triptonic"
Mobil_lat.LiatTransmisi()

Mobil_lat.UbahTransmisi("Matic")
Mobil_lat.LiatTransmisi()


    