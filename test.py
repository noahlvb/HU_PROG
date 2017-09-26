import random

def game(rangex, rangey):
    posx = random.randrange(1, rangex + 1)
    posy = random.randrange(1, rangey + 1)

    while True:
        userGuess = str(input('Enter next posistion (format: x y): '))
        userGuess = userGuess.split(' ')
        userGuess = [ int(x) for x in userGuess ]

        if userGuess[0] == posx and userGuess[1] == posy:
            print('You found the bomb!')
            break

        print('No bomb at position {} {}'.format(userGuess[0], userGuess[1]))

game(2, 3)
