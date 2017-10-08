import datetime
import csv

csvFilePath = 'inloggers.csv'

RawCsvFile = open(csvFilePath, 'r')
csvFile = csv.reader(RawCsvFile, delimiter=';')
csvFileRows = list()

for row in csvFile:
    csvFileRows.append(row)

while True:
    nu = datetime.datetime.today().strftime('%A %d %B at %H:%M')

    naam = str(input("Wat is je achternaam? "))
    if naam == 'stop':
        csvFile = open(csvFilePath, 'w')
        for row in csvFileRows:
            csvFile.write(';'.join(row))
        csvFile.close()
        break

    voorl = str(input("Wat zijn je voorletters? "))
    gbDatum = str(input("Wat is je geboortedatum? "))
    email = str(input("Wat is je e-mail adres? "))

    csvFileRows.append([nu, naam, voorl, gbDatum, email, '\n'])
