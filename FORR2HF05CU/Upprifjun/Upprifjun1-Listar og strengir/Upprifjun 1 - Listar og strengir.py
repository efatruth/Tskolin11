#livinus felix bassey
#21st august 2018
#upprifjum lista og strengi

import random
#eða from random import *

#-----Strengjarallý-----#
#1.fall sem skila fjölda orða
def teljaOrd(strengur):
    outcom=strengur.split()
    return round(len(outcom),2)

streng = input("sláðu inn setningu")
print(teljaOrd(streng))

#2.Fyrstu 5 stafina/innslættina
def fyrstaFimm(stafina):
    result=stafina[0:5] #eða[:5]
    return result

setning = input("slaðu setningu")
print(fyrstaFimm(setning))

#3.Síðustu 4 stafina/innslættina
def lastFour(strengur):
    result=strengur[-4:]
    return result

utkoma = input("sláðu inn setning")
print(lastFour(utkoma))


#4•	Miðjustafinn í setningunni.
def finnamidju(strengur):
    utkoma=""
    if len(strengur)%2 !=0:
        nr = len(strengur)//2
        utkoma=strengur[nr]
    else:
        utkoma="það ekki tala"
    return utkoma

setning = input("sláður in setning")
print(finnamidju(setning))


#5.Finna öll s/S í textanum
def finnaS(strengur):
    new = ""
    for stak in strengur:
        if stak =="s" or stak=="S" or stak=="":
            new = new+stak
        else:
            new = new +"#"
        return new

setning = input("sladur inn setning")
print(finnaS(setning))

#-----Listarallý-----#

def ranLista():
    listi=[]
    for stak in range(100):
        tala = random.randint(34,68)
        listi.append(tala)
    return listi


'''
#-----Listarallý-----#
#Búið til random lista...:
randomlisti=[]
for x in range(100):
    randomtala=randrange(34,69)
    randomlisti.append(randomtala)
print("\nListi með random númerum frá 34 til og með 68:")
print(randomlisti)
'''

#Raðið listanum:
def radlist(listi):
    listi.sort()
    return listi

#meðaltal talnanna
def medaltal(listi):
    summa = sum(listi)
    lengd = len(listi)
    samtalSumma = summa/lengd
    return round(samtalSumma,2)


#Finnið stærstu og minnstu töluna...:
def staerMinnst(listi):
    print(round(sum(listi)/len(listi),2))
    print("\nStærsta talan í listanum er:", max(listi))
    print("\nMinnsta talan í listanum er:", min(listi))


#Ef summa talnanna í listanum...:
def efSumma(listi):
    print()
    while sum(listi) > 4500:
        listi.pop(0)
    print("Summa eftir að summa hans hefur verið gerð minni en 4500:", sum(listi))


#Hendið út öllum tölum sem ganga upp í 5:
def hendiTolu(listi):
    newList=[]
    for x in listi:
        if x % 5 !=0:
            newList.append(x)
    #print("Listinn eftir að búið er að fjarlægja allar tölur sem ganga upp í 5:")
    return newList

#Setjið töluna 40 í sér lista:
def toluna40(listi):
    listiMed40=[]
    for x in listi:
        if x == 40:
            listiMed40.append(x)
    return listiMed40

myList = ranLista()
print(myList)

myList= radlist(myList)
print("hérna er raðið listanum",myList)

medaltala = medaltal(myList)
print("meðaltal er:", medaltala)

#ekki með return
staerMinnst(myList)

#ekki með return
efSumma(myList)

print("Listi without the % 5", hendiTolu(myList))


print("A list with the number 40",toluna40(myList))



