#livinus felix bassey
#Skilaverkefni_5_lambda_þappaðirlista_endurkvæmni
#10.11.2018

from random import *

#dæmi1
def randomTolur(tala, byrja,enda):
    listi = []
    for x in range(tala):
        randomtala=random.randint(byrja,enda)
        listi.append(randomtala)
        #print("\nListi með random númerum frá 15 til og með 400:")
    print(listi)
    return listi
randomTolur(20,5,201)

def finnaSamtolu(talaNot,listi):
    samTolu = []
    for x in listi:
        if talaNot == x[0]:
            return samTolu

def hverVann(samtalaNot, samtalaTol):
    for x in range(10):
        tal =randrange(1,10)
    pass

#dæmi2
def randomTolur(tala, byrja,enda):
    Listin = []
    filter(lambda x: x % 2 == 0, range(100, 600,20))
    njanListi = list(filter(lambda x: (x % 2 == 0), Listin))
    print(njanListi)

#Dæmi 3
#Notið listann úr dæmi 1 til að finna allar tölur sem ganga upp í 5 og eru stærri en 350.Notið filter() fallið
#listi = []
def myFunc(x):
    for x in listi:
        if x % 5 == 0:
            return true
        else:
            if x < 350:
                return False
            allTolar = filter(myFunc,listi)
            for x in allTolar:
                print(x)


#Dæmi 4
#Búið til lista með 200 tölum á bilinu 100 til 900. Notið map() fallið til að draga 2 frá hverri  tölu fyrir sig og setja í nýjan lista.
def Tolu200():
    tvehund = []
    for x in range(200):
            tala=random.randrange(100,900)
            tvehund.append(tala)
            return tvehund

#Dæmi 5
#Búið til lista með 200 tölum á bilinu 1 til 90. Notið list comprehension til setja allar tölur í þriðjaveldi sem eru undir 6 í annan lista.
def tol200():
    tveHun = []
    for x in range(200):
            tala=random.randrange(1,91)
            tveHun.append(tala)
            return tveHun

#Dæmi 6
#Búið til lista með 100 tölum á bilinu 1 til 20. Notið list comprehension til setja allar tölur sem enda á 0 í annan lista. Prentið út listann í röð efsta talan fyrst.
def tol100():
    hundra = []
    for x in range(100):
            rantala=random.randrange(1,20)
            hundra.append(rantala)
            return hundra


#Dæmi 7
#Notið afturkvæmt fall til að margfalda allar tölur saman í lista.
import math
listi = [2,4,6,8]

def afturkaemt(listi,x):
    if x ==-1:
        return 1
    else:
        tala = listi[x]
        return (tala*afturkvaemt(listi,x-1))


result = afturkvaemt(listi,len(listi)-1)
print(result)
print(math.pow(2,5))


#Dæmi 8
#Notið genarator fall (yield) til þess að skrifa eina tölu í einu út úr 100 talna random lista sem fallið tekur inn sem færubreytu(argument).


#Dæmi 9(hafið þennan lið í sér skjali)
#Til er mörg söfn í python. Eitt af þessum söfnum er tkinter.py. prófið að importa það og gerið eftirfarandi forrit:

randomTolur(20,5,201)
