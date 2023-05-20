#Along A. Loftsson 21.09.2017
import random

def kasta_pening():
    throw = random.randint(1,2) #Fæ annaðhvort 1 eða 2
    if throw == 1:
        return True #Verður True fyrir skjaldarmerki og False fyrir loðnu
    elif throw == 2:
        return False

loop = True #Loop breyta til að keyra loop-una
skjald = 0
lodna = 0
while loop == True:
    try:
        print("1. Kasta pening.")
        print("2. Hætta.")
        choose = int(input("Hvað viltu gera? "))
        print()
        if choose == 1:
            if kasta_pening() == True: #Leitar í fallið hvor hlið kemur.
                skjald += 1
                print("Skjaldarmerki:", skjald, "Loðna:", lodna)
                print()

            else: #Bætir svo einn á og heldur áfram
                lodna += 1
                print("Skjaldarmerki:", skjald, "Loðna:", lodna)
                print()

        elif choose == 2: #Hættir á loop-uni.
            loop = False
            print("Takk fyrir.")

        else: #Er notað ef einhver reynir að velja annað en 1. og 2.
            print("Þú verður að velja tölu 1 eða 2.")
            print()

    except ValueError: #Ef einhver velur bókstaf í staðinn.
        print()
        print("Þetta er ekki tala, reyndu aftur.")
        print()
