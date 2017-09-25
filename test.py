totaalSum = int()
keepRunning = True

while keepRunning:
    userInput = input('Geef een getal op: ')
    if userInput == 'quit':
        keepRunning = False
        break
        
    totaalSum += int(userInput)

print(totaalSum)
