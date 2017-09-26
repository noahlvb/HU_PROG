def readTickerFile(filePath):
    RawFile = open(filePath, 'r')
    fileLines = RawFile.read().splitlines()
    RawFile.close()

    tickerSymbols = {}

    for line in fileLines:
        tickerSymbols[line.split(':')[0].lower()] = line.split(':')[1]

    return tickerSymbols

def findKey(input_dict, value):
    return next((k for k, v in input_dict.items() if v == value), None)

tickerSymbols = readTickerFile('tickerSymbols.txt')

companyName = str(input('Enter Company name: '))
print('Ticker symbol {}'.format(tickerSymbols[companyName.lower()]))

CompanyTicker = str(input('Enter Company ticker: '))
print('Company Name: {}'.format(findKey(tickerSymbols, CompanyTicker)))
