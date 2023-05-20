'''
Conversation opened. 1 unread message.

Skip to content
Using Gmail with screen readers
Click here to enable desktop notifications for Gmail.   Learn more  Hide

  More 
1 of 35
 
Upprifjun 1 og aefingaverkefni 2 
Inbox
x 

Daniel Arnarsson <danielarnarsson@gmail.com>
Attachments3:50 PM (42 minutes ago)
to me 

3 Attachments
	
Click here to Reply or Forward
2.12 GB (14%) of 15 GB used
Manage
Terms · Privacy · Program Policies
Last account activity: 0 minutes ago
Details
	
Gmail is getting an update
In less than 1 week, Gmail will get an updated look and new features like Snooze. You can still go back to classic. Learn more
''' 
from random import *
#-----Strengjarallý-----#


#Skrifið inn streng.
strengur="Hallo eg heiti Strúturs"
print(strengur)

#Fjöldi orða:
fjoldiOrda=len(strengur.split())
print("\nFjöldi orða í strengnum: ", fjoldiOrda)

#Fyrstu 5 stafirnir:
first_5_char=strengur[:5]
print("\nFyrstu 5 stafir: "+first_5_char)

#Síðustu 4 stafirnir:
last_4_char=strengur[-4:]
print("\nSíðustu 4 stafir: "+last_4_char)

#Miðjustafurinn í setningunni:
lengdstrengs=len(strengur)
if lengdstrengs/2==int:
    print("\nÞað er enginn miðjustafur í strengnum því lengd hans er slétt tala")
else:
    midjustafur=lengdstrengs/2-0.5
    midjustafur=int(midjustafur)
    print("\nStafurinn í miðjunni er: "+strengur[midjustafur])

#Öll s/S í textanum:
finnaStafi=""
for x in strengur:
    if x=="S" or x=="s":
        finnaStafi+=str(x)
    elif x==" ":
        finnaStafi+=str(" ")
    elif x!="s" or x!="S":
        finnaStafi+=str("#")
print("\n" + finnaStafi)
        
#-----Listarallý-----#


#Búið til random lista...:
randomlisti=[]
for x in range(100):
    randomtala=randrange(34,69)
    randomlisti.append(randomtala)
print("\nListi með random númerum frá 34 til og með 68:")
print(randomlisti)

#Raðið listanum:
randomlisti.sort()
print("\nraðaður listi: ")
print(randomlisti)

#Finnið stærstu og minnstu töluna...:
print(round(sum(randomlisti)/len(randomlisti),2))
print("\nStærsta talan í listanum er:", max(randomlisti))
print("\nMinnsta talan í listanum er:", min(randomlisti))

#Ef summa talnanna í listanum...:

print()
while sum(randomlisti) > 4500:
    randomlisti.pop(0)
print("Listinn eftir að summa hans hefur verið gerð minni en 4500:")
print(randomlisti)

#Hendið út öllum tölum sem ganga upp í 5:
y=len(randomlisti)
x=1
for x in range(0,y):
    if randomlisti[x] % 5==0:
        del(randomlisti[x]) #Hendir öllum tölum úr listanum sem ganga upp í 5
print("Listinn eftir að búið er að fjarlægja allar tölur sem ganga upp í 5:")
print(randomlisti)
#Setjið töluna 40 í sér lista:
print()
listiMed40=[]
i = randomlisti.count(40)
print(randomlisti)
print()
for x in range(i):
    listiMed40.append(40)
    randomlisti.remove(40)
print(randomlisti)
print()
print(listiMed40)
    
'''
upprifjun.py
Displaying upprifjun.py.
'''
