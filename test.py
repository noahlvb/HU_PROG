def hello(name):
    for char in name:
        if char.isalpha() == False:
            return 'Een naam mag alleen uit letter bestaan'
        return 'Welcome, ' + name + ', to the world of Python.'

while True:
    userName = str(input('Wat is je naam: '))
    print(hello(userName))
