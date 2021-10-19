# Program luas bangun
import math

print('/tMenu Program')
print('|\t1. Luas Segitiga\t|')
print('|\t2. Luas Lingkaran\t|')
print('|\t3. Luas Persegi \t|')
print('|\t4. Luas Persegi panjang\t|')

usr_input = int(input('Pilih\t: '))
if usr_input == 1:
    # Segitiga (1/2.a.t)
    obj1 = int(input('Masukkan alas\t: '))
    obj2 = int(input('Masukkan tinggi\t: '))
    hasil = 0.5 * obj1 * obj2
    print(hasil)
elif usr_input == 2:
    # lingkaran (3.14.r^2)
    obj1 = int(input("Masukkan ruas\t: "))
    hasil = math.pi * pow(obj1, 2)
    print(hasil)
elif usr_input == 3:
# persegi (s.s)
    obj1 = int(input('Masukkan sisi\t: '))
    hasil = pow(obj1, 2)
    print(hasil)
elif usr_input == 4:
# persegi panjang (p.l)
    obj1 = int(input('Masukkan panjang\t: '))
    obj2 = int(input('Masukkan lebar\t\t: '))
    hasil = obj1 * obj2
    print(hasil)
