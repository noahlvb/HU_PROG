def wijzig(lijst):
    nieuweInhoud = ['d', 'e', 'f']
    for index, content in enumerate(nieuweInhoud):
        lijst[index] = content

lijst = ['a', 'b', 'c']
print(lijst)
wijzig(lijst)
print(lijst)
