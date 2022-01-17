from creator import *
from time import sleep

while True:
    type_password = input("""Choose some password type:
    1 - Numeric Password
    2 - Letter Password
    3 - Alphanumeric Password
    4 - Special Characters Password
    5 - Master Password
    (just insert numbers): """).strip()
    characters_quantity = input('Insert the quantity of characters to the password: ').strip()
    repeatition = input('Insert 1 to allow repeated characters or 2 to not allow: ').strip()
    sleep(1)
    try:
        type_password = int(type_password)
        characters_quantity = int(characters_quantity)
        repeatition = int(repeatition)
    except:
        print('Error, you need insert correct values, according above statement.\nPlease try again.')
        sleep(1)
    else:
        if repeatition in (1, 2):
            if repeatition == 1:
                repeatition = True
            else:
                repeatition = False
            if type_password == 1:
                password = CreatePassword(length=characters_quantity, repeat=repeatition)
                password = password.numeric_password()
                print('Password created: ', *password, sep='')
                sleep(1)
            elif int(type_password) == 2:
                password = CreatePassword(length=characters_quantity, repeat=repeatition)
                password = password.letter_password()
                print('Password created: ', *password, sep='')
                sleep(1)
            elif int(type_password) == 3:
                password = CreatePassword(length=characters_quantity, repeat=repeatition)
                password = password.letter_num_password()
                print('Password created: ', *password, sep='')
                sleep(1)
            elif int(type_password) == 4:
                password = CreatePassword(length=characters_quantity, repeat=repeatition)
                password = password.special_chrt_password()
                print('Password created: ', *password, sep='')
                sleep(1)
            elif int(type_password) == 5:
                password = CreatePassword(length=characters_quantity, repeat=repeatition)
                password = password.master_password()
                print('Password created: ', *password, sep='')
                sleep(1)
            else:
                print('Please, insert correct values, according above statement.')
        else:
            print('You need insert just 1 or 2, to allow or not repetition')
            sleep(1)
    finally:
        stop = False
        while True:
            ask = input('Do you want continue?\nPress 1 to YES or 2 to NOT\n(Just use numbers): ').strip()
            sleep(1)
            try:
                ask = int(ask)
            except:
                print('Please, insert correct values, according above statement.')
                sleep(1)
            else:
                if ask == 2:
                    print('Thank you! Bye bye!')
                    sleep(1)
                    stop = True
                    break
                elif ask == 1:
                    sleep(1)
                    break
                else:
                    sleep(1)
                    print('Please, insert correct values, according above statement.\nPress 1 or 2')
                    sleep(1)
        if stop:
            sleep(1)
            break
