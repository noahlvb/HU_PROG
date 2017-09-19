import functions

keepRunning = True

while keepRunning:
    print('\n-------------------------------------')
    print('1: Wil weten hoeveel kluizen nog vrij zijn')
    print('2: Ik wil een nieuwe kluis')
    print('3: Ik wil even iets uit mijn kluis halen')
    print('4: Ik geef mijn kluis terug')
    print('5: Stop het programma')

    userChoice = int(input('\nMaak je keuze(geef op als getal): '))

    if userChoice == 1:
        functions.freeLockerAmount()
    elif userChoice == 2:
        newPassword = input('Geef een wachtwoord op voor je kluis: ')
        functions.newLocker(newPassword)
    elif userChoice == 3:
        lockerNumber = int(input('Geef je kluis nummer op: '))
        password = input('Geef het wachtwoord op voor je kluis: ')
        functions.openLocker(lockerNumber, password)
    elif userChoice == 4:
        lockerNumber = int(input('Geef je kluis nummer op: '))
        password = input('Geef het wachtwoord op voor je kluis: ')
        functions.handinLocker(lockerNumber, password)
    elif userChoice == 5:
        keepRunning = False
    else:
        print('Maak een correcte keze')
