#------------------------------
# LOOP
#------------------------------

# While
count = 0
while (count < 9):
    print('nilai count : ', count)
    count = count + 1

print('Keluar while loop') # kalo looping nga berhenti press ctrl+C

print('')

# For Loop
list_angka = [1,2,3,4,5]

for x in list_angka:
    print(x)

print('Keluar for loop')

print('')

print(range(10))

print(list(range(8))) # cara buat data list

list_range = list(range(2, 20))
print(list_range)

list_range = list(range(2, 20, 3)) # list lompat 3 angka
print(list_range)

for x in list(range(2,10,2)):
    print(x)

print('')

# Nested loop
i = 90

while (i < 100):
   j = 2
   print((i/j))
   while (j <= (i/j)):
      print("Loop dalam loop!")
      j = j + 1
      i = i + 1

print("Keluar Nested loop")
print('')

# Break & Continue
for val in "string":
   if val == "i":
      break # stop looop in i string

   print(val)

print("Loop telah berakhir.")

for val in "string":
   if val == "i":
      continue  # skip i string

   print(val)

print("Loop telah berakhir.")
print('')

# BONUS: FOR ELSE
daftar_murid = ['Angga', 'Mardadi', 'Rowi']
nama_murid = 'Farhan'

for nama in daftar_murid:
    if nama == nama_murid:
        print(f'Ditemukan nama murid : {nama}')
        break
else:
    print("Nama murid tidak ditemukan.")

# BONUS: Pass
for nama in daftar_murid:
    pass

print('')
print('Exercise')
# Exercise
# Buatlah operasi loop yang akan mencetak angka GENAP dari 1-120
# Lalu gunakan statement continue agar operasi tidak mencetak angka 12, 56 dan 78
# Dan juga gunakan statement break agar operasi berhenti hanya sampai di angka 100

for x in list(range(2,122,2)):
    if x == 12 or x == 56 or x == 78:
      continue
    if x == 102:
       break        
    print(x)

