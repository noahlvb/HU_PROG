studentenCijfers = [[6, 7, 5], [8, 7, 9], [4, 6, 3]]

def cijfersPerStudent(studentenCijfersList):
    result = str()
    for studentenCijfer in studentenCijfersList:
        totaalCijfers = int()
        aantalCijfers = int()
        for cijfer in studentenCijfer:
            totaalCijfers += cijfer
            aantalCijfers += 1

        studentGemiddelde = round(totaalCijfers/aantalCijfers, 1)
        result = result + 'gemiddelde is: ' + str(studentGemiddelde) + '\n'
    return result

def cijfersAlleStuenten(studentenCijfersList):
    totaalCijfersStudenten = int()
    aantalStudenten = int()
    for studentenCijfer in studentenCijfersList:
        totaalCijfers = int()
        aantalCijfers = int()
        for cijfer in studentenCijfer:
            totaalCijfers += cijfer
            aantalCijfers += 1

        studentGemiddelde = round(totaalCijfers/aantalCijfers, 1)
        totaalCijfersStudenten += studentGemiddelde
        aantalStudenten += 1

    schoolGemiddelde = round(totaalCijfersStudenten/aantalStudenten, 1)
    return 'Het gemiddelde van alle studenten is: ' + str(schoolGemiddelde)

print(cijfersPerStudent(studentenCijfers))
print(cijfersAlleStuenten(studentenCijfers))
