totaalSum = []

while True:
    userInput = int(input('Geef een getal op: '))

    if userInput == 0:
        print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(totaalSum), sum(totaalSum)))
        break

    totaalSum.append(int(userInput))
