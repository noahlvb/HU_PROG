def readFile(filename):
    kaartnummersRawFile = open(filename, 'r')
    kaartnummersFile = kaartnummersRawFile.read()
    kaartnummersRawFile.close()
    return kaartnummersFile

kaartnummers = readFile('kaartnummers.txt')
kaartnummers = kaartnummers.splitlines()

for nummer in kaartnummers:
    nummerNaam = nummer.split(',')
    print(nummerNaam[1] + ' heeft kaartnummer: ' + nummerNaam[0])
