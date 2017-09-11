def readFile(filename):
    kaartnummersRawFile = open(filename, 'r')
    kaartnummersFile = kaartnummersRawFile.read()
    kaartnummersRawFile.close()
    return kaartnummersFile

kaartnummers = readFile('kaartnummers.txt')
kaartnummers = kaartnummers.splitlines()

kaartRegels = len(kaartnummers)
hoogsteKaartnummer = list([0, 0])

for regelnummer, nummer in enumerate(kaartnummers):
    nummerNaam = nummer.split(',')
    if int(nummerNaam[0]) > int(hoogsteKaartnummer[0]):
        hoogsteKaartnummer[0] = nummerNaam[0]
        hoogsteKaartnummer[1] = regelnummer + 1

print('Deze file telt ' + str(kaartRegels) + ' regels')
print('Het grootste kaartnummer is: ' + str(hoogsteKaartnummer[0]) + ' en dat staat op regel ' + str(hoogsteKaartnummer[1]))
