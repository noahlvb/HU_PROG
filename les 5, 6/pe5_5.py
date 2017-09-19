def gemiddelde(sentence):
    words = sentence.split()
    totalWords = len(words)
    totalChar = int()
    for word in words:
        totalChar += len(word)
    return totalChar / totalWords

inputSentence = str(input('Type een zin in: '))
print('De gemiddelde lengte van een woord in deze zin is ' + str(round(gemiddelde(inputSentence))))
