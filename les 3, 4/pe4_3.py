def langGenoeg(length):
    if length >= 120:
        return 'Je bent lang genoeg!'
    else:
        return 'Sorry, je bent te kort.'

userLength = int(input('Geef je lengte op (in centimeters): '))
print(langGenoeg(userLength))
