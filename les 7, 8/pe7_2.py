while True:
    userInput = str(input('Geef een string van vier letters: '))

    if len(userInput) == 4:
        print('Inlezen van correcte string: {} is geslaagd'.format(userInput))
        break

    print('{} heeft {} letters'.format(userInput, len(userInput)))
