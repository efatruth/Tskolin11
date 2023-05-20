#Það þarf að import module sys til að geta náð
#í undantekningar/villur (exceptions)
import sys
"""
randomList = ['a', 0, 2]

for stak in randomList:
    try:
        print("Þetta stak er ", stak)
        r = 1/int(stak)
        break
    except:
        print("Oops! Þessi villa kom upp", sys.exc_info() [0])
        print("Næsta stak.")
        print()
print("Talan", stak, "deilt með einum er", r)

#######################################################################
a = 'b'
try:
    #Taktu Hashtaggið í burtu til þess að prufa allar þessar villur.
    #c=int(a)
    #d=23/0
    #f = open('myfile.txt')
    #4 + spam*3
    #'2' + 2
    pass

except ValueError:
    print("Oops! Vitlaus gagnatak", sys.exc_info())
    pass
except (ZeroDivisionError):
    print("Oops! bannað að deila með núlli",sys.exc_info())
except (TypeError):
    print("Get ekki lagt saman str og int", sys.exc_info())
    pass
except (NameError):
    print("Óskilgreind breyta",sys.exc_info())
    pass
except:
    print("Oops! Óvæn villa kom upp", sys.exc_info())
    pass
##################################################################

try:
    a = int(input("Sláðu inn plús tölu samt ekki stærri en hundrað: "))
    if a <= 0:
        raise ValueError("Þetta er ekki plústala!")
    if a > 100:
        raise ValueError("Þessi tala er stærri en 100!")
except ValueError as x:
    print(x)
###################################################################

try:
    f = open("test.txt", encoding = 'utf-8')
    x = f.readline()
    print(x)
    a = int(x)
    x = f.readline()
    print(x)
    a = int(x)
except:
    print("Eitthvað fór úrskeiðis", sys.exc_info())
finally:
    f.close()
print("Skránni hefur verið lokað.")
###################################################################
"""
