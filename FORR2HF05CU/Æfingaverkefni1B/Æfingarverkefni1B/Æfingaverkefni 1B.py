from random import *
#Dæmi 1
dict1={}

#Bý til keys og values:
dict1['A'] = 'Api'
dict1['B'] = 'Banani'
dict1['C'] = 'Cookie'
dict1['D'] = 'Daníel'
dict1['E'] = 'Elías'
dict1['F'] = 'Friðrik'
dict1['G'] = 'Guðmundur'
dict1['H'] = 'Hávar'
dict1['I'] = 'Ingimar'
dict1['J'] = 'Jóhannes'
dict1['K'] = 'Kári'
dict1['L'] = 'Lárus'
dict1['M'] = 'Markús'
dict1['N'] = 'Nonni'
dict1['O'] = 'Orri'
print(dict1)

#Dæmi 2
for k, v in dict1.items(): #Loopar í gegnum öll keys (k) og values (v)
    print(k,"er fyrir",v) #Prentar út key og value key-sins

#Dæmi 3
print('\n' + dict1['E'])

#Dæmi 4
dict1['H'] = 'Heiðar' #Breytir value-inu sem er í 'H' í value-ið Heiðar

#Dæmi 5
print('\n' + str(dict1))

#Dæmi 6
del dict1['C'] #Eyðir key 'C' og value þess.


#Dæmi 7
print(dict1)

#Dæmi 8
dict1.popitem() #Popitem tekur alltaf fyrsta stakið sem BYRTIST en það er
#samt random því að dictionaryið sjálft er ekki raðað á neinn sérstakann hátt

#Dæmi 9
print(dict1)

#Dæmi 10
dict2 = dict1.copy() #dict2 er sama sem copy af dict1


#Dæmi 11

del dict1 #Eyðir dictionaryinu og öllu sem er í henni

#Dæmi 12
#þegar ég geri: "print("dict1", str(dict1))" Þá kemur: "name 'dict1' is not defined"
print("\nAfrit af dict1:")
print(dict2)

#Dæmi 13
dict3={}
for x in range(1,6):
    y=randint(1,100) #y er random tala frá 1 til 100
    dict3[x] = y #Býr til lykilinn x sem hefur value-ið y í dict3
print(dict3)

#Dæmi 14

#a
print("\nliður a:")
print(str(dict3.items())) #Sýnir öll items og values í dictionaryinu
#b
print("liður b:")
print(dict3.keys()) #Sýnir bara öll keys í dictionaryinu
if 1 in dict3.keys(): #Ef 1 er lykill í dict3
    print("1 er lykill í dict")
#c
print("liður c:")
print(dict3.values())
for x in range(0,50):
    if x in dict3.values(): #Ef x er value í dict3
        print(x, "er value í dict3")
#d
for x in range(1,70):
    if x in dict3.values(): #Ef x er value í dict 3
        dict3.clear() #Eyðir öllu úr dictionaryinu en dictionaryið er ennþá til
if len(dict3)==0: #Ef það er ekkert í dict3
    print("\ndict3 eftir að það er búið að clear-a hana:",dict3)
else:
    print("\ndict3 eftir að það er ekki búið að clear-a hana:", dict3)
