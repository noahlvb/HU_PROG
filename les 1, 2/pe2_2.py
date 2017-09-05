cijferICOR = 6.8
cijferPROG = 7.2
cijferCSN = 6.3

cijfersTotaal = cijferICOR + cijferPROG + cijferCSN

gemiddelde = (cijfersTotaal)/3
beloning = cijfersTotaal * 30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van ' + str(beloning) + 'Euro op!'

print(overzicht)
