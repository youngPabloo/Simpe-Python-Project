# simple menu program

# menu
print("\tMenu")
print('1. Nasi Jinggo\tRp.5000')
print('2. Esteh\tRp.3000')
print('3. Teh hangat\tRp.2000')
print('')
# input
usr_input = int(raw_input("Masukkan menu anda\t: "))

# execute program // kondisional
if usr_input == 1:
    usr_cash = int(raw_input('masukkan uang anda\t: '))
    print('Terimakasih!\nSisa uang anda : ' + str(usr_cash - 5000))
elif usr_input == 2:
    usr_cash = raw_input('masukkan uang anda\t: ')
    print('Terimakasih!\nSisa uang anda : ' + str(usr_cash - 3000))

elif usr_input == 3:
    usr_cash = raw_input('masukkan uang anda\t: ')
    print('Terimakasih!\nSisa uang anda : ' + str(usr_cash - 2000))

