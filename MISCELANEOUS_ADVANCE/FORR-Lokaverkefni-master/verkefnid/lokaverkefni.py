'''
Lokaverkefni
Róbert og Knútur
'''
import random
class Nagdyr:
    def __init__(self, tegund, stadsetning, afl):
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl
    def upp(self):
        return self.teg , str(self.stad) , str(self.afl) 
    
class border:
    def endir(self):
        print("W"*80)
        print("><><><><><><><><> Niður staða <><><><><><><><><")
        print("-----------------------------------------------")
        print("Umferðir = "+ str(teljari))
        print("-----------------------------------------------")

 
    def byrjun(self):
        print("W"*81)
        print("><><"*8 +" leikur " + str(teljari) + " ><><"*8)
 
    def fotur(self):
        print("W"*81)
            

def kast(tegund):
    if tegund.teg == "Mús":
        kast = random.randint(1,6)
        print(tegund.teg +" kastar og fær"+ str(kast) + " og er á reit " + str(tegund.stad) + " afl hennar er " + str(tegund.afl))
        for x in range (abs(kast)):
            mus.stad +=1
            print (str(tegund.teg) + " er á " + str(tegund.stad))
            dyrstoppar = berjast(tegund)
            if dyrstoppar:
                break
    if tegund.teg == "Rotta" or tegund.teg == "Rotta_2" or tegund.teg == "Rotta_3":
        kast = random.randint(1,6)
        #hvort rottan fer upp eða niður
        #1= upp 0=niður
        val= random.randint(0,1)
        breytastodu = False
        breytastodunidur = False
        print(tegund.teg +" kastar og fær"+ str(kast) + " og er á reit " + str(tegund.stad) +"valið er"+str(val)+ " afl hennar er " + str(tegund.afl))
        for x in range(abs(kast)):
            if tegund.stad <= 1 or breytastodu:
                breytastodu = True
                tegund.stad +=1
            elif tegund.stad >= 99 or breytastodunidur:
                breytastodunidur = True
                tegund.stad -=1
            elif val == 1:
                tegund.stad +=1
            elif val == 0:
                tegund.stad -=1
            dyrstoppar = berjast(tegund)
            print (str(tegund.teg) + " er á " + str(tegund.stad))
            if dyrstoppar:
                 break
        if tegund.stad == hamstur.stad:
                hamstur.stad += 1
                print("hamstur og rotta lenda saman hamstur fer einn áfarma")
                    
    if tegund.teg == "Hamstur":
        kast = random.randint(1,6)
        print(tegund.teg +" kastar og fær"+ str(kast) + " og er á reit " + str(tegund.stad) + " afl hennar er " + str(tegund.afl))
        for x in range(abs(kast)):
            if mus.stad > hamstur.stad:
                hamstur.stad += 1
            else:
                hamstur.stad -= 1
            print (str(tegund.teg) + " er á " + str(tegund.stad))
            dyrstoppar = berjast(tegund)
            if dyrstoppar:
                break
        # ef hamstur lendir á sama reit og rottur
        for x in rottur: 
            if tegund.stad == x.stad:
                hamstur.stad += 1
                print("hamstur og rotta lenda saman hamstur fer einn áfarma")
game = 0
border = border()
teljari = 1
rottur = list() 

mus = Nagdyr("Mús",1,random.randrange(2,7,2))
rotta = Nagdyr("Rotta",random.randrange(2,100,),random.randrange(2,7,2))
rotta2 = Nagdyr("Rotta_2",random.randrange(2,100,),random.randrange(2,7,2))
rotta3 = Nagdyr("Rotta_3",random.randrange(2,100,),random.randrange(2,7,2))
hamstur = Nagdyr("Hamstur",random.randrange(2,100,),random.randrange(3,8,2))

print(mus.stad)
print(rotta.stad)
print(rotta2.stad)
print(rotta3.stad)
print(hamstur.stad)
rottur.append(rotta)
rottur.append(rotta2)
rottur.append(rotta3)



def berjast(tegund):
    ret_dyrstoppar = False
    #mús kastar
    if tegund.teg == "Mús":
        for x in rottur:#allar rottur í lista
            if mus.stad == x.stad:
                ret_dyrstoppar = True
                if mus.afl > x.afl:
                    x.stad -=mus.afl
                    print("mus vann", str(x.teg)," og rottan er á reit",str(x.stad))
                else:
                    mus.stad -=x.afl
                    print("mus tapaði fyrir "+ x.teg+ " og fer " + str(x.afl)+" reiti aftur á bak og er á reit "+ str(mus.stad))
        if mus.stad == hamstur.stad:
            mus.stad += hamstur.afl
            print("Hamstur kastar mús um "+ str(hamstur.afl) +" reiti, mus er á reiti "+ str(mus.stad))
    #rottur kasta
    if tegund.teg == "Rotta" or tegund.teg == "Rotta_2" or tegund.teg == "Rotta_3":
        for x in rottur:
            if x.stad == mus.stad:
                ret_dyrstoppar = True
                if x.afl > mus.afl:
                    mus.stad -= mus.afl
                    if mus.stad <= 0:
                        mus.stad = 1
                    print("rotta vann mus")
                else:
                    x.stad -= mus.afl
    #hamstur lendir mús
    if tegund.teg == "Hamstur":
        if hamstur.stad == mus.stad:
            mus.stad += hamstur.afl
            print("hamstur kastar mús um "+ str(hamstur.afl) +" reiti")
            ret_dyrstoppar = True
        if hamstur.stad <= 1:
            hamstur.stad =1
        if hamstur.stad >=100:
            hamstur.stad = 99
        return ret_dyrstoppar
def puntar():
    puntar= list()
    for x in range(110):
        puntar.append("*")
    puntar[mus.stad]="M"
    puntar[rotta.stad]="R"
    puntar[rotta2.stad]="R"
    puntar[rotta3.stad]="R"
    puntar[hamstur.stad]="H"
    puntar[100]= "E"
    #prenta ut
    for x in puntar:
        print(x, end="")
    
        
    
while game != "buinn":
    border.byrjun()
    dyrstoppar = False
    print("")
    kast(mus)
    print("")
    dyrstoppar = False
    for x in rottur:
        kast(x)
    if rotta.stad == rotta2.stad:
        rotta.stad +=1
    if rotta3.stad == rotta2.stad:
        rotta3.stad +=1
    if rotta3.stad == rotta2.stad:
        rotta2.stad +=1
    dyrstoppar = False
    teljari += 1
    print("")
    kast(hamstur)
    print("")
    puntar()
    print("")
    border.fotur()
    print("")
    print("")
    
    



    if mus.stad >= 100:
        game = "buinn"
        print("Músin vann")
        border.endir()

    
