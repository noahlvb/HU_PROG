def kwadratenSom(grondgetallen):
    kwadratenFinalSom = int()
    for getal in grondgetallen:
        if getal >= 0:
            kwadratenFinalSom += getal**2
    return kwadratenFinalSom

print(kwadratenSom([4, 5, 3, -81]))
