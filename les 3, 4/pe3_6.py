s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkerS = str( )

for letter in s:
    if(letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        klinkerS = klinkerS + letter
print(klinkerS)
