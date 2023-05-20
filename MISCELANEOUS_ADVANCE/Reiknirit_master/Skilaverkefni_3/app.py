import string
from itertools import combinations
from time import perf_counter

startTime = perf_counter()

def hanoi(n, A, B, C):
    if n == 1:
        print("Færa disk %s frá %s til %s" %(n, A, B))
    else:
        hanoi(n - 1, A, C, B)
        print("Færa disk %s frá %s til %s" % (n, A, B))
        hanoi(n - 1, C, B, A)

def allAlphabetStrings(n):
    allLowercaseLetters = list(string.ascii_lowercase)
    allCombinedStrings = list(combinations(allLowercaseLetters, n))
    for i in range(len(allCombinedStrings)):
        print("".join(allCombinedStrings[i]))

def listAlphabetStrings(n):
    combinedStringsNormal = []
    allLowercaseLetters = list(string.ascii_lowercase)
    allCombinedStrings = list(combinations(allLowercaseLetters, n))
    for i in range(len(allCombinedStrings)):
        combinedStringsNormal.append("".join(allCombinedStrings[i]))
    combinedStringsReversed = combinedStringsNormal[::-1]

    print("NOT REVERSED")
    print(combinedStringsNormal)

    print()
    print("REVERSED")
    print(combinedStringsReversed)


print()
print("Dæmi 1")
hanoi(2, "A", "B", "C")

print()
print("Dæmi 4")
allAlphabetStrings(2)

print()
print("Dæmi 5")
listAlphabetStrings(2)

