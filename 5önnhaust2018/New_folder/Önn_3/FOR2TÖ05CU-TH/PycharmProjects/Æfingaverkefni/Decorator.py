
"""
def plus(tala):
    temp = tala + 2
    return temp

def adgerd(fall, tala):
    utkoma = fall(tala)
    return utkoma

print(adgerd(plus, 5))
"""
"""
def adSkilaFalli():
    def prenta():
        print("Halló")
    return prenta

nyttFall = adSkilaFalli()
nyttFall()
"""

def skreyta(fall):
    def inniFalli():
        print("Ég var skreytt")
        fall()
    return inniFalli
"""
nyrraFall = skreyta(print)
nyrraFall()

@skreyta
def oskreytt():
    print("Ég er alsendis óskreytt fall")

fint = skreyta(oskreytt)
fint()

oskreytt()
"""

############################################################

print("1.")
def gay():
    def insidegay():
        return "Hey gays"
    return insidegay()
print(gay())

print()
print("2.")

def first(string):
    print("one", string)


print(first("two"))

print()
print("3.")

def baetaStreng(fall): #Fékk svar
    def innraFall(t1,t2):
        print("Utkoman er þetta:", end=" ")
        return fall(t1,t2)
    return innraFall

@baetaStreng
def samlagning(t1,t2):
    utkoma = t1+t2
    return utkoma

@baetaStreng
def margfeldi(t1,t2):
    utkoma = t1*t2
    return utkoma

print(margfeldi(2,5))
print()
print("Dæmi: 4.")
def athMismunur(fall):
    def innraFall(t1,t2):
        if t1 < t2:
            svar = "Fyrri tala má ekki vera minni"
        else:
            svar = fall(t1,t2)
        return svar
    return innraFall

@athMismunur
def mismunur(t1,t2):
    utkoma = t1-t2
    return utkoma

print(mismunur(2,3))
print(mismunur(6,2))

##########################################################################################

print()
print("Dæmi: 2.1")

ald1 = int(input("Sláðu inn aldur persónu 1: "))
ald2 = int(input("Sláðu inn aldur persónu 2: "))
ald3 = int(input("Sláðu inn aldur persónu 3: "))


def who(fall):
    def getvalue(x,y,z):
        if fall(x,y,z) < 15:
            answer = "Þau eru börn. Meðalaldur er undir 15."

        elif fall(x,y,z) > 60:
            answer = "Þau eru ellilífeyrisþegar. Meðalaldur er yfir 60."

        else:
            answer = "Þau eru fullorðnir. Meðalaldur er á milli 30-60."

        return answer
    return getvalue

@who
def avgage(x,y,z):
    avg = (x+y+z)/3
    return avg

print(avgage(ald1, ald2, ald3))



