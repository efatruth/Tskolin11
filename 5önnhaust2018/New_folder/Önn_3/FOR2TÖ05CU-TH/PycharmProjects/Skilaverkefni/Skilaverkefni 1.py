#Along A. Loftsson. 24.08.2017 (Skilaverkefni 1).

print("1.")
print()

phonenumber = { 'Albert' : '7775910', 'John' : '8695432', 'Alma' : '8785486', 'Kalli' : '9895467', 'Fannar' : '8759867',
                'Tara': '7974768', 'Sigmundur' : '8986784', 'Ingimundur' : '7767489', 'Elsa' : '6684201',
                'Helgi' : '7746847',}
#---------------Biðja um símanúmer eftir nafni---------------
print(phonenumber)
print()
choose = input("Sláðu inn nafn fyrir símanúmer: ")
random_value = 1 #Þetta er value sem ég mun nota til að halda lykkjum o.fl.

for i in phonenumber: #Fer í gegnum listann og skoða hvort símanúmerið er í dictionary
    if choose.lower() == i.lower():
        print("Símanúmerið hjá", i, "er", phonenumber.get(i))
        random_value = 0
        print()

if random_value == 1: #Þetta kemur ef nafnið er í skránni
    print("Þetta nafn er ekki til í skránni")
    print()
#---------------Bæta við nafni og númeri---------------
print("Núna máttu bæta við notanda í skránna.")
add_name = input("Sláðu inn nafn: ")
add_number = input("Sláðu inn númer: ")

while len(add_number) != 7 or add_number.isnumeric() == False: #Númer eru venjulega með 7 tölustafi.
    print("Þetta er ekki 7-stafa númer. Reyndu aftur.")
    add_number = input("Sláðu inn númer: ")
else:
    pass

phonenumber.update({add_name.capitalize():add_number})
print("Nafn og símanúmer hefur verið bætt.")
print(phonenumber)
print()
#---------------Henda út nafn/símanúmer---------------
random_value = 0 #Hérna er random_value notað aftur.
while random_value == 0:
    del_number = input("Sláðu inn nafn notanda sem á að vera hent út úr skránni: ")
    for i in phonenumber:
        if del_number.lower() == i.lower():
            random_value = 1
    if random_value == 0:
        print("Þetta nafn er ekki til, reyndu aftur.")
else:
    phonenumber.pop(del_number.capitalize())
    print("Símanúmerið hefur verið hent út.")
print(phonenumber)
print()
#---------------Breyta símanúmeri---------------
random_value = 0
while random_value == 0:
    change_number = input("Sláðu inn nafn hjá honum sem þú vilt breyta: ")
    for i in phonenumber:
        if change_number.lower() == i.lower(): #Er notað til að sjá hvort nafnið er í listanum.
            random_value = 1
    if random_value == 0:
        print("Þetta nafn er ekki til, reyndu aftur.")
else:
    pass

new_number = input("Sláðu inn nýja númerið: ")

while len(new_number) != 7 or new_number.isnumeric() == False:
    print("Þetta er ekki 7-stafa númer. Reyndu aftur.")
    new_number = input("Sláðu inn nýja númerið: ")
else:
    pass

phonenumber.update({change_number.capitalize():new_number}) #Hér er breytt númerinu.
print("Símanúmerið hefur verið breytt.")
print(phonenumber)
print()

print("2.")
print()

group_for = []
group_gso = []
counting_class = int(input("Hvað eru margir nemendur í FOR1TÖ05CU? "))
print("Sláðu inn nöfn þeirra.")

for i in range(counting_class):
    name = input("Sláðu inn nafn: ")
    group_for.append(name)
print()

counting_class = int(input("Hvað eru margir nemendur í GSÖ1TÖ05AU? "))
print("Sláðu inn nöfn þeirra.")

for x in range(counting_class):
    name = input("Sláðu inn nafn: ")
    group_gso.append(name)

group_for = sorted(group_for) #Hér er hóparnir sortaðir eftir stafrófsröð.
group_gso = sorted(group_gso)
print()
print("Listarnir eru sort raðaðir í stafrófsröð.")
print(group_for)
print()
print(group_gso)
print()
#---------------Birta þá sem eru í báðum áföngum---------------
print("Þeir sem eru í báðum áföngum verða birtir hér fyrir neðan.")
for i in group_for:
    for x in group_gso:
        if i == x: #Hér er gáð hvort einhver er í báðum áföngum.
            print(i)
print()
#---------------Skrifa út hvor hópur er stærri---------------
if len(group_for) < len(group_gso): #If-lykkja sem sér hvor hópur er stærri.
    print("Stærri hópurinn er GSÖ með", len(group_gso), "á móti", len(group_for))
elif len(group_for) == len(group_gso):
    print("Hóparnir eru jafnstórir með", len(group_for))
else:
    print("Stærri hópurinn er FOR með", len(group_for), "á móti", len(group_gso))
print()
#---------------Færa tvo öftustu nemendurna úr FOR yfir í GSÖ---------------
group_gso.append(group_for[-1])
group_for.pop() #Tveir öftustu nemendur færðir með því að nota append og svo henda þeim í fyrri hópnum með pop().
group_gso.append(group_for[-1])
group_for.pop()
group_gso = sorted(group_gso)
print("Öftustu tveir í FOR hafa verið færðir yfir á GSÖ. Svona eru bekkirnir núna:")
print(group_for)
print(group_gso)
print()

print("3.")
print()


open_file = open("lykilord.txt", "r", encoding="utf-8")
read_file = open_file.read()
split_file = read_file.split('\n')

accounts = [] #Hér er lesið úr skrá og splittað.
for i in split_file:
    users = i.split(";")
    accounts.append(users) #Svo bætt inn í lista.

for i in accounts:
    print(i)

log_name = input("Sláðu inn notandanafn (EKKI CASE SENSITIVE): ")
log_pass = input("Sláðu inn lykilorð (CASE SENSITIVE): ") #Lykilorð eru venjulega case sensitive.

login = list((log_name.capitalize(), log_pass)) #Hér er sett í lista svo að er hægt að bera saman við notanda-listann.

for i, x in accounts: #If-lykkja in í for-lykkju til þess að sjá hvort lykilorð og notandanafnið passar.
    if login[0] == i and login[1] == x:
        print("VELKOMINN.")
        break
    elif login[0] == i and login[1] != x or login[0] != i and login[1] == x:
        print("RANGT.")
        break
else:
    print("EKKI TIL.")
print()
print("4")
print()

text = input("Sláðu inn streng/nafn: ")
newstring = ''
fixedstring = '' #Newstring er fyrir orðið þegar er búið að víxla því, fixedstring er til þess að snúa því venjulega.
v1 = 0
v2 = 2
if len(text) % 2 != 0: #Ef talan er ekki slétt tala verður síðastur stafurinn ekki víxlaður.
    length = int((len(text)-1)/2) #Er lengdin á textanum.
    for i in range(length): #v1 og v2 eru notuð sem breytur sem víxlar stöfunum og setur þá í newstring.
        temp = text[v1:v2]
        newstring += temp[1] + temp[0]
        v1 += 2 #Breyturnar fara upp um tvo til þess að velja næsta stafi í orðinu.
        v2 += 2
    newstring += text[-1]
    print("strengurinn er svona núna:",newstring.upper())

else: #Sama gerist hér nema að núna eru tölurnar sléttar þannig að allir bókstafir verða víxlaðir.
    length = int(len(text)/2)
    for i in range(length):
        temp = text[v1:v2]
        newstring += temp[1] + temp[0]
        v1 += 2
        v2 += 2
    print("strengurinn er svona núna", newstring.upper())
#Hérna er víxlað stafaruglinu aftur til baka, var ekki viss hvað að afkóða þýddi, þannig að ég held að þetta sé það.
v1 = 0
v2 = 2
if len(newstring) % 2 != 0: #Newstring er notað sem lengd, og nýja orðið er sétt í fixedstring breytuna í staðinn.
    length = int((len(newstring) - 1) / 2)
    for i in range(length):
        temp = newstring[v1:v2]
        fixedstring += temp[1] + temp[0]
        v1 += 2
        v2 += 2
    fixedstring += newstring[-1]
    print("strengurinn aftur eins og hann var:", fixedstring.upper())

else:
    length = int(len(newstring) / 2)
    for i in range(length):
        temp = newstring[v1:v2]
        fixedstring += temp[1] + temp[0]
        v1 += 2
        v2 += 2
    print("Strengurinn aftur eins og hann var:", fixedstring.upper())