stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', "’s-Hertogenbosch", 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']

def askStation(beginStation, beginStationName):
    beginEindeString = 'beginstation' if beginStation else 'eindstation'

    while True:
        userInput = str(input('Wat is je {}: '.format(beginEindeString))).lower().capitalize()

        if userInput in stations:
            if beginStation == False and stations.index(userInput) < stations.index(beginStationName):
                print('Dit traject gaat maar in een richting! Kies een ander station')
                continue

            return userInput

        print('Geef een station op dat zich op dit traject bevind!')

def omroep(beginStation, eindStation):
    beginStationIndex = stations.index(beginStation)
    eindStationIndex = stations.index(eindStation)
    stationIndexDiff = eindStationIndex - beginStationIndex
    prijs = stationIndexDiff * 2

    print('\n===================================================')
    print('Het beginstation {} is het {}e station in het traject.'.format(beginStation, beginStationIndex + 1))
    print('Het eindstation {} is het {}e station in het traject.'.format(eindStation, eindStationIndex + 1))
    print('De afstand bedraagt {} station(s).'.format(stationIndexDiff))
    print('De prijs van het kaartje is {} euro.'.format(prijs))
    print('\nJij stapt in de trein in: {}'.format(beginStation))
    print(' - ' + ', '.join(stations[beginStationIndex+1:eindStationIndex]))
    print('Jij stapt uit in: {}'.format(eindStation))

beginStation = askStation(True, None)
eindStation = askStation(False, beginStation)
omroep(beginStation, eindStation)
