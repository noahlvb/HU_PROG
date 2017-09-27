def code(string):
    string = list(string)
    asciiString = list()
    newString = ''

    for char in string:
        asciiString.append(ord(char)+3)

    for char in asciiString:
        newString += chr(char)

    return newString

print(code('RutteAlkmaarDen Helder'))
