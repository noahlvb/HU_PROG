inputLijst = eval(input('Geef hier je lijst op: '))
nieuweLijst = list()

for woord in inputLijst:
    if len(woord) <= 5:
        nieuweLijst.append(woord)

print(nieuweLijst)
