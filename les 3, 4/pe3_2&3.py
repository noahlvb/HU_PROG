leeftijd = int(input('Wat is je leeftijd?: '))
paspoort = input('Heb je een paspoort?: ')

# Check of Ja of Nee is geantwoord
if(paspoort.lower() == 'ja' AND leeftijd >= 18):
    print('Gefeliciteerd je mag stemmen')
elif(paspoort.lower() == 'nee' OR leeftijd < 18):
    print('Je bent niet stemgerechtig')
else:
    print('Geef antwoord in de vorm: ja of nee')
