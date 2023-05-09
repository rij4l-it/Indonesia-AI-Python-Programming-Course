# Operator Aritmatika dan Operator Perbandingan

# Operator Aritmatika
a = 5
b = 3
print('')
print('a + b =', a + b)
print('a - b =', a - b)
print('a * b =', a * b)
print('a / b =', a / b)
print('a % b =', a % b) # modulus menghasilkan sisa bagi
print('a // b =', a // b) # pembagian dengan pembulatan ke bawah
print('a ** b =', a ** b) # Pangkat

a = 5
a += 3 # a di tambah 3
print(a)

a = 5
a *= 3 # a di kali 3
print(a)

s = "ini string "
s *= 5 # perkalian di mungkinkan untuk type data string
print(s)

b = True
b /= 2 # pembagian di mungkinkan di type data boolean (true = 1)
print(b)

print('')
print('')

# Operator Perbandingan

x = 10
y = 15
print('x > y:', x>y)
print('x < y:', x<y)
print('x == y:', x==y)
print('x != y:', x!=y)
print('x >= y:', x>=y)
print('x <= y:', x<=y)

print('')
print( x is y)
print( x is not y)


# Exercise
# Tentukan berapa hasil dari operasi +, -, *, /, %, // dan ** dari kedua variable di bawah!
# Lalu bandingkan hasil yang ada dengan nilai 30 dengan perbandingan >, <, ==, !=, >=, <= 

variable1 = 0.25
variable2 = 20

hasil = variable1 + variable2
print('')
print('variable1 + variable2 =', hasil)
print(f'30 > {hasil} :', 30 > hasil)
print(f'30 < {hasil} :', 30 < hasil)
print(f'30 == {hasil} :', 30 == hasil)
print(f'30 != {hasil} :', 30 != hasil)
print(f'30 >= {hasil} :', 30 >= hasil)
print(f'30 <= {hasil} :', 30 <= hasil)

hasil = variable1 - variable2
print('')
print('variable1 - variable2 =', hasil)
print(f'30 > {hasil} :', 30 > hasil)
print(f'30 < {hasil} :', 30 < hasil)
print(f'30 == {hasil} :', 30 == hasil)
print(f'30 != {hasil} :', 30 != hasil)
print(f'30 >= {hasil} :', 30 >= hasil)
print(f'30 <= {hasil} :', 30 <= hasil)