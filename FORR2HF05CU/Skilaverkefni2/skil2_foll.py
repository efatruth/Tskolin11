#livinus felix bassey
#Skilaverkefni2_skil2_foll
#21.09.2018

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




def margfeldi_af(x,y):
    if x % y == 0:
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



def er_slett_tala(tolu):
    if tolu % 2 == 0:
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


