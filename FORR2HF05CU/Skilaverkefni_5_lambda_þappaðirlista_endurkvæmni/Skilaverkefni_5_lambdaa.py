#livinus felix bassey
#Skilaverkefni_5_lambda_þappaðirlista_endurkvæmni
#10.11.2018

from random import *

#dæmi1
#Skrifið forrit sem býr til lista með 20 randomtölum á ákveðnu bili.
def randomTolur(tala, byrja,enda):
    listi = []
    for x in range(tala):
        randomtala=randrange(byrja, enda)
        listi.append(randomtala)
        #print("\nListi með random númerum frá 15 til og með 400:")
    return listi

#finnur síðan samtölu allra talna sem ganga upp í ákveðna tölu valda af notanda.
def finnaSamtolu(talaNot,listi):
    samTolu = []

    for x in listi:
        if talaNot == x[0]:
            return samTolu

#Notandi velur sér tölu (á bilinu 1-10)sem hann vill fá samtölu fyrir
#og fyrir tölvuna er valin random tala á sama bili
def hverVann(samtalaNot, samtalaTol):#
    for x in range(10):
        tal = randrange(1,10)
    pass

#dæmi2
def randomTolu(tala, byrja,enda):
    Listin = []
    filter(lambda x: x % 2 == 0, range(100, 600,20))
    njanListi = list(filter(lambda x: (x % 2 == 0), Listin))
    print(njanListi)


val = 1 # breyta sem nýtist í valmynd, sett sem 1 til að komast inn í while
# bý til valmynd
while val != 0:
    print('-----------')
    print('Valmynd:')
    print('1. forrit sem býr til lista með 20 randomtölum á ákveðnu bili')
    print('2. Notið filter() og lambda til að setja allar jafnar tölur ')
    print('3.listann úr dæmi 1 til að finna allar tölur')
    print('4. lista með 200 tölum á bilinu 100 til 900 ')
    print('5.lista með 200 tölum á bilinu 1 til 90 ')
    print('6.lista með 100 tölum á bilinu 1 til 20 ')
    print('7. afturkvæmt fall ')
    print('8.genarator fall (yield) ')
    print('0. Til að hætta') # Þegar notandi velur 0 er hætt í valmynd/forriti
    val = int(input('Veldu númer úr valmynd'))

    # Nú getum við notað if, elif, else til að fara í valinn lið
    if(val == 1):
        pass

    elif(val == 2):
        #Búum til forrit sem hefur 100 random tölur á bilinu 200-600 í lista
        ranlisti = randomTolur(100,200,600)
        even = filter(lambda x : x%2==0,ranlisti)
        print(ranlisti)
        print(even)


    elif(val == 3):
        #Notið listann úr dæmi 1 til að finna allar tölur sem ganga upp í 5
        #og eru stærri en 350.Notið filter() fallið
        ranlisti = randomTolur(20,1,1001)
        listaTal = list(filter(lambda x: x%5==0 and x>350, ranlisti))
        print("listaTal sem er hærri en 350",listaTal)

    elif(val == 4):
        #Búið til lista með 200 tölum á bilinu 100 til 900.
        #Notið map() fallið til að draga 2 frá hverri  tölu fyrir sig og setja í nýjan lista.
        ranlisti = randomTolur(200,100,901)
        print(ranlisti)
        nyjaListi = list(map(lambda x: x-2, ranlisti))
        print(nyjaListi)

    elif(val == 5):
        #Búið til lista með 200 tölum á bilinu 1 til 90.
        #Notið list comprehension til setja allar tölur í þriðjaveldi sem eru undir 6 í annan lista.
        ranlisti = randomTolur(200,1,90)
        print(ranlisti)
        nyjaListi = [x**3 for x in ranlisti if x <6]
        print(nyjaListi)

    elif(val == 6):
        #Búið til lista með 100 tölum á bilinu 1 til 20.
        #Notið list comprehension til setja allar tölur sem enda á 0 í annan lista. Prentið út listann í röð efsta talan fyrst.
        ranlisti = randomTolur(100,1,200)
        print(ranlisti)
        nyjaListi = [x for x in ranlisti if x % 10==0]
        print(nyjaListi)
        #for x in ranlisti:
            #if x % 10==0:
                #print(x)
    elif(val == 7):
        #Notið afturkvæmt fall til að margfalda allar tölur saman í lista.
        import math
        listi = [2,4,6,8,10]
        def afturkvaemt(listi,x):
            if x ==-1:
                return 1
            else:
                tala = listi[x]
                return (tala*afturkvaemt(listi,x-1))


        results = afturkvaemt(listi,len(listi)-1)
        print(results)
        print(math.pow(2,5))


    elif val == 8:
        #Notið genarator fall (yield) til þess að skrifa eina tölu í einu út úr 100 talna random lista
        #sem fallið tekur inn sem færubreytu(argument).
        def gen_rator(num):
            breytu = (num)
            for i in range(breytu):
                yield num[i]
        for stak in gen_rator(100):
            print(stak)


    elif val == 9:
        #Dæmi 9(hafið þennan lið í sér skjali)
        #Til er mörg söfn í python. Eitt af þessum söfnum er tkinter.py. prófið að importa það og gerið eftirfarandi forrit:

        pass
