#Along A. Loftsson
import re

class Geimvera:
    def __init__(self):
        self.frumnafn = "Geimvera"

    def HverErEg(self):
        vera = ("Ég er", self.frumnafn)
        vera = " ".join(vera)
        return vera

class Venus(Geimvera):
    def __init__(self, litur, tala):
        Geimvera.__init__(self)
        self.litur = litur
        self.tala = tala
        self.nafn = "Venus"

    def HverErEg(self):
        frumnafn = self.frumnafn
        text = ("Ég er", frumnafn, "frá", self.nafn, "Talan er", self.tala, "og liturinn er", self.litur)
        text = " ".join(text)
        return text

class Mars(Geimvera):
    def __init__(self, litur, tala):
        Geimvera.__init__(self)
        self.litur = litur
        self.tala = tala
        self.nafn = "Mars"

    def HverErEg(self):
        frumnafn = self.frumnafn
        text = ("Ég er", frumnafn, "frá", self.nafn, "Talan er", self.tala, "og liturinn er", self.litur)
        text = " ".join(text)
        return text


class Snorri:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def konni(self):
        mylist = range(self.a,self.b,self.c)
        for i in mylist:
            yield i

    def sigga(self):
        dictionarymade = {"a":self.a, "b":self.b, "c":self.c}
        return dictionarymade

    def tolur(self):
        otilgreind = int(input("Sláðu inn hversu margar tölur þú vilt setja inn: "))
        summa = 0
        for i in range(otilgreind):
            tala = int(input("Sláðu inn tölu: "))
            summa += tala
        return summa

    def breyta(self):
        newglobal = int(input("Sláðu inn tölu: "))
        global summan
        summan = newglobal
        return summan

    def lamba(self):
        otilgreind = int(input("Sláðu inn lengd listans: "))
        oldlist = []
        for i in range(otilgreind):
            tala = int(input("Sláðu inn tölu: "))
            oldlist.append(tala)
        filteredlist = list(filter(lambda x: 50 < x < 90 and x%2 == 0, oldlist))
        return filteredlist


print("1.")
print()

passwd = input("Sláðu inn lykilorð: ")
if re.match('^[A-Z]{1}[a-zA-Z]{3}\d{2}[^"]{1,}[#$&]$', passwd):
    print("Lykilorð virkar")
else:
    print("Lykilorð virkar ekki.")
print()
print("2.")
print()

x = int(input("Sláðu inn Færibreytu 1: "))
y = int(input("Sláðu inn Færibreytu 2: "))
z = int(input("Sláðu inn Færibreytu 3: "))

klassi = Snorri(x,y,z)
print("Tölur á milli x og y sem hoppar með z er:")
for i in klassi.konni():
    print(i)
print("Dictionary: ",klassi.sigga())
summan = klassi.tolur()
print("Summa tölurnar verða:",summan, "Þetta notar breytuna 'summan'.")
print("Breytan 'summan' verður að:",klassi.breyta())
print("Listi sem er með tölur á milli 50 og 90 og er líka sléttar tölur:", klassi.lamba())


print()
print("3.")
print()

hlutur1=Geimvera()
hlutur2=Venus("gulur", "22")
hlutur3=Mars("rauður", "136")
print(hlutur1.frumnafn)
print(hlutur1.HverErEg())
print(hlutur2.nafn)
print(hlutur2.HverErEg())
print(hlutur3.nafn)
print(hlutur3.HverErEg())
