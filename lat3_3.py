#------------------------------
# ERROR HANDLING
#------------------------------
''' '''
# Syntax error

fruit_list = ["apple", "banana", "watermelon"]
# for fruit in fruit_list
# SyntaxError: invalid syntax (tanpa titik dua dan syntax setelah for)




# Logical error
#print(dir(locals()['__builtins__'])) # jenis2 logical error pada python

nilai = 10
pembagi = 0
# hasil = nilai/pembagi
# Errornya ZeroDivisionError: division by zero
# kemudian python melakukan break dan syntax selanjutnya tidak di jalankan  <---


try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except:
    print("Oops! Terjadi error.")

print('Instruksi selanjutnya')

# try berisi codingan / syntax pemograman
# except berisi jika ada logical error maka akan di jalankan perintah
# jika terjadi error syntax / perintah selanjutnya tetap di jalankan  <---

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except Exception as e:                               # jenis error di lempar ke variable e
    print("Oops! Terjadi ", e.__class__, ".")        # jenis error di tampilkan

try:
    nilai = 10
    pembagi = 0
    hasil = nilai/pembagi
except ZeroDivisionError:                               # Jika terjadi jenis error yang di ketahui ( seperti kondisi loop )
    print("Oops! Terjadi ZeroDivisionError.")           
except ValueError:
    print("Oops! Terjadi ValueError.")
except:
    print("Oops! Terjadi error yang tidak dikenali.")


try:
    nilai = 10
    pembagi = 2
    hasil = nilai/pembagi
except Exception as e:
    print("Oops! Terjadi ", e.__class__, ".")
else:
    print("Tidak ada error.")                   # bisa di gunakan kondisi seperti if


class ValueTooSmallError(Exception): # membuat jenis error sendiri
    pass

class ValueTooLargeError(Exception): # membuat jenis error sendiri
    pass

number = 10

while True:                                                                 # kondisi looping (terus mengulang sampai benar)
    try:                                                                    # tempat syntax / instruksi
        i_num = int(input("Masukan angka: "))

        if i_num < number:
            raise ValueTooSmallError                                        # memanggil / melempar type error ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break
    
    except ValueTooSmallError:                                              # jika terjadi error ValueTooSmallError maka.....
        print("Angka yang kamu tebak terlalu kecil, coba lagi!")
        print()
    except ValueTooLargeError:
        print("Angka yang kamu tebak terlalu besar, coba lagi!")
        print()

print("Betul! Kamu berhasil menebak dengan tepat.")                         # jika kondisi looping bernilai benar, maka....


# Exercise
# Instruksi cetak di bawah menyebabkan program terhenti karena mengalami IndexError
# Tangani error tersebut dengan teknik Error Handling yang sudah dipelajari
# Setelah itu, jalankan program dan pastikan tidak ada lagi pemberitahuan error pada program

#list = [1, 3, 5, 7, 9, 11, 13, 15]
#print(list[20])

try:
    list = [1, 3, 5, 7, 9, 11, 13, 15]
    print(list[20])    
    #pass
except Exception as e:
    #print("Oops! Terjadi ", e.__class__, ".")
    pass

print(list[3])