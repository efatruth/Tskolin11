from random import *
#-----Strengjarallý-----#


#Skrifið inn streng.
strengur="Hallo eg heiti Strúturs"
print(strengur)

#Fjöldi orða:
fjoldiOrda=len(strengur.split())
print("\nFjöldi orða í strengnum: ", fjoldiOrda)

#Fyrstu 5 stafirnir:
first_5_char=strengur[:5]
print("\nFyrstu 5 stafir: "+first_5_char)

#Síðustu 4 stafirnir:
last_4_char=strengur[-4:]
print("\nSíðustu 4 stafir: "+last_4_char)

#Miðjustafurinn í setningunni:
lengdstrengs=len(strengur)
if lengdstrengs/2==int:
    print("\nÞað er enginn miðjustafur í strengnum því lengd hans er slétt tala")
else:
    midjustafur=lengdstrengs/2-0.5
    midjustafur=int(midjustafur)
    print("\nStafurinn í miðjunni er: "+strengur[midjustafur])

#Öll s/S í textanum:
finnaStafi=""
for x in strengur:
    if x=="S" or x=="s":
        finnaStafi+=str(x)
    elif x==" ":
        finnaStafi+=str(" ")
    elif x!="s" or x!="S":
        finnaStafi+=str("#")
print("\n" + finnaStafi)
        
#-----Listarallý-----#


#Búið til random lista...:
randomlisti=[]
for x in range(100):
    randomtala=randrange(34,69)
    randomlisti.append(randomtala)
print("\nListi með random númerum frá 34 til og með 68:")
print(randomlisti)

#Raðið listanum:
randomlisti.sort()
print("\nraðaður listi: ")
print(randomlisti)

#Finnið stærstu og minnstu töluna...:
print(round(sum(randomlisti)/len(randomlisti),2))
print("\nStærsta talan í listanum er:", max(randomlisti))
print("\nMinnsta talan í listanum er:", min(randomlisti))

#Ef summa talnanna í listanum...:

print()
while sum(randomlisti) > 4500:
    randomlisti.pop(0)
print("Listinn eftir að summa hans hefur verið gerð minni en 4500:")
print(randomlisti)

#Setjið töluna 40 í sér lista:
print()
listiMed40=[]
i = randomlisti.count(40)
print(randomlisti)
print()
for x in range(i):
    listiMed40.append(40)
    randomlisti.remove(40)

print("Listinn eftir að búið er að fjarlægja allar tölur sem jafngilda 40:")
print(randomlisti)
print()
print("Listi með jafnmikið af tölum sem jafngildu 40 í hinum listanum:")
print(listiMed40)

#Hendið út öllum tölum sem ganga upp í 5:
randomlisti = [x for x in randomlisti if x % 5 != 0]
print("\nListinn eftir að búið er að fjarlægja allar tölur sem ganga upp í 5:")
print(randomlisti)

    

