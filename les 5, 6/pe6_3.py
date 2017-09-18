invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
getallen = invoer.split('-')

getallen = [ int(x) for x in getallen ]
getallen.sort()

print('Gesorteerde list van ints: ' + str(getallen))
print('Grootste getal: ' + str(max(getallen)) + ' en Kleinste getal: ' + str(min(getallen)))
print('Aantal getallen: ' + str(len(getallen)) + ' en Som van de getallen: ' + str(sum(getallen)))
print('Gemiddelde: ' + str(sum(getallen)/len(getallen)))
