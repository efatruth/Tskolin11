import sys
print("1.")
print()
number_list = []

print("Sláðu inn 10 heiltölur")
while len(number_list) != 10:
    try:
        x = int(input("Sláðu inn heiltölu: "))
        number_list.append(x)
    except ValueError:
        print("Þetta er ekki integer.")
else:
    pass
print()
print("2.")
print()

a = 'b'
val = 0
while val != 6:
    print("1. c = int(a)")
    print("2. d = 3/0")
    print("3. e =open('myfile.txt')")
    print("4. f = 6 + eitthv*3")
    print("5. g ='2' + 2")
    print("6. Exit")
    val = int(input("Sláðu inn númer: "))
    try:
        if val == 1:
            c = int(a)
        elif val == 2:
            d = 3/0
        elif val == 3:
            e =open('myfile.txt')
        elif val == 4:
            f = 6 + eitthv*3
        elif val == 5:
            g ='2' + 2
        elif val == 6:
            pass
        pass
    except ValueError:
        print("Þetta er vitlaust gagnatak.", sys.exc_info())
        print()
        pass
    except ZeroDivisionError:
        print("Ekki er hægt að deila með núlli.", sys.exc_info())
        print()
        pass
    except TypeError:
        print("Ekki er hægt að leggja saman str. og int.", sys.exc_info())
        print()
        pass
    except NameError:
        print("Óskilgreind breyta.", sys.exc_info())
        print()
        pass
    except:
        print("Óvæn villa kom upp", sys.exc_info())
        print()
        pass

else:
    print("Takk")
print()