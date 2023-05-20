#livinus felix bassey
#Skilaverkefni#
#10.09.2018

import csv
from minir_klasar import *
import sys

lagerhlutir = []
def opnaSkra():
    lager = []
    with open('lagerhlutir.csv', 'r', newline='',encoding='utf-8') as file:
         reader = csv.reader(file, delimiter=';')
         id=0
         for row in reader:
             hlutur = Lager_hlutur(row[0],row[1],int(row[2]),int(row[3]))
             lager.append(hlutur)
    return lager

lagerhlutir= opnaSkra()
heildav = 0
for x in lagerhlutir:
    x.prenta_lager_hlut()



def skrifaSkra():#Skrifar í skrána.
    lagerhlutir= opnaSkra()
    heildav = 0
    for x in lagerhlutir:
        x.prenta_lager_hlut()

def nyrLagerhlutur():#bætir inn nýju tilviki(object,hluti)
   persons = []
   with open('lagerhlutir.csv', 'r') as f:
       reader = csv.reader(f)
       for row in reader:
           persons.append({'name': row[0], 'age': int(row[1]),'hobbies': row[2:]})

def eydaLagerhlut():#eyðir tilviki(object,hluti)
    reader = csv.reader(open('lagerhlutir.csv'))
    for rows in lagerhlutir:
        rows[0].strip()
        return rows


def breytaLagerhlut():#breytir tilviki(object,hluti)
    reader = csv.reader(open('lagerhlutir.csv'))
    for rows in lagerhlutir:
        rows[0].strip().split(',')
        return rows


def prentaLager():#skrifar á skjáinn allt sem er í skránni(innhald listans af tilvikum)
    listi = 0
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




