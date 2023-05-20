#livinus felix bassey
#Skilaverkefni2
#02.11.2018

list1=["konni","sigga","snorri"]
list2=["fótbolti","handbolti","blak"]


nyjan_lista=[x+y for x in ["konni","sigga","snorri"]for y in["fótbolti","handbolti","blak"]]
print(nyjan_lista)




class Geimvera():
    def __init__(self,nafn,litil,tala):
        self.nafn = nafn
        self.litil = litil
        self.tala = tala

    def get_nafn(self):
         return self.nafn
    def get_litil(self):
         return self.litil
    def get_tala(self):
         return self.tala

    def set_nafn(self,newNafn):
            self.nafn=newNafn
    def set_litil(self,newLitil):
            self.litil =newLitil
    def set_tala(self,newTala):
            self.tala =newTala


    def __str__(self):
            return "Eg er Geiimavera"

class Venus(Geimvera):
    def __init__(self,nafn,litil,tala):
        self.nafn = nafn
        self.litil = litil
        self.tala = tala
    def __str__(self):
            return "Ég er Geimavera fra venus talan er" + str(self.tala) + "og liturinn er"+ self.litil


class Mars(Geimvera):
    def __init__(self,nafn,litil,tala):
        self.nafn = nafn
        self.litil = litil
        self.tala = tala
    def __str__(self):
            return "Ég er Geimavera fra mars talan er" + str(self.tala) + "og liturinn er"+ self.litil


hlutur1=Geimvera()
hlutur2=Venus("22","gulur")
hlutur3=Mars("136","rauður")

print(hlutur1.get_nafn())
print(hlutur2.get_litil())
print(hlutur3.get_tala())

hlutur1.set_nafn()
hlutur2.set_litil()
hlutur3.set_tala()
