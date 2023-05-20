#Along A. Loftsson
import re
from tkinter import *


def findAge(): #Fyrir Dæmi 10.
    text2=age_entry.get()
    finalage=100-float(text2) #Dregur aldur frá 100.
    if finalage > 0: #Kemur ef þú ert undir 100 ára gamall
        finalnumber.configure(text=str(finalage)+" ár!")
    else:
        finalnumber.configure(text="Þú ert kominn yfir 100 ára aldur!!!") #Kemur ef þú ert 100 eða yfir 100 ára.
    print("Þú færð í raun töluna", finalage) #Þetta prentar töluna sem þú fékkst í raun í python forritinu.

def printName(): #Fyrir Dæmi 9.
    texti = entry_1.get()
    texti2 = entry_2.get()
    utkoma=float(texti)+float(texti2)
    label_4.configure(text=utkoma)
    print("útkoman er ",utkoma)


loop = True #Til að halda forritinu opið.
choice = True #Er notað til að velja milli valmöguleika.
while loop == True:
    try:
        print("-----------------------------------------------------")
        print("Valmynd:")
        print("1. Kennitala")
        print("2. Finna í Index")
        print("3. Mánuðir 1")
        print("4. Mánuðir 2")
        print("5. Spurningar og Svör")
        print("6. LEGB breytur (Scope)")
        print("7. Útskyring yfir geymslu hluta")
        print("8. Breyting á LEGB")
        print("9. 2 forrit Dæmi")
        print("10. Okkar eigið forrit")
        print("11. Hætta.")
        print("-----------------------------------------------------")
        print()
        choice = int(input("Veldu: "))
        print()

        if choice == 1:
            print("Liður 1")
            print()
            kt = input("Sláðu inn kennitölu sem þú villta prufa: ")

            if re.search("^\d{6}-?\d{3}[9,0]$", kt): #Regex sem finnur íslenskar kennitölur sem endar á 9 eða 0.
            #Dagsetning á bilinu 1-30 og mánuður á bilinu 1-12
                if 1<= int(kt[0:2]) <= 30 and 12 >= int(kt[2:4]) and 9 == int(kt[-1:]) or 0 == int(kt[-1:]):
                    print("Kennitala lögleg")
                else:
                    print("Kennitala ekki rétt.")
            else:
                print("Kennitala ekki rétt.")
            input("Ýttu á enter til þess að halda áfram.")

        elif choice == 2:
            print("Liður 2")
            print()
            stafir_og_tolur = "abc 123 def 456 ghjk 7890 lm 12 nop 345 q 6 rstuv 78901 xyz 234"
            for i in re.finditer('(\d{1,})', stafir_og_tolur): #Finnur iter. eftir fyrsta staf fyrir hvert orð í strengnum.
                print("Grúppa: ",i.group()) #Sýnir í hvaða grúppu hún er í.
                print("Start index: ", i.span()[0]) #Sýnir hvaða tölu stafurinn er í röðinni.
            input("Ýttu á enter til þess að halda áfram.")

        elif choice == 3:
            print("Liður 3")
            print()
            my_regex = ("\w+\s") #Tekur bara orð sem eru með tölustafi og bil.
            matches = re.findall(my_regex, "March, April 29, May 5, June 15, August, Dec 8")
            for match in matches: #Svo prentar það út eftir hvaða mánuður kemur fyrst.
                print("Match month: %s" % (match))
            input("Ýttu á enter til þess að halda áfram.")

        elif choice == 4:
            print("Liður 4")
            print()
            listi = ["March", "April 29", "May 5", "June 15", "August", "Dec 8"]
            for element in listi:
                m = re.match("([a-z]+)([0-9]+)", element.replace(" ", ""), re.I) #Skiptir inn element og tekur a-z og númer.
                if m: #Ef m virkar þá er það formattað þannig að það birtir eins og það á að birta.
                    print("{0:7}{1}".format((m.group(2)),
                                            (m.group(1))))
            print()
            input("Ýttu á enter til þess að halda áfram.")

        elif choice == 5:
            print("Liður 5")
            print() #Svör við spurningum.
            print("A. Fyrir hvað stendur namespace í python?")
            print('Svar: Það er kerfi sem er notað til þess að búa til nöfn sem eru ekki alveg eins.\n')
            print("B. Hvað er module í python?")
            print('Svar: Það er aðferð sem þú getur notað fyrir fjölda falla, eins og "library".\n')
            print("C. Hvað er átt við með hulun (scope)?")
            print('Svar: Það er aðferð sem forritið notar til að finna hvaða breytu á að nota.\n')
            input("Ýttu á enter til þess að halda áfram.")

        elif choice == 6:
            print("Liður 6")
            print()
            konni = "Global konni" #Skilbreytt sem global scope
            def localscope():
                konni = "Local konni" #Local scope
                def enclosedscope():
                    konni = "Enclosed konni" #Enclosed scope
                    print(konni)
                enclosedscope()
                print(konni)

            localscope()
            print(konni)
            print()
            input("Ýttu á enter til þess að halda áfram.")

        elif choice == 7:
            print("Liður 7")
            print() #Útskýring yfir ID
            print("Hver hlutur hefur sitt eigið ID, eða auðkenningu, sem er einstakt. T.d.")
            idlist = [2,6,4,3]
            idstring = "Hæ lololololololol"
            print('Listinn "idlist" hefur ID-ið:', id(idlist))
            print('String-ið "idstring" hefur ID-ið:', id(idstring))
            print('Eins og þú sérð er idlist með ID-ið',id(idlist), 'og "idstring" með', id(idstring),' þannig er það geymt.')
            print()
            input("Ýttu á enter til þess að halda áfram.")

        elif choice == 8:
            print("Liður 8")
            print() #Sett global konni fyrir utan til að skilgreina að það sé nýja breytan í global scale.
            global konni
            def localscope():
                #konni = "Local konni"
                def enclosedscope():
                    #konni = "New konni"
                    print(konni)

                enclosedscope()
                print(konni)

            konni = "Global konni"
            localscope()
            print(konni)

            input("Ýttu á enter til þess að halda áfram.")

        elif choice == 9:
            print("Liður 9")
            print() #Sýnidæmi yfir forrit.
            print("1. Fyrsta Forrit")
            print("2. Seinna Forrit")
            program = int(input("Viltu fá fyrsta forritið eða seinna?"))
            print("Mundu að loka forritinu til þess að halda áfram.")
            if program == 1:
                root=Tk()
                label_1=Label(root,text="Sláðu inn tölu eitt")
                label_2=Label(root,text="Sláðu inn tölu tvó")
                label_3=Label(root,text="Tölurnar lagðar saman")
                texti=StringVar()
                texti2=StringVar()
                entry_1=Entry(root,textvariable=texti)
                entry_2=Entry(root,textvariable=texti2)
                texti=entry_1.get()
                label_4=Label(root,text="")
                label_1.grid(row=0,sticky=E)
                label_2.grid(row=1,sticky=E)
                label_3.grid(row=3,sticky=E)
                entry_1.grid(row=0,column=1)
                entry_2.grid(row=1,column=1)
                label_4.grid(row=3,column=1)

                button_1=Button(root,text=" Leggja saman ",command=printName)
                button_1.grid(columnspan=2)
                root.mainloop()

            elif program == 2:
                root =Tk()#auður gluggi
                topFrame=Frame(root)
                one=Label(root,text="einni",bg="red",fg="red")
                two=Label(root,text="einni",bg="yellow",fg="blue")
                one.pack(fill=X)
                two.pack(side=LEFT,fill=Y)
                topFrame.pack()
                bottomFrame=Frame(root)
                bottomFrame.pack(side=BOTTOM)
                button1=Button(topFrame,text="ýttu á mig",fg="red")
                button2=Button(topFrame,text="button2",fg="blue")
                button3=Button(topFrame,text="button2",fg="yellow")
                button4=Button(bottomFrame,text="button2",fg="purple")
                button1.pack(side=LEFT)
                button2.pack(side=LEFT)
                button3.pack(side=LEFT)
                button4.pack(side=BOTTOM)
                theLabel=Label(root,text="hér er ég")#búa til merkjamiða með ákveðnum texta staðsettan á formin
                theLabel.pack()#settu það inn
                root.mainloop()#heldur glugganum opnum birtist aftur og aftur
            else:
                print("Þetta var ekki valmöguleiki.")

        elif choice == 10:
            print("Liður 10")
            print()
            #Ég var þegar búinn að klára lið 10, þannig hérna er það til gamans.
            root = Tk()
            title=Label(root,text="Hvenær verður þú 100 ára?")
            name_label=Label(root, text="Sláðu inn Nafnið þitt: ")
            age_label=Label(root, text="Sláðu inn aldur: ")
            years_label=Label(root, text="Þú verður 100 ára eftir...")
            name_text=StringVar()
            age_text=StringVar()
            name_entry=Entry(root, textvariable=name_text)
            age_entry=Entry(root, textvariable=age_text)
            text=name_entry.get()
            finalnumber=Label(root,text="")
            title.grid(row=0,sticky=E)
            age_label.grid(row=3,sticky=E)
            years_label.grid(row=5,sticky=E)
            age_entry.grid(row=3,column=1)
            finalnumber.grid(row=5,column=1)

            button_1=Button(root,text=" Leggja saman ", command=findAge)
            button_1.grid(columnspan=2)
            root.mainloop()

        elif choice == 11: #Hættir á forriti.
            loop = False
            choice = False
            print("Takk fyrir mig.")

        else: #Ef valið er eitthvað annað en það sem er boðið upp á.
            print("Þetta er ekki valmöguleiki.")

    except ValueError: #Ef reynt er að slá inn eitthvað annað en númer.
        print("Þetta er ekki hægt að gera.")
