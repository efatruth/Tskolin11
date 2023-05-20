#Daníel Arnarsson
#4.10.2017


#1


def genfall():
    n = 1
    print("Nú hefur verið náð í mig í fyrsta sinn.")
    yield n
    n += 1

    print("Nú hefur verið náð í mig í annað sinn.")
    yield n

    n += 1
    print("Nú hefur verið náð í mig í þriðja sinn.")
    yield n

    n += 1
    print("Nú hefur verið náð í mig í fjórða sinn.")
    yield n

    n += 1
    print("Nú hefur verið náð í mig í fimmta sinn.")
    yield n

a=genfall()
next(a)
next(a)
next(a)
next(a)
next(a)


#2


listi=[10,20,30,40,50,60,70,80,90,100]

def genfall2(listi):
    for x in listi:
        yield x

b=genfall2(listi)

for x in range(len(listi)):
    print(next(b))


#3


listcomp=[x for x in range(1001) if x % 5==0 and x > 1 and x % 2==1]
print(listcomp)


#4

heilsanir=[x+y for x in ['Hallo ', 'Hae '] for y in ['yo','hei']]
print(heilsanir)
