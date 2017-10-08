import xmltodict

xmlFile = open('products.xml', 'r')
xmlDict = xmltodict.parse(xmlFile.read())
xmlFile.close()

for artikel in xmlDict['artikelen']['artikel']:
    print('nummer: {}, code: {}, naam: {}, voorraad: {}, prijs: {}'.format(artikel['@nummer'], artikel['code'], artikel['naam'], artikel['voorraad'], artikel['prijs']))
