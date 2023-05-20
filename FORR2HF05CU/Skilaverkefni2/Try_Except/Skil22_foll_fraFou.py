#livinus felix bassey
#Skilaverkefni2_skil2_foll
#21.09.2018


"""
import math

def langhlid(sidA, sidB):
    ans= pow(sidA,2 ) + pow(sidB,2)
    sidC = math.sqrt(ans)
    return round(sidC,2)
print(langhlid(3, 4))


def margfeldi_Af(fj1, fj2):
    if fj2 % fj1 == 0:
        return  True
    else:
        return False

if margfeldi_Af(40, 30)== True:
    print("annan tala er margfeldi af fyrsta tala")
else:
    print("það margfeldi EKKI hinni töluna")

def ferningur_ur_stjornum(fj):
    str = ""
    for stak in range(fj):
        str = str + "*"
    print(str)

ferningur_ur_stjornum(5)

#Liður 3
def ferningur(fj):
    for stak in range(fj):
        print("* "*fj)
"""



'''
Fuad Poroshtica
20.9.2018
Allar útskýringar eru í aðal skjalinu um hvernig föllin virka
'''

import math
import time




def menu(listi):
    print('\n Valmynd: ')
    count = 0
    for i in listi:
        print('',count,') :',i,': ')
        count += 1





def langhlid(a,b):
    c = math.sqrt((a**2)+(b**2))
    return c




def margfeldi_af(a,b):
    if a % b == 0:
        flag = True
        time.sleep(1)
    else:
        flag = False
        time.sleep(1)
    return flag




def star_square(stars):
    count = 1
    for i in range(stars**2):
        if count % stars == 0:
            print('*')
            count = 1
        else:
            print('*',end=' ')
            count += 1




def er_slett_tala(numb):
    if numb % 2 == 0:
        flag = True
    else:
        flag = False
    return flag



def circle_surface(radius):
    surface = (radius**2)*math.pi
    return float("%0.2f" % surface)




def knock_knock(secs):
    for i in range(secs):
        for i in range(5):
            print(' Bank')
            time.sleep(0.2)
    print('\n Hver er þar?')
Skil2_foll.py
Displaying Skil2_foll.py.
