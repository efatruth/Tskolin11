#livinus felix bassey
#Skilaverkefni1
#12.09.2018

#a

def finnafn(dict):
    print("----------liður a:--------------")
    nafn = input("slaðu nafn")
    if nafn in dict:
        print(dict.get(nafn))
    else:
        print("nafn finnið  ekki")

#b
def baetaNafn(dict):
    print("----------liður b:--------------")
    simanumer=input("sladu simanumer: ")
    nafn = input("slaðu nafn")
    dict[nafn] = simanumer #Býr til item í simaskra með nafni sem key og simanumer sem value
    if simanumer in dict:
        print(dict.get(simanumer))
        print("Nafn og símanúmer skráð.")
    return dict

#c
def eydaNafn(dict):
    print("----------liður c:--------------")
    nafn=input("sláðu inn nafn manneskju sem þú vilt eyða úr símaskrá: ").lower()
    if nafn in dict: #ef nafn er í símaskrá
        del dict[nafn] #Eyðir key og value-inu hans sem nafn matchar
        print("nafni og símanúmeri hjá",nafn.title(),"hefur verið eytt.")
    else:
        print("Þetta nafn er ekki í símaskránni.")
    return dict

#d
def breySimNafn(dict):
    print("----------liður a:--------------")
    nafn=input("Sláðu inn nafn manneskju sem þú vilt breyta símanúmeri hjá: ")
    if nafn in dict:
        print("Núverandi símanúmer hjá " + nafn + ": " + simaskra[nafn])
        simanumer=input("Sláðu inn nýtt símanúmer fyrir " + nafn +":")
        dict[nafn] = simanumer #Breytir value fyrir key-ið sem nafn matchar
    return dict


#("----------fall fyrir 2--------------")
def makeList():
    listi = []
    fjoldi=int(input("Hvað eru margir skráðir í áfangann? (skrifaðu það með integer tölu): "))
    for x in range(fjoldi):
        nafn = input("Sláðu inn nafn  ")
        listi.append(nafn) #Bætir nafninu við listann
    return listi
''' 
def hvar_margar():
        print("Þú valdir lið 2")
        listiFOR = []
        margirFOR=int(input("Hvað eru margir skráðir í hópinn FOR1TÖ05CU? (skrifaðu það með integer tölu): "))
        margirFOR=margirFOR+1
        for x in range(1,margirFOR):
            nafn = input("Sláðu inn nafn "+str(x)+": ")
            listiFOR.append(nafn) #Bætir nafninu við listann
'''
        #a1
''' 
def  listiFOR_GSO():
        listiFOR.sort() #Sorterar stök í listanum í alphabetical order
        for x in listiFOR: #loopa sem keyrir jafn oft og það eru stök í listanum. Þegar loopan fer einn hring verður x alltaf næsta stak í listanum.
            print(x)

def listiGSO():
        listiGSO = []
        margirGSO = int(input("Hvað eru margir skráðir í hópinn GSÖ1TÖ05AU? (skrifaðu það með integer tölu): "))
        margirGSO = margirGSO + 1
        for x in range(1, margirGSO):
            nafn = input("Sláðu inn nafn " + str(x) + ": ")
            listiGSO.append(nafn) #Bætir nafninu við listann
        return listiGSO

        #a2
def baediLiStaf():
    listiGSO.sort()#Sorterar stök í listanum í alphabetical order
    for x in listiGSO: #loopa sem keyrir jafn oft og það eru stök í listanum. Þegar loopan fer einn hring verður x alltaf næsta stak í listanum.
        print(x)

        #b
def baediHopa():
        print("nemendur sem eru skráðir í FOR1TÖ05CU og GSÖ1TÖ05AU: ")
        for x in listiGSO: #loopa sem keyrir jafn oft og það eru stök í listanum. Þegar loopan fer einn hring verður x alltaf næsta stak í listanum.
            if x in listiFOR: #Ef nafnið er í listiFOR
                print(x) #Prentar nafnið

        #c
def hvorStaeri():
        if len(listiFOR)>len(listiGSO):
            print("Forritunarhópurinn er stærri")

        elif len(listiFOR)<len(listiGSO):
            print("Gagnasafnsfræðihópurinn er stærri")

        elif len(listiFOR)==len(listiGSO):
            print("Forritunar- og gagnasafnsfræði-hópurinn eru jafn stórir.")
        #d
def tvoOftust():
        for x in range(-2,0): #mínus tala þýðir frá endanum á listanum
            listiGSO.append(listiFOR[x]) #Nær í síðustu tvö nöfnin í listiFOR og setur þau í listiGSO
            del listiFOR[x] #Eyðir síðustu tveimur nöfnunum úr listanum listiFOR
        print(listiGSO)
        print(listiFOR)
        
'''
#("----------fall fyrir 3--------------")
def nafnLykil():
    print("Þú valdir lið 3")
    passWordDict = {}
    with open("lykilord.txt", "r") as f: #les skrána í lista
        passWordList=f.readlines() #les eina línu í einu og setur hana sem streng í lista úr lykilord.txt.

        for i in passWordList: #Nær í stökin í passWordList
            tI=i.strip().split(";") #Býr til temporary lista úr i sem splittar 1 staki í 2 stök við hvert ";". Listinn resettar eftir hvern hring í loopu.
            passWordDict[tI[0]] = tI[1] #setur stak 1 í tI sem key en stak 2 í tI sem value í passWordDict.






#("----------fall fyrir 4--------------")






flag=True
while flag==True:
    val = input("Sláðu inn lið sem þú vilt keyra 1, 2, 3, 4 eða 5 til að hætta: ")
    if val=='1':
        print("þú valdir lið 1.")
        simaskra = {'daníel': '6142242',
                    'ragnar': '8533580',
                    'sigurður': '7942438',
                    'friðrik': '7549925',
                    'benjamín': '58765432',
                    'hulda': '6244256',
                    'erna': '6853683',
                    'svala': '5803833',
                    'þuríður': '6137702',
                    'jónína': '7328050'}  # býr til dictionary sem heitir simaskra með keys og values


        simaskra = baetaNafn(simaskra)
        print(simaskra)

        simaskra = eydaNafn(simaskra)
        print(simaskra)

        simaskra = breySimNafn(simaskra)
        print(simaskra)

        ''' 
        flag2=True
        while flag2==True:
            print()
            val2 = input("Góðan daginn. \nsláðu inn 1 til að leita af símanúmeri, \n2 til að bæta við nafni og símanúmeri í símaskrá, \n3 til að eyða nafni og símanumeri, \n4 til að breyta símanúmeri hjá því nafni sem þú vilt, \n5 til að prenta símaskrána, \n6 til að hætta: ")
            if val2=="1":
                finnafn(simaskra)
            elif val2=="2":
                nafn=input("nafn: ").lower()
                simanumer=input("simanumer: ")
                simaskra[nafn] = simanumer #Býr til item í simaskra með nafni sem key og simanumer sem value
                print("Nafn og símanúmer skráð.")


            elif val2=="3":
                nafn=input("sláðu inn nafn manneskju sem þú vilt eyða úr símaskrá: ").lower()
                if nafn in simaskra: #ef nafn er í símaskrá
                    del simaskra[nafn] #Eyðir key og value-inu hans sem nafn matchar
                    print("nafni og símanúmeri hjá",nafn.title(),"hefur verið eytt.")

                else:
                    print("Þetta nafn er ekki í símaskránni.")

            elif val2=="4":
                nafn=input("Sláðu inn nafn manneskju sem þú vilt breyta símanúmeri hjá: ")
                if nafn in simaskra:
                    print("Núverandi símanúmer hjá " + nafn + ": " + simaskra[nafn])
                    simanumer=input("Sláðu inn nýtt símanúmer fyrir " + nafn +":")
                    simaskra[nafn] = simanumer #Breytir value fyrir key-ið sem nafn matchar


            elif val2 == "5":
                for key, value in simaskra.items(): #Býr til loopu sem keyrir jafn oft og lengd listans, rennur í gegnum öll items í listanum og "key" verður að key og "value" verður að value þess keys.
                    print(key.title() + ":" + value) #Prentar út nöfn og símanúmer

            elif val2=="6":
                flag2=False #Lætur mann hætta í lið 1

            else:
                print("Liður ófundinn. Reyndu aftur.")
        '''

#("----------kall fall fyrir 2--------------")
    elif val=='2':
        forListi =[]
        gsoListi =[]
        forListi=makeList()
        gsoListi = makeList()

        print("For listi")
        print(forListi)

        print("GSÖ")
        print(gsoListi)

        #item a
        gsoListi.sort()
        print("GSÖ listinn sorteraður")
        for x in gsoListi:
            print(x)

        forListi.sort()
        print("For listinn sorteraður")
        for x in forListi:
            print(x)

        # item b
        print("nemendur sem eru skráðir í FOR1TÖ05CU og GSÖ1TÖ05AU: ")
        for x in gsoListi: #loopa sem keyrir jafn oft og það eru stök í listanum. Þegar loopan fer einn hring verður x alltaf næsta stak í listanum.
            if x in forListi: #Ef nafnið er í listiFOR
                print(x) #Prentar nafnið
        # item c
        if len(forListi)>len(gsoListi):
            print("Forritunarhópurinn er stærri")

        elif len(forListi)<len(gsoListi):
            print("Gagnasafnsfræðihópurinn er stærri")

        elif len(forListi)==len(gsoListi):
            print("Forritunar- og gagnasafnsfræði-hópurinn eru jafn stórir.")

        # item d
        for x in range(-2,0): #mínus tala þýðir frá endanum á listanum
            gsoListi.append(forListi[x]) #Nær í síðustu tvö nöfnin í listiFOR og setur þau í listiGSO
            del forListi[x] #Eyðir síðustu tveimur nöfnunum úr listanum listiFOR
        print(gsoListi)
        print(forListi)

        
        """
        print("Þú valdir lið 2")
        listiFOR = []
        margirFOR=int(input("Hvað eru margir skráðir í hópinn FOR1TÖ05CU? (skrifaðu það með integer tölu): "))
        margirFOR=margirFOR+1
        for x in range(1,margirFOR):
            nafn = input("Sláðu inn nafn "+str(x)+": ")
            listiFOR.append(nafn) #Bætir nafninu við listann
        #a1
        listiFOR.sort() #Sorterar stök í listanum í alphabetical order
        for x in listiFOR: #loopa sem keyrir jafn oft og það eru stök í listanum. Þegar loopan fer einn hring verður x alltaf næsta stak í listanum.
            print(x)

        listiGSO = []
        margirGSO = int(input("Hvað eru margir skráðir í hópinn GSÖ1TÖ05AU? (skrifaðu það með integer tölu): "))
        margirGSO = margirGSO + 1
        for x in range(1, margirGSO):
            nafn = input("Sláðu inn nafn " + str(x) + ": ")
            listiGSO.append(nafn) #Bætir nafninu við listann
        #a2
        listiGSO.sort()#Sorterar stök í listanum í alphabetical order
        for x in listiGSO: #loopa sem keyrir jafn oft og það eru stök í listanum. Þegar loopan fer einn hring verður x alltaf næsta stak í listanum.
            print(x)
        #b
        print("nemendur sem eru skráðir í FOR1TÖ05CU og GSÖ1TÖ05AU: ")
        for x in listiGSO: #loopa sem keyrir jafn oft og það eru stök í listanum. Þegar loopan fer einn hring verður x alltaf næsta stak í listanum.
            if x in listiFOR: #Ef nafnið er í listiFOR
                print(x) #Prentar nafnið
        #c
        if len(listiFOR)>len(listiGSO):
            print("Forritunarhópurinn er stærri")

        elif len(listiFOR)<len(listiGSO):
            print("Gagnasafnsfræðihópurinn er stærri")

        elif len(listiFOR)==len(listiGSO):
            print("Forritunar- og gagnasafnsfræði-hópurinn eru jafn stórir.")
        #d
        for x in range(-2,0): #mínus tala þýðir frá endanum á listanum
            listiGSO.append(listiFOR[x]) #Nær í síðustu tvö nöfnin í listiFOR og setur þau í listiGSO
            del listiFOR[x] #Eyðir síðustu tveimur nöfnunum úr listanum listiFOR
        print(listiGSO)
        print(listiFOR)
        
"""

        """
    elif val=='3':
        print("Þú valdir lið 3")
        passWordDict = {}
        with open("lykilord.txt", "r") as f: #les skrána í lista
            passWordList=f.readlines() #les eina línu í einu og setur hana sem streng í lista úr lykilord.txt.

        for i in passWordList: #Nær í stökin í passWordList
            tI=i.strip().split(";") #Býr til temporary lista úr i sem splittar 1 staki í 2 stök við hvert ";". Listinn resettar eftir hvern hring í loopu.
            passWordDict[tI[0]] = tI[1] #setur stak 1 í tI sem key en stak 2 í tI sem value í passWordDict.

        name = input("\nSláðu inn leyni nafnið og ýttu á enter: ") #spyr um nöfn og leyniorð
        passWord = input("\nSláðu inn leyniorðið sem fylgir og ýttu á enter: ")
        if name in passWordDict.keys(): #ef nafn er lykill í passWordDict
            if passWordDict[name] == passWord:
                print("\nVELKOMIN")
            elif name in passWordDict.keys() or passWord in passWordDict.values(): #allskonar kannanir hér
                    print("\nRANGT")
        elif passWord in passWordDict.values(): #eða ef passWord er value í passWordDict
            print("\nRANGT")

        else:
            print("\nEKKI TIL")
        """
    elif val=='3':
        #("----------numer 3--------------")
        usernname = input("hvað heitir þú")
        passw = input("hvað lykillorð  þú")
        passWordDict = {}
        f =  open("lykilord.txt", "r") #les skrána í lista
        passWordList=f.read() #les eina línu í einu og setur hana sem streng í lista úr lykilord.txt.
        f.close()

        #print(passWordList)
        passWordList=passWordList.split("\n")
        passWordList.pop()
        print(passWordList)

        for i in passWordList: #Nær í stökin í passWordList
            name = i.split(";")[0] #Býr til temporary lista úr i sem splittar 1 staki í 2 stök við hvert ";". Listinn resettar eftir hvern hring í loopu.
            pw= i.split(";")[1]
            if name== usernname:
                if pw != passw:
                    print("Ekki til")
                    break
                elif pw== passw:
                    print("VELKOMIN!!")
                    break
            '''elif name != username:'''


    #("----------kalla fall fyrir 4--------------")
    elif val=='4':
        print("Þú valdir lið 4")
        string=input("\nSláðu inn streng og ýttu á enter: ")
        if len(string) % 2 == 0: #ef lengdin á strengnum er slétt tala
            for i in range(0, len(string), 2): #"2" þýðir að það plúsar alltaf 2 við i eftir hvert loop.
                print(string[i+1].upper(), end="") #velur staf númer i + 1 í strengnum og prentar hann í hástöfum. end="" lætur strenginn enda á engu í staðin fyrir nýja línu.
                print(string[i].upper(), end="") #velur staf númer i í strengnum og prentar hann í hástöfum. end="" lætur strenginn enda á engu í staðin fyrir nýja línu.

        else:
            for i in range(0, len(string) - 1, 2): #setjum -1 við len(string) svo kóðunn mun ekki gera neitt við síðasta stafinn.
                print(string[i + 1].upper(), end="")#velur staf númer i + 1 í strengnum og prentar hann í hástöfum. end="" lætur strenginn enda á engu í staðin fyrir nýja línu.
                print(string[i].upper(), end="")#velur staf númer i í strengnum og prentar hann í hástöfum. end="" lætur strenginn enda á engu í staðin fyrir nýja línu.
                print(string[-1].upper()) #Velur síðasta stafinn í strengnum en færir hann ekki. Setur hann í hástafi.
            print()



    elif val=='5':
        flag=False

    else:
        print("Þú valdir lið sem er ekki til. reyndu aftur.")
