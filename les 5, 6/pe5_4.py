import os
import datetime

outputFile = None
keepAsking = True

if os.path.isfile('hardlopers.txt'):
    outputFile = open('hardlopers.txt', 'a')
else:
    outputFile = open('hardlopers.txt', 'w+')

while keepAsking:
    continueAsking = input('Klik op enter om een tijd op te nemen. Type STOP om te stoppen: ')

    if continueAsking == 'STOP':
        keepAsking = False
        outputFile.close()
        break

    nu = datetime.datetime.today()
    hardloper = str(input('Wat is de naam van de hardloper: '))

    outputFile.write(str(nu) + ', ' + hardloper + '\n')
