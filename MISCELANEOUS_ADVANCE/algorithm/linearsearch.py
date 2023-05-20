def linear_search(l, n):
    length = len(l)
    x = 0
    for x in range(length):
        if l[x] == n:
            return x
    return -1

l = [1, 65, 43, 656, 76, 767, 10938, 4, 6]

print(linear_search(l, 1))
print(linear_search(l, 65))
print(linear_search(l, 76))
print(linear_search(l, 10938))
print(linear_search(l, 6))

while True:
    tala = int(input("Sláðu inn tölu til að finna: "))
    index = linear_search(l, tala)

    if index == -1:
        print("Talan", tala, "er ekki í listanum")

    else:
        print("Talan", tala, "er í sæti", index)
