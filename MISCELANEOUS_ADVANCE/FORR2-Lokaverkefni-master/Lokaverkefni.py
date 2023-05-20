# Helgi Tuan
# Pétur Steinn
# 23.11.17
# Lokaverkefni-FORR2

import random
import time


class nagdyr:   # Nagdýr búið til og gefið nafn, tegund, staðsetningu, afl
    def __init__(self, nafn, tegund, stadsetning, afl):
        self.nafn = nafn
        self.teg = tegund
        self.stad = stadsetning
        self.afl = afl

    def upplysingar(self):  # Hægt að nota þetta def til að prenta út stats á nagdýrunum
        return 'Nafn: ' + self.nafn + ' | Tegund: ' + self.teg + \
               ' | Staðsetninging: ' + \
            str(self.stad) + ' | Afl: ' + str(self.afl)


def drawPos():  # Prentar map á skjáinn með staðsetningunum á öllum nagdýrunum.
    reitir_nafn = list()
    reitir_map = list()
    for i in range(110):
        reitir_nafn.append(' ')
        reitir_map.append('_')

    reitir_end_mark = ' ' * 99 + '|'
    reitir_end = ' ' * 98 + 'END'
    # Hér replace-ar forritið stökum í listum út fyrir viðeigandi merkingu.
    try:
        reitir_map[mus.stad - 1] = bcolors.BLUE + \
            bcolors.UNDERLINE + "^" + bcolors.ENDC
        reitir_nafn[mus.stad - 1] = bcolors.BLUE + "M" + bcolors.ENDC
        reitir_map[rotta1.stad - 1] = bcolors.RED + \
            bcolors.UNDERLINE + "*" + bcolors.ENDC
        reitir_nafn[rotta1.stad - 1] = bcolors.RED + "R" + bcolors.ENDC
        reitir_map[rotta2.stad - 1] = bcolors.RED + \
            bcolors.UNDERLINE + "*" + bcolors.ENDC
        reitir_nafn[rotta2.stad - 1] = bcolors.RED + "R" + bcolors.ENDC
        reitir_map[rotta3.stad - 1] = bcolors.RED + \
            bcolors.UNDERLINE + "*" + bcolors.ENDC
        reitir_nafn[rotta3.stad - 1] = bcolors.RED + "R" + bcolors.ENDC
        reitir_map[hamstur.stad - 1] = bcolors.YELLOW + \
            bcolors.UNDERLINE + "O" + bcolors.ENDC
        reitir_nafn[hamstur.stad - 1] = bcolors.YELLOW + "H" + bcolors.ENDC
    except:
        pass
    print("Útkoma: ")
    print("W" * 110)
    # Prentar stats.
    print("Mús: ^ m/ staðs. " + str(mus.stad) + " | Rottur: * m/ staðs. (1: " + str(rotta1.stad) + ", 2: " +
          str(rotta2.stad) + ", 3: " + str(rotta3.stad) + ") | Hamstur: O m/ staðs. " + str(hamstur.stad) +
          " | Lota: " + str(round_counter))
    print()
    # Hér fer forritið í gegnum listana og prentar þá út.
    for i in reitir_nafn:
        print(i, end='')
    print()
    for i in reitir_map:
        print(i, end='')
    print()
    print(reitir_end_mark)
    print(reitir_end)
    print()
    print("M" * 110)


def header():  # Skilgreinir byrjun lotu.
    print()
    print()
    print()
    round_number_string = " Lota " + str(round_counter) + " "
    print("-" * 46 + " Ný lota " + "-" * 55)
    header_string_1 = "*" * \
        int(110 / 2 - len(round_number_string)) + round_number_string
    header_string_2 = "*" * int(110 - len(header_string_1))
    print(header_string_1 + header_string_2)


def footer():  # Skilgreinir lok lotu.
    print()
    print("*" * 110)
    print("-" * 110)


def resetMouse():  # Passar að músin fari ekki utan við reitina.
    if mus.stad <= 0:
        mus.stad = 1

def checkIfWon():
    global won
    if (mus.stad >= 100):  # Ef músin er komin yfir 100 reiti klárast leikurinn.
        won = True
    return won

def action(nagdyr):  # Þessi def tekur við hvaða nagdýri sem er og keyrir það á viðeigandi hátt
    global switchDirection  # Hægt er að nota þessa bool núna hvar sem er.
    global counter
    global difficulty
    # Þessi boolean breyta er til að sjá til þess að rotturnar klessa ekki á vegg og snúa þeim við þegar þær gera það
    # og meir að segja láta þær halda áfram með skrefin sem þau eiga eftir.
    switchDirection = False

    # Þessi def athugar hvort rottur séu nálægt mús og keyrir á viðeigandi hátt.
    def checkIfCombat():
        if abs(mus.stad - rotta1.stad) <= difficulty:  # Ef músin er nálægt rotta1 (innan við 3 reiti)
            print(mus.nafn + " er nálægt " + rotta1.nafn)
            if mus.afl < rotta1.afl:
                # Viðeigandi rotta slær músina aftur á bak.
                mus.stad -= rotta1.afl
                resetMouse()
                print(bcolors.RED + rotta1.nafn + " hendir músinni um " + str(rotta1.afl) +
                      " reiti, mús er nú á reit " + str(mus.stad) + bcolors.ENDC)
            elif mus.afl > rotta1.afl:  # Hér vinnur músin ef hún er með meira afl en rottan.
                print(bcolors.GREEN + mus.nafn + " sigrar " + rotta1.nafn +
                      " því hún er með meira afl" + bcolors.ENDC)

            else:   # Ef þær eru með jafn mikið afl, fer músin framhjá rottunni.
                print(bcolors.YELLOW + "Jafntefli á milli " +
                      mus.nafn + " og " + rotta1.nafn + bcolors.ENDC)

        elif abs(mus.stad - rotta2.stad) <= difficulty:  # Ef músin er nálægt rotta2 (innan við 3 reiti)
            print(mus.nafn + " er nálægt " + rotta2.nafn)
            if mus.afl < rotta2.afl:
                mus.stad -= rotta2.afl
                resetMouse()
                print(bcolors.RED + rotta2.nafn + " hendir músinni um " + str(rotta2.afl) +
                      " reiti, mús er nú á reit " + str(mus.stad) + bcolors.ENDC)

            elif mus.afl > rotta2.afl:
                print(bcolors.GREEN + mus.nafn + " sigrar " + rotta2.nafn +
                      " því hún er með meira afl" + bcolors.ENDC)

            else:
                print(bcolors.YELLOW + "Jafntefli á milli " +
                      mus.nafn + " og " + rotta2.nafn + bcolors.ENDC)
        elif abs(mus.stad - rotta3.stad) <= difficulty:  # Ef músin er nálægt rotta3 (innan við 3 reiti)
            print(mus.nafn + " er nálægt " + rotta3.nafn)
            if mus.afl < rotta3.afl:
                mus.stad -= rotta3.afl
                resetMouse()
                print(bcolors.RED + rotta3.nafn + " hendir músinni um " + str(rotta3.afl) +
                      " reiti, mús er nú á reit " + str(mus.stad) + bcolors.ENDC)

            elif mus.afl > rotta3.afl:
                print(bcolors.GREEN + mus.nafn + " sigrar " + rotta3.nafn +
                      " því hún er með meira afl" + bcolors.ENDC)

            else:
                print(bcolors.YELLOW + "Jafntefli á milli " +
                      mus.nafn + " og " + rotta3.nafn + bcolors.ENDC)

    # Kast einu sinni skilgreint fyrir eftirfarandi if lykkju.
    kast = random.randint(1, 6)
    # Kast er nýtt fyrir hvert nagdýr þó.
    if (nagdyr.teg == "mús"):   # If lykkja fyrir það ef kallað er í mús.
        counter += 1    # Telur hversu oft músin kastar.

        # Hvert skref fyrir sig er athugað og prentað út.
        print(nagdyr.nafn + " fer til hægri um " + str(abs(kast)) +
              " reiti og er staðsett núna á " + str(nagdyr.stad))

        for i in range(kast):
            print("Mús færir sig frá reit", nagdyr.stad, "yfir á reit ", end='')
            # Einu skrefi bætt við, aðein í eina átt fyrir músina.
            mus.stad += 1
            print(nagdyr.stad)
            # Við hvert skref fyrir sig er svo athugað hvort að rotta sé nálgæt.
            checkIfCombat()

            # Nú er athugað hvort að hamstur sé kominn til að henda músinni.
            if nagdyr.stad == hamstur.stad:
                print(bcolors.YELLOW + "Hamstur kastar mús um",
                      hamstur.afl, "reiti" + bcolors.ENDC)
                # Musinni er hent jafn marga reiti og afl hamstursins.
                mus.stad += hamstur.afl
            elif nagdyr.stad == 100:
                break   # Ef músin er kominn á reit 100, klárast leikurinn.

    elif (nagdyr.teg == "rotta"):   # If lykkja fyrir það ef kallað er í rottu.
        # fiddy ræður hvort rottan fer til hægri eða vinstri.
        fiddy = random.randint(0, 1)
        if fiddy == 0:  # Ef hún fer til vinstri.
            kast = kast - 7
            print(nagdyr.nafn + " fer til vinstri um " + str(abs(kast)) +  # Kast prentað.
                  " reiti og er staðsett núna á " + str(nagdyr.stad))

            for i in range(abs(kast)):  # Eitt skref í einu.
                if nagdyr.stad <= 1: nagdyr.stad = 1
                # Ef rottan er komin lengst til vinstri eða hún sé núþegar búin að skipta um stefnu.
                if nagdyr.stad <= 1 or switchDirection:
                    print(nagdyr.nafn + " færir sig frá reit",  # Hvert skref prentað út.
                          nagdyr.stad, "yfir á reit ", end='')
                    nagdyr.stad += 1
                    print(nagdyr.stad)
                    # Þessi bool skiptir ekki um stefnu í hvert sinn sem hún verður True,
                    switchDirection = True
                    # bara einu sinni og því er allt í lagi að hún verði aftur True.

                else:
                    print(nagdyr.nafn + " færir sig frá reit",
                          nagdyr.stad, "yfir á reit ", end='')
                    nagdyr.stad -= 1
                    print(nagdyr.stad)
                # Eftir hvert skref athugar forritið hvort mús sé nálægt.
                checkIfCombat()
        # Allt sama og þegar hún fer til vinstri.
        elif fiddy == 1:  # Ef hún fer til hægri
            print(nagdyr.nafn + " fer til hægri um " + str(abs(kast)) +  # Kast prentað.
                  " reiti og er staðsett núna á " + str(nagdyr.stad))
            for i in range(kast):
                if nagdyr.stad >= 100: nagdyr.stad = 100
                if nagdyr.stad >= 100 or switchDirection:
                    nagdyr.stad -= 1
                    switchDirection = True

                else:
                    print(nagdyr.nafn + " færir sig frá reit",
                          nagdyr.stad, "yfir á reit ", end='')
                    nagdyr.stad += 1
                    print(nagdyr.stad)
                checkIfCombat()

    # If lykkja fyrir það ef kallað er í hamstur.
    # Hamstur mun koma til með að elta músina hvert sem hún fer, rottur gera hamstrinum ekkert mein.
    elif (nagdyr.teg == "hamstur"):
        print(nagdyr.nafn + " færir sig um " + str(abs(kast)) +  # Kast prentað.
              " reiti og er staðsettur núna á " + str(nagdyr.stad))
        for i in range(kast):  # Forrit reiknar aðstæður við hvert skref.
            if nagdyr.stad >= 101 or nagdyr.stad <= 0: nagdyr.stad = random.randrange(
            2, 99)
            if mus.stad < hamstur.stad:
                print("Hamstur færir sig frá reit",
                      nagdyr.stad, "yfir á reit ", end='')
                hamstur.stad -= 1
                print(nagdyr.stad)
            elif mus.stad > hamstur.stad:
                print("Hamstur færir sig frá reit",
                      nagdyr.stad, "yfir á reit ", end='')
                hamstur.stad += 1
                print(nagdyr.stad)
            # Hér kastar hamsturinn músinni ef hann lendir á henni í því skrefi sem hann er í.
            elif mus.stad == hamstur.stad:
                print(bcolors.YELLOW + "Hamstur kastar mús um",
                      nagdyr.afl, "reiti" + bcolors.ENDC)
                mus.stad += hamstur.afl
        # Hér kastar hamsturinn músinni ef síðasta skrefið hanns lendir á músinni, hin elif lykkjan virkar ekki í það.
        if mus.stad == hamstur.stad:
            print(bcolors.YELLOW + "Hamstur kastar mús um",
                  nagdyr.afl, "reiti" + bcolors.ENDC)
            mus.stad += hamstur.afl

# Litir sem notast er við í forritinu.


class bcolors:
    PINK = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'      # Mús vinnur bardaga
    YELLOW = '\033[93m'     # Hamstur
    RED = '\033[91m'        # Rottur / mús tapar bardaga
    ENDC = '\033[0m'        # Reset
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Breytur
kast = 0
fiddy = 0
switchDirection = False
won = False
counter = 0
round_counter = 0
reitir = ''
timiMS = ''
difficulty = 1
construct_team = ''
val = True
val_afl = 0
val_stad = 0


# Hér byður forrit notanda um hversu hratt mappið á að birtast.
try:
    timiMS = int(input(
        "Hversu lengi á hver lota að vera í (milli sekúndum), default = 300ms (ýttu á enter fyrir default): "))
except:  # Ef ýtt er bara á enter keyrir hún forritið á 300ms
    timiMS = 300

# Hér velur notandi hvort hann vilji random stats á nagdýrunum eða velja sjálfur.
while True:
    construct_team = input("Viltu fá random stats á nagdýrin eða velja sjálfur (R/M): ").upper()
    if construct_team == 'R':
        print("Random mode")
        mus = nagdyr('Mús', 'mús', 1, random.randrange(2, 7, 2))
        rotta1 = nagdyr('Rotta1', 'rotta', random.randrange(
            2, 99), random.randrange(2, 7, 2))
        rotta2 = nagdyr('Rotta2', 'rotta', random.randrange(
            2, 99), random.randrange(2, 7, 2))
        rotta3 = nagdyr('Rotta3', 'rotta', random.randrange(
            2, 99), random.randrange(2, 7, 2))
        hamstur = nagdyr('Hamstur', 'hamstur', random.randrange(
            2, 99), random.randrange(3, 8, 2))
        break

    elif construct_team == 'M':
        print("Manual mode")
        print("Ef staðsetning nagdýranna er minna en 1 eða meira en 100 resetar forritið staðsetningarnar")
        val_afl = int(input("Afl mús: "))
        mus = nagdyr('Mús', 'mús', 1, val_afl)
        val_afl = int(input("Afl rottu 1: "))
        val_stad = int(input("Staðs. rottu 1: "))
        rotta1 = nagdyr('Rotta1', 'rotta', val_stad, val_afl)
        val_afl = int(input("Afl rottu 2: "))
        val_stad = int(input("Staðs rottu 2: "))
        rotta2 = nagdyr('Rotta2', 'rotta', val_stad, val_afl)
        val_afl = int(input("Afl rottu 3: "))
        val_stad = int(input("Staðs rottu 3: "))
        rotta3 = nagdyr('Rotta3', 'rotta', val_stad, val_afl)
        val_afl = int(input("Afl hamsturs: "))
        val_stad = int(input("Staðs hamsturs: "))
        hamstur = nagdyr('Hamstur', 'hamstur', val_stad, val_afl)
        break
    else:
        print(bcolors.RED + "Vitlaust valið" + bcolors.ENDC)

print()
print(mus.upplysingar())
print(rotta1.upplysingar())
print(rotta2.upplysingar())
print(rotta3.upplysingar())
print(hamstur.upplysingar())
print()

# Difficulty sett.
while True:
    difficulty = int(input("Difficulty (1 - 3) (mæli með 1): "))

    if difficulty >= 1 and difficulty <= 3:
        break
    else:
        print(bcolors.RED + "Vitlaust valið" + bcolors.ENDC)

print()
# Hér keyrir leikurinn
while won != True:
    checkIfWon()
    round_counter += 1  # Lotu-teljari
    header()
    print(mus.upplysingar())
    print(rotta1.upplysingar())
    print(rotta2.upplysingar())
    print(rotta3.upplysingar())
    print(hamstur.upplysingar())
    print()
    action(mus)
    checkIfWon()
    print()
    action(rotta1)
    checkIfWon()
    print()
    action(rotta2)
    checkIfWon()
    print()
    action(rotta3)
    checkIfWon()
    print()
    action(hamstur)
    checkIfWon()
    print()
    drawPos()
    footer()
    time.sleep(int(timiMS) / 1000)  # Forrit keyrir á þessum hraða.


print("Músin kastaði " + str(counter) + " sinnum.")
