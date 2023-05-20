import random
def randomTolur(tala, byrja,enda):
    listi = []
    for x in range(tala):
        randomtala=random.randint(byrja,enda)
        listi.append(randomtala)
        #print("\nListi með random númerum frá 15 til og með 400:")

    return listi


def finnaSamtolu(talaNot,listi):
    summa=0
    for x in listi:
        if x% talaNot ==0:
            summa = summa +x
    return summa

listi1 = randomTolur(20,5,201)

mysum = finnaSamtolu(2,listi1)
print(mysum)
