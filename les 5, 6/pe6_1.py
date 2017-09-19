winter = (12, 1, 2)
lente = (3, 4, 5)
zomer = (6, 7, 8)
herfst = (9, 10, 11)

def seizoen(maand):
    if maand in winter:
        return 'winter'
    elif maand in lente:
        return 'lente'
    elif maand in zomer:
        return 'zomer'
    elif maand in herfst:
        return 'herfst'
    else:
        return 'You are wrong sir, WRONG!'

print(seizoen(int(input('Geef het nummer van de maand op: '))))
