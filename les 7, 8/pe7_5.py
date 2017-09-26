names = {}

while True:
    nameInput = str(input('Volgende naam: '))
    if nameInput == 'stop':
        print(names)
        for name in names:
            print('Er zijn {} studenten met de naam {}'.format(names[name], name))
        break
    elif nameInput in names:
        names[nameInput] += 1
    else:
        names[nameInput] = 1
