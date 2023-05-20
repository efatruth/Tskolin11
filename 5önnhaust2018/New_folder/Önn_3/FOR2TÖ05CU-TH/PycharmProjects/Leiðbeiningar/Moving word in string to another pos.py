print()
strengurinn = ("Það er gaman að forrita í áfanganum FOR1TÖ05AU")
replace = 2
words = strengurinn.split()
oldpos = words.index("gaman")
words.insert(oldpos+3, words.pop(oldpos))
"".join(words)

#Take 1 word out of string and appending
print(strengurinn)
print(" ".join(words))
print(strengurinn.upper())
