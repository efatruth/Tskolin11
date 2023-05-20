#livinus felix bassey
#Skilaverkefni#
#10.09.2018

import csv
#livinus felix bassey
#Skilaverkefni2
#10.09.2018


class Lager_hlutur:

    def __init__(self, num,teg,fjol,ver):
        self.numer = num
        self.tegund = teg
        self.fjoldi = fjol
        self.verd = ver


    def verdReikhlut(self):
        result = self.fjoldi * self.verd #her vanta koda
        return result


    def prenta_lager_hlut(self):
        print(self.numer,self.tegund,self.fjoldi,self.verd) #her vanta koda self.tala1 * self.tala2


lagerhlutir = []

def opnaSkra():#def skraarlestur():
    lager = [] #temp[]
    with open('lagerhlutir.csv', 'r', newline='',encoding='utf-8') as file:
         reader = csv.reader(file, delimiter=';')
         id=0
         for i in reader:
             hlutur = Lager_hlutur(i[0],i[1],int(i[2]),int(i[3]))
             lager.append(hlutur)
    return lager

def lesaSkrana():
    lagerhlutir.clear()
    file = open('lagerhlutir.csv', 'r')
    content = file.read()
    file.close()
    line_s = content.split("\n")
    for rod in line_s:
        columns = rod.split(";")
        try:
            hlutur = Lager_hlutur(columns[0],columns[1],columns[2],columns[3],)
            lagerhlutir.append(hlutur)
        except IndexError:
            print('þetta er villa!')
def skrifaSkra(listi):#Skrifar í skrána.
    line = ""
    file = open("lagerhlutir.csv", "w", encoding='utf-8')
    for x in range(len(lagerhlutir)):
        line += str(lagerhlutir[x].numer) + ";" + lagerhlutir[x].tegund  + ";" + str(lagerhlutir[x].fjoldi) + ";" + str(lagerhlutir[x].verd) +"\n"
        file.write(line)
    file.close()
def nyrLagerhlutur():#bætir inn nýju tilviki(object,hluti)
    num = int(input('hvaða numer er hlutur með sem vanta bæta við'))
    teg = input('hvaða tegund er að bæta við')
    fjol = int(input('hver er fjoldi að bæta við'))
    ver = int(input('hvað er kostar hluturinn?'))
    tilv = Lager_hlutur(num,teg,fjol,ver)
    lagerhlutir.append(tilv)
def eydaLagerhlut(num):#eyðir tilviki(object,hluti)
    for stak in lagerhlutir:
        if stak.numer == num:
            lagerhlutir.remove(stak)
            print('þessari hlutið var eytt')

def breytaLagerhlut(nr, numer,teg,fj,kr):#breytir tilviki(object,hluti)
    for x in lagerhlutir:
        if x.numer == nr:
            x.numer = numer
            x.tegund = teg
            x.fjol = fj
            x.verd = kr
def prentaLager():#skrifar á skjáinn allt sem er í skránni(innhald listans af tilvikum)
    for row in reader:
        #row = [num,names,items,price]
        num = int(row[0])
        names = (row[1])
        items = int(row[2])
        price = int(row[3])
        listi.append([num,names,items,price])
        return listi

def heildarverdHlutar():#skrifar á skjáinn heildarverð hverrar tegundar fyrir sig
    file = open('lagerhlutir.csv', 'r')
    heilHver = csv.reader(file)
    for row in heilHver:
        row[3].count()
        return row(x[3])

def heildarverdLager():#skrifar á skjáinn heildarverð allra hluta á lager
    heilvLag=[]
    myFile=csv.reader(open('lagerhlutir.csv'),delimeter=',')
    headings = next(myFile)
    for row in myFile:
        heilvLag.append(row)
    return heilvLag
'''  
eitt = x.numer*x.verd
heildav = heildav + int(eitt)
print(heildav)
'''

def mittFall():#nefnið fallið einhverju lýsandi nafni frjálst val. Samt eitthvað spennandi og flott
    import os.path
    with open('lagerhlutir.csv', 'r', newline='',encoding='utf-8') as file:
         reader = csv.reader(file, delimiter=';')
         for line in lines:
             os.rename(line[0], line[1] + str('.png'))
    return os



#----1--------
#all the data from the file is in myListi as an instance of Lagerhlutur
lagerhlutir=opnaSkra()
for x in range(len(lagerhlutir)):
    print(lagerhlutir[x].tegund)

#writing a new item to the list Lagerhlutur
nyrLagerhlutur()
skrifaSkra(lagerhlutir)


"""
#Skrifar í skrána.
print(skrifaSkra(lagerhlutir))

#bætir inn nýju tilviki(object,hluti)
print(nyrLagerhlutur())

#eyðir tilviki(object,hluti)
print(eydaLagerhlut())

#breytir tilviki(object,hluti)
tal = int(input("hvaða lager viltu breyta ?"))
breytaHLut(tal,20,"box",150,890)
print(breytaLagerhlut())

#skrifar á skjáinn allt sem er í skránni(innhald listans af tilvikum)
x.append.prenta_lager_hlut()
print(prentaLager())

#skrifar á skjáinn heildarverð hverrar tegundar fyrir sig
print(heildarverdHlutar())

#skrifar á skjáinn heildarverð allra hluta á lager
print(heildarverdLager())


 
lagerhlutir= opnaSkra()#saman af lesaSkra() eða skrálestu:
heildav = 0
for x in lagerhlutir:
    x.prenta_lager_hlut()
    
#lesaSkra()
lagerhlutir[5].prenta_lager_hlut()

#búa til nýjan hlut á lagerhlutir
nyrLagHlut()

skrifaSkra()
#bætum því í listann
lagerhlutur.append(nyja)

#prenta út allar lagerhlutur
for x in lagerhlutur:
    x.pranta_lager_hlut()
    

#tal = int(input("hvaða lager viltu breyta ?"))
breytaHLut(tal,20,"box",150,890)

"""
#skrifaSkra()
#   x.append.prenta_lager_hlut()

