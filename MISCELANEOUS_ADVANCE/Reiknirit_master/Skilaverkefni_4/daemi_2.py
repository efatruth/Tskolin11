def linear_search(listi, tala):
    for i in range(0, len(listi)):
        if listi[i] == tala:
            return i
    return -1

listi = [8, 5, 3, 7 , 1, 9, 2, 6]
tala = int(input("Sláðu inn tölu til að finna: "))
index = linear_search(listi, tala)

if index == -1:
    print("Talan", tala, "er ekki í listanum")
else:
    print("Talan", tala, "er í sæti", index)
