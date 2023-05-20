def setja_inn_lista(listi, tala):
    if not listi: # Ef listinn er tómur
        listi.insert(0, tala)
        return True
    elif listi[-1] == tala or tala > listi[-1]: # Ef seinasta talan í listanum er jafnstór eða minni en talan
        listi.insert(len(listi), tala)
        return True
    elif tala <= listi[0]: # Ef fyrsta stak listans er minni eða í jafnt og talan
        listi.insert(0, tala)
        return True
    else:
        for i in range(len(listi)):
            if listi[i] <= tala and tala < listi[i+1]:
                listi.insert(i+1, tala)
                return True
    return False

listi = [2, 3, 3, 5, 6, 7, 9, 10]
tala = int(input("Sláðu inn tölu til að setja inn: "))

print(setja_inn_lista(listi, tala))
print(listi)
