import csv

csvFilePath = 'scores.csv'

RawCsvFile = open(csvFilePath, 'r')
csvFile = csv.reader(RawCsvFile, delimiter=';')

csvFileRows = list()
highestScore = int()
highestScoreIndex = int()

for index, row in enumerate(csvFile):
    csvFileRows.append(row)
    if int(row[2]) > highestScore:
        highestScore = int(row[2])
        highestScoreIndex = index

print('De hoogste score is: {} op {} behaald door {}'.format(csvFileRows[highestScoreIndex][2], csvFileRows[highestScoreIndex][1], csvFileRows[highestScoreIndex][0]))
