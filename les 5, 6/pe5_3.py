def readFile(filename):
    kaartnummersRawFile = open(filename, 'r')
    kaartnummersFile = kaartnummersRawFile.read()
    kaartnummersRawFile.close()
    return kaartnummersFile

kaartnummers = readFile('kaartnummers.txt')
kaartnummers = kaartnummers.splitlines()

kaartRegels = len(kaartnummers)
hoogsteKaartnummer = list()

for regelnummer, nummer in kaartnummers:
    print(regelnummer)
    #nummerNaam = nummer.split(',')
    #if nummerNaam[0] > hoogsteKaartnummer[0]:
    #    hoogsteKaartnummer[0] = nummerNaam[0]
    #    hoogsteKaartnummer[1] = regelnummer + 1
#print(hoogsteKaartnummers)
