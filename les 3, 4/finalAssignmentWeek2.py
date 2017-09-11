def standaardPrijs(afstandKM):
    standaardTarief = float()
    if afstandKM < 0:
        afstandKM = 0
    if afstandKM > 50:
        standaardTarief = (15 + (afstandKM * 0.60))
    else:
        standaardTarief = afstandKM * 0.80
    return standaardTarief

def ritPrijs(leeftijd, weekendrit, afstandKM):
    standaardTarief = float(standaardPrijs(afstandKM))

    if leeftijd <= 12 or leeftijd >= 65:
        if weekendrit.lower() == 'ja':
            return standaardTarief * 0.65
        else:
            return standaardTarief * 0.70
    else:
        if weekendrit.lower() == 'ja':
            return standaardTarief * 0.60

    return standaardTarief

userAge = int(input('Wat is je leeftijd: '))
traveledDistance = float(input('Hoeveel kilometers heb je afgelegd: '))
isWeekend = input('Is het weekend (Ja of Nee): ')

finalRitprijs = ritPrijs(userAge, isWeekend, traveledDistance)

print('Je ritprijs bedraagd: ' + str(finalRitprijs) + ' Euro')
