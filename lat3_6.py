#------------------------------
# REGEX
#------------------------------
# Materi lengkap regex pada slide hal 61 file module_3.ppt

import re

teks = "regex"
x = re.match("^r...x$", teks)       # match (^ menandakan permulaan text) ($ akhir text) (r = awal huruf) (s = akhir huruf) (... = tiga huruf bebas)
print(x)


teks = "saya senang belajar regex"  
x= re.split("\s", teks)             # split ( \s = string yang memuat spasi) ( \s = string yang memuat spasi)
print(x)


teks = """
        Ada 3 tipe loop atau perulangan di bahasa pemrograman Python yaitu while loop, 
        for loop dan nested loop 2022
       """
x = re.sub("\d+","", teks)             # sub = subtituion (\d = string memuat digit) (+ = satu atau lebih) (menghapus semua string angka)
print(x)


teks = "Hujan deras di kawasan depok"
result = re.search("^Hujan.*depok$", teks) # search (. = karakter, * = 0 atau semua)
if result:
    print("Yes we have found")
else:
    print("Not fount")


teks = "23 oct 2019 23 oct,2019 23 october,2019 oct 26,2020"
x = re.findall("\d{2} [a-z]{3} \d{4}", teks) # findall (\d{2} = mencari angka berdigit 2) (mencari huruf dr a -z berdigit 4)
print(x)


teks = "Harga 1 mobil antik tersebut yaitu $1000"
x= re.sub("\$\d+", "_", teks) # mengganti angka setelah karakter $ menjadi _
print(x)


teks = "Akan dialihkan ke http://medium.com"
x = re.sub("http[s]?\://\S+", "_", teks)    # (? = karakter s bisa ada bisa nga)
print(x)


teks = "Luar biasa! #rijal Banyak anak-anak muda traveling tahun ini, begini tanggapan lesti #travel #_lesti #viral #gadget"
x = re.findall("#[_]*[a-z]+", teks)
print(x)


# Exercise
# Coba tangkap informasi domisili (Tokyo) dan informasi nomor (021 7581 6521) pada 2 teks berikut
# Gunakan modul regex (re)

teks1 = "Saya yang berdomisili di Tokyo bisa dihubungi di nomor berikut 021 7581 6521"
teks2 = "Nomor ini tidak bisa dihubungi 021 1121 6551, karena sudah di luar area Tokyo"

x = re.findall("Tokyo", teks1)
print(x)

x = re.findall("\d{3} \d{4} \d{4}", teks1)
print(x)