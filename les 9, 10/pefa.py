import xmltodict

with open('stations.xml') as stationsXML:
    stationsDict = xmltodict.parse(stationsXML.read())
    stations = stationsDict['Stations']['Station']

    print('Dit zijn de codes en types van de {} stations: '.format(len(stations)))
    for station in stations:
        print('{} - {}'.format(station['Code'], station['Type']))

    print('\ndit zijn alle stations met een of meer synoniemen:')
    for station in stations:
        if station['Synoniemen']:
            print('{} - {}'.format(station['Code'], ', '.join(station['Synoniemen']['Synoniem'])))

    print('\nDit is de lange naam van elk station')
    for station in stations:
        print('{} - {}'.format(station['Code'], station['Namen']['Lang']))
