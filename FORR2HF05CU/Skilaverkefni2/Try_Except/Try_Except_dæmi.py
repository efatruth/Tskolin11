import sys
""" 
listi = []
teljari = 0
while teljari < 10:
    try:
        tala = int(input("slaðu inn  tölu"))
        listi.append(tala)
        teljari = teljari +1
    except ValueError:
        print("það þarf að slá inn tölu")

print(listi)
"""
try:
    tala = int(input("sladu inn tölu" ))
except ValueError:
    print ("það þarf að slá inn tölu")

try:
    utkoma = 25/0
    print(utkoma)
except ZeroDivisionError:
    print(sys.exc_info())
