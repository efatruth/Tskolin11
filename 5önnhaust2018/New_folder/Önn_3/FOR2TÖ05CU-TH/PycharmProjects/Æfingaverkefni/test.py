#Along A. Loftsson 21.09.2017
import random
def gisk_tala(): #Notað til að fá einhverja slembi-tölu.
    randomtala = random.randrange(1,1001)
    return randomtala

def skoda_gisk(t1, t2): #Tekur inn slembi-töluna og giskið til að gá hvort er sama talan.
    high = False
    low = False
    if t1 == t2:
        return True
    else:
        if t1 > t2:
            high = True
            low = False
            return False
        else:
            high = False
            low = True
            return False

gisk = 1 #Notað fyrir bæði að giska og fyrir að slökkva á forritinu.
while gisk != 0:
    loop = True #Þetta er fyrir hverja umferð þangað til þú færð rétt eða hættir.
    slembitala = gisk_tala()
    while loop == True:
        try:
            gisk = int(input("Giskaðu (0 til að hætta): ")) #Lætur forritið hætta.
            if gisk == 0:
                loop = 0
                pass

            elif skoda_gisk(gisk, slembitala) == True: #Fær réttu tölu.
                print("Rétt hjá þér! Þú fannst töluna!")
                print()
                loop = False

            elif skoda_gisk(gisk, slembitala) == False: #Ekki rétt tala.
                if  low == True: #Kíkir svo hvort þessi tala sé eins lág eða ekki.
                    print("Of lág. Reyndu aftur.")

                elif high == True: #Sama hér, nema hér er há tala.
                    print("Of há. Reyndu aftur.")

        except ValueError:
            print("Þetta er ekki tala.")
else:
    print("Takk fyrir að spila.")

