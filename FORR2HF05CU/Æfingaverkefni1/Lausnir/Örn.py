

from random import randint

# STRENGJARALLÝ
string = input("\nSláðu inn streng og ýttu á enter: ")
wordCount = string.count(" ")+1

print("\nFjöldi orða er: %d, Fyrstu 5 stafirnir eru: %s, Seinustu 4 stafirnir eru: %s"
      % (wordCount, string[:5], string[-4:]))

if len(string) % 2 == 0:
    print("\nEnginn stafur er í miðjunni :(")
else: print("\nMiðjustafurinn er: %s" % (string[int(len(string)/2)]))

for i in string:
    if i == "s" or i == "S":
        print("%s" % i, end="")
    else:
        print("*", end="")
print("\n")

# LISTARALLÝ
randomList = []
fortyList = []
for i in range(100):
    randomList.append(randint(34, 68))
randomList.sort()

print("\nMeðaltal listans er: %.02f" % (sum(randomList)/100))

print("\nStærsta talan er: %d, lægsta talan er: %d" % (max(randomList), min(randomList)))

print("\nSumman fyrir: %d" % sum(randomList))
while sum(randomList) > 4500:
    del randomList[-1]
print("Summan eftir: %d" % sum(randomList))

print("\nListinn fyrir: %s" % randomList)
#farið í gegnum listann byrjað aftast til að rugla ekki indexinu
for i in range(len(randomList)-1, 0, -1):
    if randomList[i] == 41:
        del randomList[i]
        fortyList.append(41)
print("Listinn eftir: %s" % randomList)
print("Fjögurtíulistinn: %s" % fortyList)

print("\nListinn fyrir: %s" % randomList)
for i in range(len(randomList)-1, 0, -1):
    if randomList[i] % 5 == 0:
        del randomList[i]
print("Listinn eftir: %s" % randomList)