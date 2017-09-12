def gemiddelde(sentence):
    words = sentence.split()
    totalWords = int()
    totalChar = int()
    for word in words:
        totalWords += 1
        totalChar += len(word)
    return totalChar / totalWords

inputSentence = str(input('Type een zin in: '))
print('De gemiddelde lengte van een woord in deze zin is ' + str(gemiddelde(inputSentence)))
