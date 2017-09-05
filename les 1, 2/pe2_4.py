#Hier worden de inputs van de gebruiker verzameld
uurloon = float(input('Wat is je uurloon?: '))
urenGewerkt = float(input('Hoeveel uren heb je gewerkt?: '))

#Loon wordt berekend
loon = uurloon * urenGewerkt

#Alle info wordt gepresenteerd aan de gebruiker
print('Wat verdien je per uur: ' + str(uurloon))
print('Hoeveel uur heb je gewerkt: ' + str(urenGewerkt))
print(str(urenGewerkt) + ' uur werken levert ' + str(loon) + ' Euro op')
