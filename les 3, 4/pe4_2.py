def som(getalenList):
    totaalSom = int()
    for getal in getalenList:
        totaalSom += int(getal)
    return int(totaalSom)

print(som([5, 10.5, 20]))
