#------------------------------
# LIST, TUPLE & DICTIONARY
#------------------------------
print('')
# List

list1 = ['apple', 'watermelon', 'banana']
list2 = [2, 1, 2 , 7, 4, 10]
list3 = [True, False, True, False]
list4 = ['abc', 100, True, 40, False]

list5 = [list1, list2, list3, list4]
print(list5)

print(list1 + list2)

list2.sort() # sort ascending
print(list2)
list1.sort()
print(list1) # bisa sort huruf juga

list2.reverse()
print(list2) # sort descending

list6 = list2.copy()
print(list6)

print(list2.count(2)) # menghitung ada brapa angka 2 di dlm list 

fruit_list = ['apple', 'watermelon', 'banana', 'manggo', 'orange']
print(fruit_list[0]) # mangakses isi list - index dari 0
print(fruit_list[1:4]) # mangakses isi list - index dari 1 - 3
print(fruit_list[-2]) # mengakses isi list 2 terakhir
print(fruit_list[-3:4]) # mengakses isi index 3 terakhir sd index 4
print(fruit_list[2:]) # mengakses isi list index 2 sd habis
print(fruit_list[-2:]) # mengakses isi list index 2 terakhir sd habis

fruit_list[2] = 'avocado' # mengganti isi list index ke 2 (banana jadi avocado)
print(fruit_list)

# membership test (test apakah ada data yg di cari di dalam list)
print('apple' in fruit_list) # jawabannya booelan
print('banana' in fruit_list)
print('banana' not in fruit_list)

fruit_list2 = ['apple', 'orange']
fruit_list2.append('watermelon') # tambah data pada index terakhir
print(fruit_list2)

fruit_list2.insert(1, "banana") # menambah data banana pada index 1
print(fruit_list2)

fruit_list3 = ['durian', 'jambu']
fruit_list2.extend(fruit_list3) # menambah isi data fruit_list2 dengan data dari fruit_list3
print(fruit_list2)

fruit_list4 = ['apple', 'watermelon', 'banana', 'manggo', 'orange']
fruit_list4.remove('apple') # hapus isi data apple
print(fruit_list4)

fruit_list5 = ['apple', 'watermelon', 'banana', 'manggo', 'orange']
fruit_list5.pop(1) # hapus data pada index 1 (watermelon)
print(fruit_list5)

for fruit in fruit_list5:
    print("Nama buah pada fruit list5:", fruit)

fruit_list6 = ['apple', 'watermelon', 'banana', 'manggo', 'orange']
del fruit_list6[2] # hapus data pada index 2 (banana)
print(fruit_list6)
fruit_list6.clear() # hapus seluruh data
print(fruit_list6) 
#del fruit_list6 # hapus seluruh data beserta variable fruit_list6
#print(fruit_list6)


'''....'''



print('')
# Tuple

tuple1 = ("apple", "banana",  "watermelon")
tuple2 = (1, 3, 7, 9, 10)
tuple3 = (True, False, False)
tuple4 = ("abc", 10, True, 40, "male")

fruit_tuple = ("apple", "banana", "watermelon", "orange", "mango")
fruit_tuple[1] # banana
fruit_tuple[1:4] # banana, watermelon, orange
fruit_tuple[-2:] # orange, mango

print(fruit_tuple)

fruit_tuple = ("apple", "banana", "watermelon", "orange", "mango")
# fruit_tuple[1] = "banana" # constanta / imunable tidak bisa di edit

fruit_tuple = ("apple", "banana", "watermelon", "orange", "mango")
# del fruit_tuple[1] # constanta / immutable tidak bisa di hapus

for fruit in fruit_tuple:
    print("Nama buah pada fruit tuple:", fruit)


'''....'''


print('')
# Dictionary

fruit_dict = {'nama' : 'Pisang',
             'jenis' : 'Ambon',
             'kode' : 891,
             'harga' : 20000
             }

print(fruit_dict)
print(fruit_dict['jenis'])

fruit_dict['jenis'] = 'Kepok' # rubah field / key dari jenis
print(fruit_dict)

for key, value in fruit_dict.items():
    print(key, value)

print('------------------')

for key in fruit_dict.keys():
    print(key, fruit_dict[key])


print('------------------')

fruit_dict2 = [{'nama' : 'Pisang',
                'jenis' : 'Ambon',
                'kode' : 891,
                'harga' : 20000
              },
              {'nama' : 'Pisang2',
                'jenis' : 'Ambon',
                'kode' : 891,
                'harga' : 20000
              }]  

print(fruit_dict2)
print(fruit_dict2[1])



print('')
# BONUS: Set (himpunan)
A = {1,2,3,4,5}
B = {4,5,6,7,8}

# Union (menggabungkan)
print(A | B) # nilai yang sama tidak di tampilkan lagi

# Intersection (Iriisan)
print( A & B)

# Difference (mengambil nilai di luar irisan dari salah satu list data)
print(A - B)
print(B - A)

# Symmetric Difference (mengambil nilai di luar irisan dari kedua list data)
print(A ^ B)


print('')
print('Exercise')
# Exercise
# Buatlah 2 buah dictionary yang memuat informasi 10 murid dan informasi 10 karyawan
# Lalu cetak data murid dan karyawan yang berada di-index 2 dan 9
# Setelah itu cetak semua data yang ada di dictionary tersebut dengan for loop

dict_murid = [{'nama' : 'murid_1',
              'nip' : 10000              
              },
             {'nama' : 'murid_2',
              'nip' : 20000              
              },
             {'nama' : 'murid_3',
              'nip' : 30000              
              },
             {'nama' : 'murid_4',
              'nip' : 40000              
              },
             {'nama' : 'murid_5',
              'nip' : 50000              
              },
             {'nama' : 'murid_6',
              'nip' : 60000              
              },
             {'nama' : 'murid_7',
              'nip' : 70000              
              },
             {'nama' : 'murid_8',
              'nip' : 80000              
              },
             {'nama' : 'murid_9',
              'nip' : 90000              
              },
             {'nama' : 'murid_10',
              'nip' : 10001              
              }]
dict_karyawan = [{'nama' : 'karyawan_1',
              'nip' : 10000              
              },
             {'nama' : 'karyawan_2',
              'nip' : 20000              
              },
             {'nama' : 'karyawan_3',
              'nip' : 30000              
              },
             {'nama' : 'karyawan_4',
              'nip' : 40000              
              },
             {'nama' : 'karyawan_5',
              'nip' : 50000              
              },
             {'nama' : 'karyawan_6',
              'nip' : 60000              
              },
             {'nama' : 'karyawan_7',
              'nip' : 70000              
              },
             {'nama' : 'karyawan_8',
              'nip' : 80000              
              },
             {'nama' : 'karyawan_9',
              'nip' : 90000              
              },
             {'nama' : 'karyawan_10',
              'nip' : 10001              
              }]

#print(dict_murid)
print(dict_murid[2:10])

for murid in dict_murid:
    #print("Nama buah pada fruit list5:", fruit)
    for key, value in murid.items():
        print(key, value)
    #pass

print('------------------')

'''
for murid in dict_murid[2:5]:    
    for key, value in murid.items():
        print(key, value)


'''
print(dict_karyawan[2:10])

for karyawan in dict_karyawan:    
    for key, value in karyawan.items():
        print(key, value)
    #pass


