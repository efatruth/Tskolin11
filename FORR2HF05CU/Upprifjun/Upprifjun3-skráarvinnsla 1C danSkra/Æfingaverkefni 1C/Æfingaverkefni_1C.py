
from math import *


#Búið til textaskrá...
with open("tolur.txt",'w',encoding='utf-8') as f: #býr til skjalið tolur.txt og gerir það mögulegt að edita í það
    for x in range(21): #Býr til loopu sem keyrir 21 sinnum þar sem x hækkar alltaf um 1 þegar það loopar
        tala=str(int(pow(2,x))) #tala verður 2 í x veldi
        f.write(tala+" ") #skrifar value-ið sem "tala" er inn í tolur.txt og bil


#a
print("\nLiður a:")

with open("tolur.txt",'r',encoding='utf-8') as f: #opnar skjalið tolur.txt og gerir það mögulegt að nota innihald þess
    for tolulisti in f: #tolulisti verður allur strengurinn sem er inni í tölur.txt
        tolulisti=tolulisti.split(" ") #tolulisti.split býr til nýtt value eftir hvert bil í strengnum og setur það í lista
    tolulisti.remove('') #eyðir tómu value-i úr tolulisti
print(tolulisti)


#b
print("\nLiður b:")

x=0
with open("tolur.txt",'r',encoding='utf-8') as f: #opnar skjalið tolur.txt og gerir það mögulegt að nota innihald þess
    lina=f.read() #lina verður allur strengurinn inni í tolur.txt
    tel=0
    listi=lina.split(" ") #lina.split býr til nýtt value eftir hvert bil í strengnum og setur það í lista
    listi.remove('') #Eyðir tómu value-i úr "listi"
    for x in listi: #býr til loopu sem keyrir jafnoft og það eru values í listanum og x verður að value-inu.
        tel+=1 #tel hækkar um einn alltaf þegar loopan byrjar
        print(x,end=' ') #prentar x og bil. End lætur það enda á bili í staðin fyrir nýja línu
        if tel % 10==0: #ef tel modulus 10==0:
            print() #prenta nýja línu


#c
print("\n\nLiður c:")

tolulisti2=[]

for x in tolulisti:
    if x[-1]=="6": #ef síðasti character á value-inu "x" er strengurinn "6"
        tolulisti.remove(x) #eyðir value-inu "x" úr tolulisti
        tolulisti2.append(x) #Bætir value-inu "x" í tolulisti2
print(tolulisti)
print(tolulisti2)

with open("tolur2.txt",'w',encoding='utf-8') as f: #Býr til skjal sem hetir tolur2.txt, opnar það og gerir það mögulegt að edita það
    for x in tolulisti2: #býr til loopu sem keyrir jafn oft og listinn er langur og x verður næsta value úr listanum
            f.write(x + " ") #skrifar value-ið x og bil inn í tolur2.txt

tolulisti = list(map(int, tolulisti)) #breytir values í listanum yfir í int
tolulisti2 = list(map(int, tolulisti2)) #breytir values í listanum yfir í int



#d
print("\nLiður d:")

with open("tolur.txt",'r',encoding='utf-8') as f: #opnar skjalið tolur.txt og gerir það mögulegt að nota innihald þess
    lina=f.read() #lina verður allur strengurinn inni í tolur.txt
    tel=0
    listi=lina.split(" ") #lina.split býr til nýtt value eftir hvert bil í strengnum og setur það í lista
    listi.remove('') #Eyðir tómu value-i úr "listi"
    for x in listi: #býr til loopu sem keyrir jafnoft og það eru values í listanum og x verður að value-inu.
        tel+=1 #tel hækkar um einn alltaf þegar loopan byrjar
        print(x,end=' ') #prentar x og bil. End lætur það enda á bili í staðin fyrir nýja línu
    print() #prenta nýja línu


    with open("tolur2.txt",'r', encoding='utf-8') as f: #opnar skjalið tolur2.txt og gerir það mögulegt að nota innihald þess
        lina = f.read() #lina verður allur strengurinn inni í tolur.txt
        tel = 0
        listi = lina.split(" ") #lina.split býr til nýtt value eftir hvert bil í strengnum og setur það í lista
        listi.remove('') #Eyðir tómu value-i úr "listi"
        for x in listi: #býr til loopu sem keyrir jafnoft og það eru values í listanum og x verður að value-inu.
            tel += 1 #tel hækkar um einn alltaf þegar loopan byrjar
            print(x, end=' ') #prentar x og bil. End lætur það enda á bili í staðin fyrir nýja línu
        print() #prenta nýja línu


#e
print("\n Liður e:")

dictmedtolum={} #býr til dictionary

y=0
with open('tolur2.txt', 'r', encoding='utf-8') as f: #opnar skjalið tolur2.txt og gerir það mögulegt að nota innihald þess
    for space in f: #space verður allur strengurinn sem er inni í tölur.txt
        x = space.split(" ") #space.split býr til nýtt value eftir hvert bil í strengnum og setur það í lista
        x.remove('') #eyðir tómu value-i úr listanum
        x = list(map(int, x)) #Breytir values í listanum yfir í int
        for a in x: #býr til loopu sem keyrir jafnoft og það eru values í listanum "x" og "a" verður að value-inu.
            y=y+1
            dictmedtolum[y] = a #"y" verður key að value-inu "a" í dictionaryinu "dictmedtolum"
print(dictmedtolum)

