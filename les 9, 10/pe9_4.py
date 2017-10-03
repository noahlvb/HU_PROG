import csv

csvFilePath = 'products.csv'
csvContent = [
['Artikelnummer', 'Artikelcode', 'Naam', 'Voorraad', 'Prijs'],
['121', 'ABC123', 'Highlight pen', '231', '0.56'],
['123', 'PQR678', 'Nietmachine', '587', '9.99'],
['128', 'ZYX163', 'Bureaulamp', '34', '19.95'],
['137', 'MLK709', 'Monitorstandaard', '66', '32.50'],
['271', 'TRS665', 'Ipad hoes', '155', '19.01']
]

# Write to file
csvFile = open(csvFilePath, 'w')
for line in csvContent:
    csvFile.write(';'.join(line) + '\n')
csvFile.close()

# Read file
RawReadCsvFile = open(csvFilePath, 'r')
readerReadCsvFile = csv.reader(RawReadCsvFile, delimiter=';')
readCsvFile = list()
for index, line in enumerate(readerReadCsvFile):
    if not index == 0:
        readCsvFile.append(line)

RawReadCsvFile.close()

# Most expensive
costOfMostExpensive = int()
costOfMostExpensiveIndex = int()
for index, line in enumerate(readCsvFile):
    if float(line[4]) > costOfMostExpensive:
        costOfMostExpensive = float(line[4])
        costOfMostExpensiveIndex = index
print('Het duurste artikel is {} en die kost {} Euro'.format(readCsvFile[costOfMostExpensiveIndex][2], costOfMostExpensive))

# Minste Voorraad
leastInventory = int(99999)
leastInventoryIndex = int()
for index, line in enumerate(readCsvFile):
    if int(line[3]) < leastInventory:
        leastInventory = int(line[3])
        leastInventoryIndex = index
print('Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(leastInventory, readCsvFile[leastInventoryIndex][0]))

# totaal items
totaalItems = int()
for line in readCsvFile:
    totaalItems += int(line[3])
print('In totaal hebben wij {} producten in ons magazijn liggen'.format(totaalItems))
