#Along A. Loftsson. 19.10.2017
#No time to comment :(
import random

def tölur(number): #Liður 1: Lambda
    list_number = list(filter(lambda x: (x % 5 == 0), range(number)))
    return list_number

def bingo_gen(a_list): #Liður 3 - Generator
    count = 0
    for i in a_list:
        count += 1
        if i == 5 or i == 12 or i == 54 or i == 67:
            string = ("Tala", count, "í listanum er:", i, "bingó tala.")
            yield string
        else:
            string = ("Tala", str(count), "í listanum er:", str(i))
            yield string


def digit_3(a_list): #Liður 4
    new_list = []
    three_list = [x for x in a_list if len(str(x)) > 2]
    three_list = [x for x in three_list if str(x)[2] == '3']
    return three_list


def addfunc(func): #Liður 6 - Veldi
    def power(number, power):
        newnumber = 0
        for i in range(power):
            newnumber += number * number
        answer = func(newnumber)
        return answer
    return power

@addfunc #Liður 6 - Decorator
def decoratefunc(number):
    new_string = "Fallið gefur töluna " + str(number)
    return new_string

print()
print("1.")
print()
numbers = 20
print(tölur(numbers))

print()
print("2.")
print()
"""
def minus_two(i): #Liður 2: Recursive #wtf
    if i > 1:
        for i in reversed(range(i)):
            x = i+10
            i -= 2
        return x
    else:
        return "Þarf að vera stærri en 1."


print(minus_two(2))
"""
print()
print("3.")
print()


how_many = int(input("Sláðu inn hvað listinn á að vera langur: "))
bingolist = []
for i in range(how_many):
    number = int(input("Sláðu inn tölu til að setja inn í lista: "))
    bingolist.append(number)

for x in bingo_gen(bingolist):
    print(x)

print()
print("4.")
print()

randomlistlol = [12, 123, 333, 324, 45]
print(digit_3(randomlistlol))

print()
print("5.")
print()

list1 = ["konni", "sponni", "sigga", "snorri"]
list2 = ["fótbolta", "handbolta", "blak"]

combined_list =[x+" er í "+y for x in list1 for y in random.sample(set((list2)), 1)]
print(combined_list)

print()
print("6.")
print()


the_number = int(input("Sláðu inn Tölu sem þú vilt setja í veldi: "))
the_power = int(input("Sláðu inn Tölu sem veldi: "))
print(decoratefunc(the_number, the_power))

