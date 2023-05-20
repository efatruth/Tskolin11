
#Along A. Loftsson 12.09.2017
import skil2_foll

#------------------~ 1 ~--------------------
x = 1
while x == 1:
    side1 = float(input("Sláðu inn hlið 1: "))
    if side1 >= 0:
        side2 = float(input("Sláðu inn hlið 2: "))
        hypotenuse = skil2_foll.find_hypotenuse(side1, side2)
        print("Langhliðin er", hypotenuse)
        print("Sláðu inn mínustölu sem hlið 1 til þess að hætta.")
        print()
    else:
        x = 0
        print("Forritið er hætt.")
        print()
else:
    pass #Þarf að bæta við ValueError

#------------------~ 2 ~--------------------
x = 2
while x == 2:
    division1 = int(input("Sláðu inn fyrri töluna: "))
    if division1 != 0:
        division2 = int(input("Sláðu inn seinni töluna: "))
        multiplied = skil2_foll.multiply_of(division1, division2)
        if multiplied == True:
            print(division2, "er margfeldi af", division1)

        else:
            print(division2, "er ekki margfeldi af", division1)

    else:
        print("Forritið er hætt.")
        print()
        x = 0

else:
    pass

#------------------~ 3 ~--------------------

x = 3
if x == 3:
    star = int(input("Sláðu inn hvað stórt stjörnukassinn á að vera: "))
    starbox = skil2_foll.box_of_stars(star)
    for star in starbox:
        print(starbox)
    print()
    x = 0

#------------------~ 4 ~--------------------

x = 4
while x == 4:
    try:
        findnumber = int(input("Sláðu inn tölu: "))
        even_odd = skil2_foll.is_even(findnumber)
        if even_odd == True:
            print(findnumber, "er slétt tala.")
            print()
        else:
            print(findnumber, "er odda tala.")
            print()

    except ValueError:
        print("Þú hefur ekki slegið inn heilatölu.")
        print()
#------------------~ 5 ~--------------------


