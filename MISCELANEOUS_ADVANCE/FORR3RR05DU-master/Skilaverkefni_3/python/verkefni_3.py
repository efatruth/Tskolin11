# Róbert Ingi.

from string import ascii_lowercase
from itertools import combinations
import time

def laStafir(fStafir):
    strengur = []
    for i in combinations(ascii_lowercase,fStafir):
        stafur = ""
        for ii in i:
            stafur += ii
        strengur.append(stafur)
    return strengur


def rugla(l):
    tmp = []
    for x in range((len(l)-1),-1,-1):
        tmp.append(l[x])
    return tmp

# Dæmi 4


def sort(listi):
    for passnum in range(len(listi)-1,0,-1):
        for i in range(passnum):
            if listi[i]>listi[i+1]:
                temp = listi[i]
                listi[i] = listi[i+1]
                listi[i+1] = temp

start = time.time()
abc = laStafir(4)
end = time.time()

print((end- start)*1000)


# Dæmi 5



abc = rugla(abc)

print("Orðin í rugli: \n{}\nLengd listans: {}".format(abc,len(abc)))
start = time.time()
sort(abc)
end = time.time()
print("Orðin í röðuð: \n{}\nLengd listans: {}".format(abc,len(abc)))
print((end- start)*1000)

