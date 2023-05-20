#27.9.2017
#Daníel Arnarsson

#1
def prenta(func):
    return func
def streng():
    print("I got decorated")
prenta(streng())


#2
def Fyrsti(func):
    print("fyrsti")
    return func

def Annar(func):
    print("annar")
    return func
@Annar
@Fyrsti

#3

def ofurfall(func):
    def inner(a,b):
        print("Þessar tölur skila ", end="")
        return func(a,b)
    return inner


@ofurfall
def fall1(a,b):
    return a + b

@ofurfall
def fall2(a,b):
    return a * b
print(fall1(2,4))
print(fall2(2,4))


#4
def ofurfall(func):
    print("ofurfall")
    def inner(a,b):
        if (a-b) < 0:
            return "fyrri talan má ekki vera minn en sú síðari"
        else:
            return "mismunur talnanna er = " + str(func(a,b))
    return inner

@ofurfall
def fall1(a,b):
    return a-b
#útskrift
print("fyrsta kall")
print(fall1(2,4))
print("annað kall")
print(fall1(4,2))
