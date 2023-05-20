#Höfundur: Daníel Arnarsson
import re, random

#Dæmi 1
print("----Dæmi 1----")
#passw=input("Sláðu inn lykilorð")
#re.search('{8,9999}',passw)
print("\n\n\n")



#Dæmi 2
print("----Dæmi 2----")
class snorri: #bý til klasa
    def __init__(self,a,b,c):  #bý til smið sem tekur a,b og c inn sem input
        a = int(a)
        b = int(b)
        c = int(c)
        self.a = a
        self.b = b
        self.c = c

    def konni(self):  #bý til function
        if self.a > self.b:
            hopp = self.b + self.c
        elif self.a < self.b:
            hopp = self.a + self.c
        listi=[]
        listi.append(self.a)
        listi.append(hopp)
        listi.append(self.c)
        self.listi = listi
        return self.listi

    def sigga(self):
        dict = {}
        listi = self.listi
        dict["a"] = listi[0]
        dict["b"] = listi[1]
        dict["c"] = listi[2]
        return dict

    def tolur(self, *args):
        self.args = args
        summa = sum(self.args)
        return summa

    def breyta(self, tala):
        self.a = tala
        return self.a

    lamba = lambda self, listi: [x for x in listi if x <= 90 and x >= 50]




x = snorri(10, 2, 5)
print(x.konni())
print(x.sigga())
print(x.tolur(1,5,7,35))
print(x.breyta(7))
flotturlisti=[32,46,50,51,89,90]
print(x.lamba(flotturlisti))
print("\n\n\n")






#Dæmi 3
print("----Dæmi 3----")
class Geimvera:
    def __init__(self, litur=None, tala=None):
        self.litur = litur
        self.tala = tala
        self.frumnafn = "Geimvera"
        self.EgEr = "Ég er Geimvera"

    def HverErEg(self):
        return self.EgEr

class Venus(Geimvera):
    #def __init__(self):
        #super().Geimvera(self, etc.)
        # nafn = "Venus"
        #self.nafn = nafn
    nafn = "Venus"
    def HverErEg(self):
        nafn = "Venus"
        self.nafn = nafn
        print(self.EgEr, "frá", self.nafn, "Talan er", self.tala, "og liturinn er", self.litur)

class Mars(Geimvera):
    #def __init__(self):
        #super().Geimvera(self, etc.)
        # nafn = "Mars"
        #self.nafn = nafn
    nafn = "Venus"
    def HverErEg(self):
        nafn = "Venus"
        print(self.EgEr, "frá", self.nafn, "Talan er", self.tala, "og liturinn er", self.litur)



hlutur1 = Geimvera()
hlutur2 = Venus("gulur","22")
hlutur3 = Mars("rauður","136")
print(hlutur1.frumnafn)
print(hlutur1.HverErEg())
print(hlutur2.nafn)
print(hlutur2.HverErEg())
print(hlutur3.nafn)
print(hlutur3.HverErEg())


