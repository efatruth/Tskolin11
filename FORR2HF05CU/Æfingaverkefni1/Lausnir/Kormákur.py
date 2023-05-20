

from random import *

def eydaStaki(listi, stak):
   return [gildi for gildi in listi if gildi != stak]

svar = 0
while svar != 3:
    print("*************************")
    print("*** 1 = Strengjarallý ***")
    print("*** 2 = Listarallý    ***")
    print("*** 3 = Hætta         ***")
    print("*************************\n")
    svar = int(input("Sláðu inn valmöguleikann sem þú vilt: "))
    print("\n")

    if svar == 1:
        #########################################
        ##########                     ##########
        ##########    Strengjarallý    ##########
        ##########                     ##########
        #########################################
        #Notandi slær inn streng
        strengur = input("Sláðu inn streng:")
        #Strengirnir t og a er skilgreindir sem 0, og verða notaðir sem teljarar
        t = 0
        a = 0
        #Þessi for lykkja fer í gegnum öll stök sem forritið fær eftir að hafa
        # skipt strengnum upp með bilunum.
        for i in strengur.split(" "):
            #Þessi if lykkja kemur í veg fyrir að tóm stök séu talin með sem
            # orð ef tvö bil eru hlið við hlið í strengnum.
            if i != "":
                #Teljarinn t gerir sitt og telur orðin í strengnum.
                t = t + 1
        #Forritið lætur notandann vita hversu mörg orð eru í strengnum.
        print("Það eru",t,"orð í strengnum")
        #Strengurinn fyrstu5 er skilgreindur sem fyrstu fimm innslættir í
        # strengnum.
        fyrstu5 = strengur[:5]
        #Forritið lætur notandann vita hverjir fyrstu fimm inslættirnir í
        # strengnum eru.
        print("Fyrstu 5 innslættir eru:",fyrstu5)
        #Strengurinn sidustu4 er skilgreindur sem síðustu fjórir innslættir í
        # strengnum.
        sidustu4 = strengur[-4:]
        #Forritið lætur notandann vita hverjir síðustu fjórir inslættirnir í
        # strengnum eru.
        print("Síðustu 4 innslættir eru:",sidustu4)
        #Þessi for lykkja fer í gegnum öll stökin
        for i in strengur:
            #Teljarinn a gerir sitt og telur orðin í strengnum.
            a = a + 1
        #Þessi if lykkja athugar hvort fjöldi stafa sé slétt tala.
        if a % 2 == 0:
            #Ef fjöldinn er slétt tala, segir forritið notandanum hér.
            print("Það er enginn stafur í miðju setningar! Fjöldi stafa er slétt tala.")
        #Þessi else lykkja keyrir ef skilyrðið í if lykkjunni stendur ekki.
        else:
            #Ef fjöldi staka í strengnum er oddatala, er strengnum skipt í tvennt.
            midja = len(strengur) / 2
            #Þegar oddatölu er deilt í 2, vantar alltaf 0.5 upp á að það sé talan
            # í miðjunni, svo hér er 0.5 bætt við töluna.
            midja = midja + 0.5
            #Forritið segir notandanum númer hvaða stafur er í miðjunni, og hvaða
            # stafur það er.
            print("Stafur númer",int(midja),"er í miðjunni, það er",strengur[int(midja)])
        #Breytan nyrstrengur er afrit af breytunni strengur.
        nyrstrengur = strengur
        #Þessi for lykkja fer í gegnum öll stökin í breytunni nyrstrengur
        for i in nyrstrengur:
            #Ef stakið jafngildir ekki s, S eða bili, er því skipt út fyrir $
            if i != "s" and i != "S" and i != " ":
                nyrstrengur = nyrstrengur.replace(i,"$")
        #Strengurinn nyrstrengur er prentaður út.
        print(nyrstrengur,"\n")
    if svar == 2:
        ########################################
        #########                      #########
        #########      Listarallý      #########
        #########                      #########
        ########################################
        listi = []
        for i in range(100):
            o = randint(34,68)
            listi.append(o)
        print("Eftirfarandi eru 100 tölur á milli 34 og 68")
        print(listi)
        print("Eftirfarandi er sami listi, flokkaður")
        listi.sort()
        print(listi)
        summa = 0
        for i in listi:
            summa = summa + i
        medaltal = summa / 100
        print("Meðaltalið er",round(medaltal,2))
        print("Stærsta talan er",max(listi))
        print("Minnsta talan er",min(listi))
        while summa > 4500:
            listi = listi[:-1]
            print(listi[-1],"var fjarlægð ")
            summa = 0
            for i in listi:
                summa = summa + i
            print("Summan er nú",summa)
        print("\nNú verða öll stök sem jafngilda 40 færð yfir í sér lista")
        listiMedBara40 = []
        for i in listi:
            if i == 40:
                listiMedBara40.append(i)
        print("Listi með öllum stökum sem jafngilda 40 í hinum listanum:",listiMedBara40)
        listi = eydaStaki(listi,40)
        print("Listinn: ",listi)
        listi = [x for x in listi if x % 5 != 0]
        print("Listinn eftir að öllum tölum sem ganga í 5 hefur verið eytt:",listi,"\n")
    if svar == 3:
        print("\n\n\n\n\n\n\n\n\n\nTakk og bless\n\n")
        exit()