#Along A. Loftsson. 22.08.2017
import random
print("1.") #Strengjarallý

#Fjölda orða
x = input("Sláðu inn streng: ")
value = len(x.split()) #Skipta niður orð og setja "len" til að telja það.

#Finna miðjustaf.
counting = len(x.replace(" ", ""))
if counting%2 == 0: #Ef heildarstrengurinn (ekki með bil) er slétt tala, er ekki miðjustafur.
    middle = "Enginn!"
else:
    middle = int(((counting-1)/2)) #Heildarstrengur er skiptur í tvennt og tekið einn staf í burtu (listi byrjar á 0)
    middle = x[middle]

#Finna öll s/S í textanum
instances = 0 #Hvað mörg s eru í strengnum
count = 0 #Verður að Auto_Increment
Stringlisted = list(x) #Breytt í lista til þess að fara í gegnum staf eftir staf.
for i in Stringlisted: #Ef það er s í lista, er instance += 1.
    if i.lower() == "s":
        instances += 1
        count += 1
    elif i.lower() == " ": #nenni ekki hafa bil sem $, þannig einangra það bara.
        count += 1
    else:
        Stringlisted[count] = '$'
        count += 1
Stringlisted = "".join(Stringlisted) #Svo sameina það aftur í setningu.

print()
print("Fjölda orða er",value)
print("Fyrstu 5 stafir/Inslættir:", x[:5])
print("Síðustu 4 stafir/Inslættir:", x[-4:])
print("Miðju stafurinn er:", middle)
print("Öll s/S sem eru í strengum eru:", instances)
print("Strengurinn lítur svona út:", Stringlisted)
print()
input("Ýttu á Enter til þess að halda áfram.")
print()

print("2.")
print()

randomlist = []
for i in range(100): #Búa til random lista
    randomlist.append(random.randint(34, 68))

#Raða listanum
sortedlist = randomlist
sortedlist.sort(key=int)

#Finna meðaltal talnanna með 2 stafa nákvæmni
removeNumbers = 0
for x in randomlist:
    removeNumbers += x
average = round(removeNumbers/100, 2)


print("Listi með 100 tölum frá 34 til og með 68:", randomlist)
print("Raðaður listi", sortedlist)
print("Meðaltal talna er:", average)
print("Minnsta talan í listanum er:", min(randomlist), "og stærsta talan er:", max(randomlist))
print("Nú skal sýna summuna og dregið úr listanum ef summan er yfir 4500. Ýttu á Enter til þess láta það ganga.")

#Fá summuna undir 45000
while 4500 < removeNumbers:
    print("Summu listans er yfir 4500, og er", removeNumbers)
    removeNumbers -= randomlist[-1]
    randomlist.pop()
    input()

else:
    print("Núna er listinn undir 4500, og er", removeNumbers)


#Henda allar tölur sem ganga upp í 5.
fourtylist = []
for x in randomlist[:]:
    print(x)
    if x%5 == 0 and x != 40:
        randomlist.remove(x)
    elif x == 40: #Talan 40 sett í sér lista.
        fourtylist.append(x)
        randomlist.remove(x)

print("Núna eru öll númer sem ganga upp í 5 í listanum hent út. Listinn lítur svona út núna.")
print(randomlist)
print()
print("Talan 40 er sett í sér lista:")
print(fourtylist)
print()
print("See you space cowboy.")
