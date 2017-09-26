cijfersreeks = {
'piet': [6, 4, 7.1],
'henk': [8, 7, 9],
'dirk': [6, 9, 9.6]
}

for name in cijfersreeks:
    for cijfer in cijfersreeks[name]:
        if cijfer >= 8:
            print('{} heeft een {} gehaald!'.format(name, float(cijfer)))
