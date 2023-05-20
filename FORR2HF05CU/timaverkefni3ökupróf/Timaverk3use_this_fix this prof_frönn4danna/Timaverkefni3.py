'''
livinus felix bassey
05.04.18
timaverkefni3
'''

import random
listi1 = []
listi2 = []
def bua_til_lista(random_min, random_max,fjoldi=200):
    listi=[]
    for x in range (fjoldi):
        tala = random.randint(random_min, random_max)
        listi.append(tala)
    return(listi)

def syna_lista(listi):
    for x in listi:
        print(x, end = ":")
    print()


def summa_og_medaltal(listi):
    summa = sum(listi)
    lengd = len(listi)
    print("the sum is",summa)
    samtalSumma = summa/lengd
    return round(samtalSumma,3)

def deiling_med_5_og_8(listi):
    for x in range(len(listi)):
        r = listi[x]
        if r % 5 == 0:
            print('im5',listi[x])
        elif r % 8 == 0:
            print('im 8',listi[x])

def skila_bili(listi,fra,til):
    for x in range(fra,til):
        print(listi[x])
        print(x)


listi1 = bua_til_lista(100,200,300)

syna_lista(listi1)

medaltal = summa_og_medaltal(listi1)
print("the average is:", medaltal)

deiling 0


#skila_bili(listi1,fra,til)


class fyrstiKlasi:
    def utreikningur(self,tal1,tal2,tal3,tal4):
        reikna = tal1*tal2*tal3*tal4
        utkoma = reikna/3
        print(round(utkoma,2))

class AnnaKlasi:
    def __init__(self,lid,stig):
        self.nafn_lids = lid
        self.fjoldi_stiga = stig

