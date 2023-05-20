#Along A. Loftsson
import math
import random

print("1.")
print()

class TrapisaTest:
    def __init__(self, a,b,c,d,h):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.h = h

    def ummalTrapisu(self):
        ummal = self.a+self.b+self.c+self.d
        return ummal

    def flatarmalTrapisu(self):
        flatarmal = self.h * ((self.a + self.b)/2)
        return flatarmal

    def trapisa_jafnarma(self): #This shit doesnt make sense
        if self.d == self.b or self.d == self.c or self.c == self.b or self.b == self.a:
            return True
        else:
            return False

    def read_me(self):
        explanation = "Trapisa eða hálfsamsíðungur er ferhyrningur þar sem tvær mótlægar hliðar eru samsíða"
        return explanation


class Bill: #Klassinn bíll með smið sem býr til bíl.
    def __init__(self,tegund,argerd,hradi,bensin,eydsla):
        self.tegund = tegund
        self.argerd = argerd
        self.hradi = hradi
        self.bensin = bensin
        self.eydsla = eydsla


    def createCar(self):
        type = self.tegund
        year = self.argerd
        speed = random.randrange(60, 190, 10)
        gas = random.randrange(30, 80, 5)
        usage = random.randrange(3, 5) #t.d. eyðir 3 lítra eftir 100 metra.
        return type,year,speed,gas,usage

a = int(input("Sláðu inn hlið a: "))
b = int(input("Sláðu inn hlid b: "))
c = int(input("Sláðu inn hlið c: "))
d = int(input("Sláðu inn hlið d: "))
h = int(input("Sláðu inn hæð: "))
trapisa = TrapisaTest(a,b,c,d,h) #Láta notanda slá inn hliðar.

print("Ummál er", trapisa.ummalTrapisu())
print("Flatarmál er", trapisa.flatarmalTrapisu())
print("er trapísa jafnarma?", trapisa.trapisa_jafnarma())
print(trapisa.read_me())

print()
print("3.")
print()


type = input("Sláðu inn tegund bíl 1: ") #Notað til að búa til bíl.
year = int(input("Sláðu inn árgerð bíl 1: "))

bill_1 = Bill(type, year, 0, 0, 0) #Set 0 við það sem smiðurinn breytir.

type = input("Sláðu inn tegund bíl 2: ")
year = int(input("Sláðu inn árgerð bíl 2: "))

bill_2 = Bill(type, year, 0, 0, 0)

type = input("Sláðu inn tegund bíl 3: ")
year = int(input("Sláðu inn árgerð bíl 3: "))

bill_3 = Bill(type, year, 0, 0, 0)

bill_1 = Bill.createCar(bill_1)
bill_2 = Bill.createCar(bill_2)
bill_3 = Bill.createCar(bill_3)
carlist = [bill_1, bill_2, bill_3]#Bílarnir settir í lista til að sjá hver vinnur.

x = 0
print("Keppni Hjá bílum:")
for i in carlist: #Sýnir hvaða bíll hefur hvað.
    x += 1 #
    print(x, "bíllinn er", i[0], i[1], "módel. Hann keyrir á hraðanum", i[2], "hefur", i[3],"lítra og eyðir", i[4],
          "lítra á 100 metrum")

x = 0
lengthlist = [] #Used to hold onto the times travelled.
results = [] #Notað til að sjá hvernir seinustu tveir verða í öðru og þriðja sæti.
no_gas = [] #Notað til þess að vita hvaða bíll er bensínlaus.


for i in carlist:
    length = math.trunc(1000/i[2]) #Notað til að sjá hvort bíllinn nær alla leið.
    if length*i[4] > i[3]:
        print(i[0], i[1], "nær ekki alla leið!")
        no_gas.append(0)
    else:
        lengthlist.append(length)
        no_gas.append(1)
    x += 1

if no_gas[0] == 0 and no_gas[1] == 0 and no_gas[2] == 0: #No one wins
    print("Allir töpuðu því enginn náði yfir.")

else: #Check who is first

    if no_gas.count(0) == 2: #Ef tveir bílar verða bensínlausir
        for i in range(2):
            if no_gas[i] == 0:
                pass
            elif no_gas[i] == 1:
                winner = carlist[i][0] #Ef báðir bílar komast ekki er enginn í öðru og þriðja sæti.
                second = "Enginn"
                last = "Enginn"
    elif no_gas.count(0) == 1: #Ef 1 verður bensínlaus.
        winner = []
        for i in range(3):
            if no_gas[i] == 0:
              last = carlist[i][0] #Seinasta sæti við bílinn sem varð bensínlaus.
            elif no_gas[i] == 1:
                winner.append(carlist[i])
        if winner[0][2] > winner[1][2]: #Til að vita hver er í öðru sæti.
            winner = carlist[0][0]
            second = carlist[1][0]
        elif winner[1][2] > winner[0][2]:
            winner = carlist[1][0]
            second = carlist[0][0]

    else: #Ef enginn bíll verður bensínlaus.
        if carlist[0][2] > carlist[1][2] and carlist[0][2] > carlist[2][2]:
            winner = carlist[0][0]
            for i in carlist:
                if i != carlist[0]:
                    results.append(i)

        elif carlist[1][2] > carlist[0][2] and carlist[1][2] > carlist[2][2]:
            winner = carlist[1][0]
            for i in carlist:
                if i != carlist[1]:
                    results.append(i)

        elif carlist[2][2] > carlist[0][2] and carlist[2][2] > carlist[1][2]:
            winner = carlist[2][0]
            for i in carlist:
                if i != carlist[2]:
                    results.append(i)

        else: #Ef bílarnir komast í jafntefli.
            if carlist[0][2] == carlist[1][2]:
                print("Jafntefli milli", carlist[0][0], "og", carlist[1][0])
                print("Síðastur var:", carlist[2][0])
            elif carlist[1][2] == carlist[2][2]:
                print("Jafntefli milli", carlist[1][0], "og", carlist[2][0])
                print("Síðastur var:", carlist[0][0])
            elif carlist[0][2] == carlist[2][2]:
                print("Jafntefli milli", carlist[0][2], "og", carlist[2][0])
                print("Síðastur var:", carlist[1][0])

        if results[0][2] == results[1][2]:  # Sjá hvaða bílar verða í öðru ef tveir eru bensínlausir.
            if lengthlist[0] * results[0][4] > lengthlist[1] * results[1][4]:
                second = results[0][0]
            else:
                second = results[1][0]
        else:
            if results[0][2] > results[1][2]:  # Sjá hvaða bíll er í öðru og þriðja ef enginn er bensínlaus.
                second = results[0][0]
                last = results[1][0]
            elif results[1][2] > results[0][2]:
                second = results[1][0]
                last = results[0][0]

    print("Sem er í fyrsta sæti er",winner)
    print("Sem er í öðru sæti er", second)
    print("Sem er seinastur er",last)
