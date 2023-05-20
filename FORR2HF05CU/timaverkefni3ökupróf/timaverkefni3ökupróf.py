#livinus felix bassey
#Timaverkefni 3 ökupróf
#10.12.2018

import random
on = 1
while on == 1:
    print("dæmi.1,forrit sem tekur tvær heiltolu ")
    print("dæmi.2,forrit sem hefur klasann ")
    print("dæmi.3,útfæra base-klasann ")
    val = int(input("veldu val 1 - 3"))

    #Dæmi eitt
    #if val == 1:
    def add(tal1, tal2):
        return tal1 + tal2
        print("hvada æfinga")
        print("Æfing 1")

        #Safna innslátu frá notanda
        vali = input("innslátu(1):")


        if vali == '1':
            print(fjol1,"+",fjol2,"=", add(fjol1,fjol2))
        else:
            print("tolu er slagid inn ekki !")

    #elif val == 2:
        class konni: #bý til klasa
            def __init__(self,nafn,aldur):  #bý til smið sem tekur nafn og aldur inn sem input
                nafn = str(nafn)
                aldur = str(aldur)
                self.nafn = nafn
                self.aldur = aldur

            def snorri(self, *args):
                self.args = args
                summa = sum(self.args)
                return summa

            def sigga(self, tala):
                self.a = tala
                return self.a

            lamba = lambda self, listi: [x for x in listi if x >= 40 and x >= 1]





    #elif val == 3:
        pass

x = konni("konni","59")

print(x.snorri(1,5,7,35))

flotturlisti=[32,46,50,51,89,90]
print(x.lamba(flotturlisti))
print("\n\n\n")


