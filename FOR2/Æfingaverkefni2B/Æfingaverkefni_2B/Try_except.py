#Það þarf að import module sys til að geta náð
#í undantekningar/villur (exceptions)
import sys
randomList=['a', 0, 2]

for stak in randomList:
    try:
        print("Þetta stak er ", stak)
        r= 1/int(stak)
        break
    except:
        print("Oops! þessi villa kom upp",sys.exc_info()[0])
        print("Næsta stak.")
        print()
print("Talan",stak,"deilt með einum er",r)




a='b'
try:
    c=int(a)
    #d=23/0
    #f=open('myfile.txt')
    #4+spam*3
    #'2' + 2
    pass

except ValueError:
    print("Oops!vitlaust gagnatak",sys.exc_info())
    pass
except (ZeroDivisionError):
    print("Oops!Bannað að deila með núlli",sys.exc_info())
    pass
except (TypeError):
    print("Get ekki lagt saman str og int",sys.exc_info())
except (NameError):
    print("óskligreind breyta",sys.exc_info())
    pass
except:
    print("Oops! óvænt villa kom upp",sys.exc_info())
    pass




try:
    a=int(input("Sláðu inn plús tölu samt ekki stærri en hundrað"))
    if a <= 0:
        raise ValueError("Þetta er ekki plústala!")
    if a>100:
        raise ValueError("Þessi tala er stærri en 100")
except ValueError as x:
    print(x)




try:
    f = open("test.txt", encoding='utf-8')
    x = f.readline()
    print(x)
    a = int(x)
    x = f.readline()
    print(x)
    a = int(x)
except:
    print("Eitthvað fór úrskeiðis",sys.exc_info())
finally:
    f.close()
    print("skránni hefur verið lokað")




#Æfingadæmi

#1
numerListi=[]
while len(numerListi) < 10:
    try:
        x=int(input("Sláðu inn heiltölu"))
        numerListi.append(x)

    except ValueError as a:
        print("Oops! Þessi villa kom upp: ",a)

#2
listi=[]
teljari=1
while teljari < 7:
    try:
        a='b'
        if teljari==1:
            c=int(a)
        elif teljari==2:
            d=23/0
        elif teljari==3:
            '2' + 2
        elif teljari==4:
            4+spam*3
        elif teljari==5:
            listi[1]
        elif teljari==6:
            import HalloEgErBullModule






    except ValueError:
            teljari=2
            print("Oops!vitlaust gagnatak",sys.exc_info())
            pass
    except (ZeroDivisionError):
        teljari=3
        print("Oops!Bannað að deila með núlli",sys.exc_info())
        pass

    except (TypeError):
        teljari=4
        print("Get ekki lagt saman str og int",sys.exc_info())
        pass
    except (NameError):
        teljari=5
        print("óskligreind breyta",sys.exc_info())
        pass

    except IndexError:
        teljari=6
        print("Þetta stak er ekki til í listanum.")
        pass
    except ImportError:
        teljari=7
        print("Þetta sem þú reyndir að importa er ekki til.")
        pass
#3
