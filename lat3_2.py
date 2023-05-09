#------------------------------
# FILE HANDLING
#------------------------------

# Ini adalah file data.txt
# Pada file ini memuat beberapa informasi tentang data
# Data ini akan diproses menggunakan python

# Read
#data = open('./data.txt', mode='r') # ./ folder file txt berada sama dengan source code
#print(data.read())
#print(data.read(5))
'''
data = open('./data.txt', mode='r', encoding='utf-8') # recomended menggunakan encoding type
#print(data.read())
string = data.read()
print(string)
string = string.replace('adalah', 'merupakan')
print(string)
'''

# Append
'''
data = open('./data.txt', mode='a', encoding='utf-8') # append menambah data
data.write("\nYuk Belajar bahasa pemograman Python!")
data.write("\nAgar jago harus sering berlatih")

data.close() # agar memory tidak terpakai terlalu lama
'''


# Write
'''
data = open('./data.txt', mode='w', encoding='utf-8') # write menimpah / mengupdate data
data.write("\nYuk Belajar bahasa pemograman Python!")
data.write("\nAgar jago harus sering berlatih")

data.close() # agar memory tidak terpakai terlalu lama
'''



# Better practice (setelah di file di open pada akhir codingan file akan di close / jika terjadi error)
'''
try:
    f = open('./data.txt', mode='w', encoding='utf-8')
    #f.read()
    #f.write()
finally:
    f.close()
'''

# Best practice (file yang di open akan otomatif di tutup setelah codingan di jalankan / jika terjadi error)
'''
with open('./data.txt', mode='w', encoding='utf-8') as f:
    # diisi codingan 
    #f.read()
    #f.write()
    pass
'''

# Exercise
# Bacalah data yang ada di file data.txt
# Lalu tambahkan teks "Bahasa Pemrograman Python memiliki masa depan yang cerah"
# Pastikan tidak menghilangkan data yang sudah ada di file tersebut!
'''
with open('./data.txt', mode='a', encoding='utf-8') as f:
    f.write('\nBahasa Pemrograman Python memiliki masa depan yang cerah')
'''