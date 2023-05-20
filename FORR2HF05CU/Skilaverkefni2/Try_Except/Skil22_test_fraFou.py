#livinus felix bassey
#Skilaverkefni2_skil2_test
#21.09.2018

"""
from skil2_foll import *

ferningur(5)

on = True
while on:
    print("1. langhlid")
    print("2. langhlid")
    print("3. langhlid")
    print("4. langhlid")
    print("5. langhlid")
    print("6. langhlid")
    print("1. langhlid")
    print("1. langhlid")

    try:
        val = int(input("Veldu hvað þú vilt gera"))

        if val ==1:
            val1=True
            while val1:
                print("veludu hliðarnar og notaðu minus til að hæta")
            try:
                talaA = int(input("Sláðu inn tölu A"))
                if talaA <0:
                    break
                talaB = int(input("Sláðu inn tölu B"))
                print("langhlid er:"langhlid(t1,t2))
            except ValueError:
                print("Þú þarft að velja tölu")
            pass

        elif val == 2:
            val1=True
            while val2:
                talA = int(input( slaðu fyrsta tala))

            pass
        elif val ==3:
            try:
                tala = int(input("Hversu stóran ferniing viltu"))
                ferningur(tala)
            except ValueError:
                print("Þú þarft að velja tölu")

        elif val ==4:
            pass

    except ValueError:
        print("Þú þarft að velja tölu")
"""



'''
Fuad Poroshtica
20.9.2018
'''

#þetta er skjal sem inniheldur öll föllin sem eru ekki partur af extended library
from Skil22_foll import *


#öll önnur imports
import sys
import time
from datetime import datetime


'''
Þetta er listi sem er notað til að gefa menu() fallinu 
orð fyrir aðal menuið
menu() getur síðan verið notað aftur ef þarf
'''


main_m = ['Hætta','Langhlid','Marfeldi','Fernigur','Slétt tala','Flatarmál hrings','Bank,Bank']

continuity = True

#Biðja um nafn notanda
users_name = input('Sláðu inn nafn þitt: ')

while continuity:
    try:
        menu(main_m)
        val = int(input('\n Sláðu inn val: '))
        time.sleep(1)
        if val == 0:
            '''
                Þakka fyrir notkun forrits með nafni notanda sem spurt var um í byrjun forrits
                og birta hvað er klukkan er.
            '''
            print('\n Takk fyrir notkun forritsins',users_name)
            print(' Klukkan er: ',datetime.now().time().strftime('%H:%M:%S'))
            time.sleep(3)

            continuity = False



        elif val == 1:

            continue1 = True

            while continue1:
                try:
                    #spurt er um leng aðlægu skammhliðar og sagt að minus tölur eða 0 sendir mann aftur á main menu
                    a_side = float(input('\n Sláðu inn lengd aðlægu skammhliðarinnar (0 eða mínus til að hætta): '))
                    time.sleep(1)
                    #ef stærra en 0 spurja um lengd skammhliðar
                    if a_side > 0:
                        b_side = float(input(' Sláðu inn lengd mótlægu skammhliðarinnar: '))
                        time.sleep(1)
                        #senda skammhliðar í fallið langhlid() sem skilar langhliðinni
                        print('\n Langhliðinn er: ',round(langhlid(a_side,b_side),2))
                        time.sleep(1)
                    #ef 0 hætta
                    else:
                        continue1 = False
                #ef ekki er sleigið inn heiltölu er tekið við value error
                except ValueError:
                    print('\n Þetta er ekki kommutala. Reyndu aftur.')
                    time.sleep(1)


        elif val == 2:

            continue2 = True

            while continue2:
                try:
                    #spurt er um heiltölu
                    numb1 = int(input('\n Sláðu inn heiltölu (0 til að hætta): '))
                    #ef val er 0: senda aftur í main menu
                    if numb1 == 0:
                        continue2 = False
                    #ef val er ekki 0: spurja um aðra heiltölu
                    else:
                        '''
                            Fallið margfeldi_af() tekur inn tvær tölur
                            og skoðar hvort seinni tala er margfeldi af sú fyrri
                            skilar True eða False
                        '''
                        numb2 = int(input(' Sláðu inn aðra heiltölu: '))
                        time.sleep(1)
                        #ef True er seinni talan margfeldi af fyrri
                        if margfeldi_af(numb1,numb2) == True:
                            print('\n Seinni talan er margfeldi af sú fyrri')
                            time.sleep(1)
                        #ef False er seinni talan ekki margfeldi af fyrri
                        elif margfeldi_af(numb1,numb2) == False:
                            print('\n Seinni talan er ekki margfeldi af sú fyrri')
                            time.sleep(1)
                #ef ekki er sleigið inn heiltölu byrta error skilaboð
                except ValueError:
                    print('\n Sláðu um heil tölu',sys.exc_info())
                    time.sleep(1)


        elif val == 3:

            continue3 = True

            while continue3:
                try:
                    #Spurt er um stærð fernings
                    squaresize = int(input('\n Sláðu inn stærð ferningsins(heiltala): '))
                    time.sleep(1)
                    '''
                        Þetta fall tekur inn heiltölu
                        og skilar ferningi úr stjörnum 
                        sem er jafn langur og heiltalan (Báðar hliðar)
                    '''
                    star_square(squaresize)
                    time.sleep(1)
                    break
                #ef ekki er slegið inn heiltölu byrta error skilaboð
                except ValueError:
                    print('\n Þetta er ekki Heiltala. Reyndu aftur.')
                    time.sleep(1)



        elif val == 4:

            continue4 = True

            while continue4:
                try:
                    #Spurt um heiltölu(0 til að fara i main menu)
                    numb = int(input('\n Sláðu inn heiltölu(0 til að hætta): '))
                    time.sleep(1)
                    #ef 0: main menu
                    if numb == 0:
                        break
                    elif er_slett_tala(numb):
                        '''
                            Heiltala er sent í fallið er_slett_tala sem skoðar hvort
                            talan er slett og skilar annaðhvort True eða False
                        '''

                        #ef true er talan slétt
                        print('\n Þetta er Slétt tala.')
                        time.sleep(1)
                    #ef False er talan ekki slétt
                    else:
                        print('\n Þetta er ekki slétt tala.')
                        time.sleep(1)
                # ef ekki er slegið inn heiltölu byrta error skilaboð
                except ValueError:
                    print('\n Þetta er ekki heiltala. Reyndu aftur.')
                    time.sleep(1)


        elif val == 5:

            continue5 = True

            while continue5:
                try:
                    #spurt er um radius hrings (0 eða - fyrir main menu)
                    rad = float(input('\n Sláðu inn radíusinn(0 eða -tala til að hætta): '))
                    time.sleep(1)
                    #ef 0 fara i main menu
                    if rad <= 0:
                        break
                    else:
                        '''
                            Radiusinn er sentur í fallið circle_surface() og það skilar
                            flatarmáli hringsins
                        '''
                        print('\n Flatarmálið er: ',circle_surface(rad))
                        time.sleep(1)

                # ef ekki er slegið inn float byrta error skilaboð
                except ValueError:
                    print('\n Oops það kom upp smá villa: ',sys.exc_info()[0],sys.exc_info()[1])
                    time.sleep(1)


        elif val == 6:

            continue6 = True

            while continue6:
                try:
                    '''
                        Spurt er um hversu margar sekúndur það á að banka í
                        heiltalan er sent inn í fallið Knock_Knock()
                        þetta fallið byrtir Bank á hverjum 0,2 sekúndum
                        í sekúndurnar sem notandi sló inn
                    '''
                    knock_time = int(input('\n Í hvað margar sekúndur á að banka: '))
                    knock_knock(knock_time)
                    break
                # ef ekki er slegið inn heiltölu byrta error skilaboð
                except ValueError:
                    print('\n Oops það kom upp smá villa: ',sys.exc_info()[0],sys.exc_info()[1])


    #except fyrir main menu valið(ef ekki er slegið inn heiltölu):
    except:
        print(' Oops það kom upp villa: ', sys.exc_info()[0],sys.exc_info()[1])
        time.sleep(1)

        """ 
skil2_test.py
Displaying Skil2_foll.py.
"""
