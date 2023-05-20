#("----------fall fyrir 3--------------")

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
    elif name != username:











