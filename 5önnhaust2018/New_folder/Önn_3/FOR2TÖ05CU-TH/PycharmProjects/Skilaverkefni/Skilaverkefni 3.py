#Along A. Loftsson
import random


def addition(func): #Dæmi 1
    def innerfunc(t1,t2): #Tekur tvær tölur og setur þær saman.
        number = t1+t2
        return func(number)
    return innerfunc

@addition #Bætir við fallið sem margfaldar með tvo.
def samlagning(number):
    outcome = number*2
    return outcome


def adeinsJafnarTolur(fall): #Dæmi 2
    def innraFall(*args): #Notar *arg til að sjá hvort tölurnar sem eru slegnar inn eru sléttar.
        if any([arg for arg in args if arg %2 != 0]):
            return "Bara nota jafnar tölur"
        utkoma = fall(*args)
        return utkoma
    return innraFall

@adeinsJafnarTolur #
def samlagning1(a,b):
    return a+b


def numbermulti(func): #Dæmi 3
    def innerfunc(number): #Dæmi 3
        if number < 0:
            multi = False
        else:
            multi = 1
            for i in range(1,number):
                multi += i*multi
        return func(multi)
    return innerfunc


@numbermulti #Dæmi 3
def checkminus(number): #Dæmi 3
    if number == False:
        return "Sorry but no fucking minuses.. sus.... susses"
    else:
        return number

def makeranlist(): #Dæmi 4
    for i in range(20):
        randomlist.append(random.randrange(1,101))
    return randomlist

def findcompatible(t1,list): #Dæmi 4
    gisk = 0
    for i in list:
        if i % t1 == 0:
            gisk += 1
    return gisk

def whowon(userguess, pcguess): #Dæmi 4
    print("Notandinn var með", userguess, "og Tölvan var með", pcguess)
    if userguess < pcguess:
        return "Tölvan vann."
    elif userguess > pcguess:
        return "Notandi vann."
    else:
        return "Jafntefli."


def findevennumbers(): #Dæmi 5
    for i in range(100):
        anotherrandomlist.append(random.randrange(200, 601))
    new_list = list(filter(lambda x: x % 2 == 0, anotherrandomlist))
    return new_list

def findfives(new_list): #Dæmi 6
    for x in new_list:
        fivelist = list(filter(lambda x: x % 5 == 0 and x > 350, new_list))
    return fivelist

def maketwohundredlist(new_list): #Dæmi 7
    for x in range(200):
        new_list.append(random.randrange(100, 901))
        new = list(map(lambda x: x - 2, new_list))
    return new

print("1.")
print()

t1 = int(input("Sláðu inn tölu 1: "))
t2 = int(input("Sláðu inn tölu 2: "))


print("Talan verður þá:", samlagning(t1,t2))

print()
print("2.")
print()

t1 = int(input("Sláðu inn tölu 1: "))
t2 = int(input("Sláðu inn tölu 2: "))

print(samlagning1(t1,t2))

print()
print("3.")
print()

multinumber = int(input("Sláðu inn tölu: "))

print(checkminus(multinumber))

print()
print("4.")
print()

randomlist = []


########## Gera Loop

t1 = int(input("Sláðu inn tölu á milli 1-10: "))
t2 = random.randint(1,10)

randomlist = makeranlist()
userguess = findcompatible(t1, randomlist)
computerguess = findcompatible(t2, randomlist)
print(whowon(userguess, computerguess))

print()
print("5.")
print()

anotherrandomlist = []

new_list = findevennumbers()
print(new_list)

print()
print("6.")
print()

print(findfives(new_list))

print()
print("7.")
print()

liste = []
numberlist = maketwohundredlist(liste)
newnumberlist = list(map(lambda x: x == x - 2, numberlist))
print(newnumberlist)

new = list(map(lambda x: x == x - 2, new_list))

print(new)