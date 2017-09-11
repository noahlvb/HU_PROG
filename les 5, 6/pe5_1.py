def convert(celsius):
    return round(celsius * 1.8 + 32, 2)

def table(temps):
    print('F     C')
    for temp in temps:
        print(str(convert(temp)) + '  ' + str(temp))

table([6, 24, 31])
