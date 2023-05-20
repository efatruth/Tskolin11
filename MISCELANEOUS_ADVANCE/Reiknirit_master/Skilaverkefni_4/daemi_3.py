def binary_search(listi, byrjunar_stadur, lengd_listi, tala):
    if lengd_listi >= byrjunar_stadur:

        midjan = int(byrjunar_stadur + (lengd_listi-1)/2)

        if listi[midjan] == tala:
            return midjan

        elif listi[midjan] > tala:
            return binary_search(listi, byrjunar_stadur, midjan-1, tala)

        else:
            return binary_search(listi, midjan+1, lengd_listi, tala)

    else:
        return -1

listi = [1, 2, 3, 5, 6, 7, 8, 9] 
tala = int(input("Sláðu inn tölu til að finna: "))
index = binary_search(listi, 0, len(listi)-1, tala) 
  
if index == -1:
    print("Talan", tala, "er ekki í listanum")
else:
    print("Talan", tala, "er í sæti", index)
