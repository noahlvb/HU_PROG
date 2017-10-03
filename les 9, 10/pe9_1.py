paymentAmount = 4356

try:
    amountOfPeople = int(input('Met hoeveel mensen ben je: '))
    if amountOfPeople < 0:
        print('Je kan niet met - mensen zijn.')
    else:
        print(paymentAmount/amountOfPeople)
except ZeroDivisionError:
    print('Je kan niet delen door nol!')
except ValueError:
    print('Je moet een getal opgeven!')
except:
    print('Er is iets mis gegaan!')
