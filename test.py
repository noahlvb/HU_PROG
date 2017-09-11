userName = input('Enter your name: ')
userAge = int(input('Enter your age: '))

if userAge >= 18:
    print(userName + ' you can vote!')
else:
    print(userName + " you can't vote")
