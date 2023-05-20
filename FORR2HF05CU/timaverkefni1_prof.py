#livinus felix bassey
#timaverkefni1_prof
#28.09.2018

import sys
import time
from datetime import datetime

def menu(listi):
    print('\n Valmynd: ')
    count = 0
    for i in listi:
        print('',count,') :',i,': ')
        count += 1


def kasta_pening(a,b):
    if a % b == 0:
        flag = True
        time.sleep(1)
    else:
        flag = False
        time.sleep(1)
    return flag


def gisk_tala(numb):
    if numb  == 430:
        flag = True
    else:
        flag = False
    return flag


def Takk(secs):
    for i in range(secs):
        for i in range(5):
            print(' eigu godan dag')
            time.sleep(0.9, 0.8, 0.7)
    print('\n Hvada viku og mánadaðagur er nuna?')


main_m = ['kasta pening','hæta']

continuity = True

#Biðja um nafn notanda
users_name = input('Sláðu inn nafn þitt: ')

while continuity:
    try:
        menu(main_m)
        val = int(input('\n hvað ciltu gera: '))
        time.sleep(1)
        if val == 0:
                #her forrits með nafni notanda sem spurt var um í byrjun forrits og birta hvað er klukkan er.
            print('\n Takk notkun forritsins',users_name)
            print(' Klukkan er: ',datetime.now().time().strftime('%H:%M:%S'))
            time.sleep(3)

            continuity = False

        elif val == 1:

            continue1 = True

            while continue1:
                try:

                    numb = int(input('\n giskadu (0 til að hætta): '))
                    time.sleep(1)

                    if numb == 0:
                        break
                    elif gisk_tala(numb):


                        print(numb,'\n  er of ha reyndur aftur')
                        time.sleep(1)

                    else:
                        print('\n vel gert þu fannst toluna.')
                        time.sleep(1)

                except ValueError:
                    print(numb,'\n  er of lag. Reyndu aftur.')
                    time.sleep(1)

        elif val == 2:

            continue2 = True

            while continue2:
                try:

                    numb1 = int(input('\n hvad viltu gera '))

                    if numb1 == 0:
                        continue2 = False

                    else:

                        numb2 = int(input(': '))
                        time.sleep(1)
                        # ef True er seinni talan margfeldi af fyrri
                        if margfeldi_af(numb1, numb2) == True:
                            print('\n ')
                            time.sleep(1)
                        # ef False er seinni talan ekki margfeldi af fyrri
                        elif margfeldi_af(numb1, numb2) == False:
                            print('\n ')
                            time.sleep(1)
                # ef ekki er sleigið inn heiltölu byrta error skilaboð
                except ValueError:
                    print('\n S', sys.exc_info())
                    time.sleep(1)




        elif val == 3:

            continue3 = True

            while continue3:
                try:

                    Takk_time = int(input('\n Í hvað margar sekúndur á að Takk: '))
                    Takk(Takk_time)
                    break

                except ValueError:
                    print('\n Oops það kom upp smá villa: ',sys.exc_info()[0],sys.exc_info()[1])



    except:
        print(' Oops það kom upp villa: ', sys.exc_info()[0],sys.exc_info()[1])
        Takk.sleep(1)
