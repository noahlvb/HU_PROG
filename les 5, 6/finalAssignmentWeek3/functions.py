from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

lockerFilePath = parser.get('global', 'lockers')
lockersAmount = int(parser.get('global', 'locker_amount'))

def freeLockerAmount():
    lockerFile = open(lockerFilePath, 'r')
    print('Er zijn ' + str(lockerFile.read().count('\n')) + ' lockers in gebruik van de ' + str(lockersAmount))
    lockerFile.close()

def newLocker(newPassword):
    lockerFile = open(lockerFilePath, 'r')
    lockerFileLines = lockerFile.read().splitlines()
    lockerFile.close()

    usedLockersByID = list()
    newLockerNumber = 1

    if len(lockerFileLines) >= lockersAmount:
        print('Er zijn geen kluizen meer beschikbaar')
        return False

    for line in lockerFileLines:
        usedLockersByID.append(int(line.split(';')[0]))
    usedLockersByID.sort()

    for ID in usedLockersByID:
        if ID == newLockerNumber:
            newLockerNumber += 1

    newLockerLine = str(newLockerNumber) + ';' + newPassword

    lockerFile = open(lockerFilePath, 'a')
    lockerFile.write(newLockerLine)
    lockerFile.close()

    print('Kluisje succesvol geregistreerd, je kluis nummer is: ' + str(newLockerNumber))
    return

def isLockerOwner(lockerNumber, password):
    lockerFile = open(lockerFilePath, 'r')
    lockerFileContent = lockerFile.read()
    lockerFileLines = lockerFileContent.splitlines()
    lockerFile.close()

    lockers = list()
    for lockerFileLine in lockerFileLines:
        lockers.append(lockerFileLine.split(';'))

    for locker in lockers:
        if int(locker[0]) == lockerNumber:
            if locker[1] == password:
                return [True, lockerFileLines]
            else:
                return [False]
    return [False]

def openLocker(lockerNumber, password):
    lockerOwnerAndLines = isLockerOwner(lockerNumber, password)
    if lockerOwnerAndLines[0] == True:
        print('De kluis is open')
        return
    else:
        print('Er is geen kluis gevonden met deze nummer wachtwoord combinatie')

def handinLocker(lockerNumber, password):
    lockerFileNewLines = list()
    lockerOwnerAndLines = isLockerOwner(lockerNumber, password)
    if lockerOwnerAndLines[0] == True:
        for line in lockerOwnerAndLines[1]:
            if not str(lockerNumber) in str(line.split(',')[0]):
                lockerFileNewLines.append(line + '\n')

        lockerFile = open(lockerFilePath, 'w')
        lockerFile.writelines(lockerFileNewLines)
        lockerFile.close()
        print('Je kluis is verwijderd')
    else:
        print('Er is geen kluis gevonden met deze nummer wachtwoord combinatie')
