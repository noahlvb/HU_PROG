# Cijfers worden ingevoerd
cijferICOR = 6.8
cijferPROG = 7.2
cijferCSN = 6.3

# Cijfers worden opgeteld
cijfersTotaal = cijferICOR + cijferPROG + cijferCSN

#Verschillende data wordt berekend
gemiddelde = (cijfersTotaal)/3
beloning = cijfersTotaal * 30
overzicht = 'Mijn cijfers (gemiddeld een ' + str(gemiddelde) + ') leveren een beloning van ' + str(beloning) + 'Euro op!'

#overzicht wordt uitgeprint
print(overzicht)
