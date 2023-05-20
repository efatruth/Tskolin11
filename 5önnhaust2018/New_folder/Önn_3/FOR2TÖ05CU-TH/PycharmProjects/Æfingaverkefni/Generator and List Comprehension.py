#Along A. Loftsson

print("1.")
print()

def a_gen(length):
    n = 1
    for i in range(length):
        print("Nú hefur verið náð í mig í", n, "sinn.")
        yield n
        n += 1

how_many = int(input("Sláðu inn hversu mörgum sinnum þú vilt ná í generator: "))
for x in a_gen(how_many):
    print(x)

print()
print("2.")
print()

def second_gen(the_list):
    for i in the_list:
        yield i


how_many = int(input("Sláðu inn hvað listinn á að vera langur: "))
listi = []
for i in range(how_many):
    number = int(input("Sláðu inn tölu til að setja inn í lista: "))
    listi.append(number)

for x in second_gen(listi):
    print(x)

print()
print("3.")
print()

new_list = [x for x in range(1000) if x % 5 == 0 and x % 2 == 1]
print(new_list)