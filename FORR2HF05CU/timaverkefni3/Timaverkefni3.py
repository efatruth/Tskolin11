#livinus felix bassey
#Timaverkefni 3
#21.11.2018

val = 0
while val !=4:
    print(".............................")
    print("dæmi.1,fall sem tekur tvær heiltolu ")
    print("dæmi.2,fall sem tekur inn lista")
    print("dæmi.3,fall sem tekur inn ótilgreindan fjölda")

    val=input("Veldu val 1-3")
        #Dæmi eitt
    if val =="1":
        def add(tal1, tal2):
            return tal1 + tal2
            print("hvada æfinga")
            print("Æfing 1")

            #Safna innslátu frá notanda
            vali = input("innslátu(1):")


            if vali == '1':
               print(fjol1,"+",fjol2,"=", add(fjol1,fjol2))
            else:
               print("tolu er slagid inn ekki !")

          #Dæmi tvö
    elif val =="2":
        listi = []
        def myFunc(x):
            for x in listi:
                if x % 5 == 0:
                    return True
                else:
                    if x < 350:
                        return False
                    allTolar = filter(myFunc,listi)
                    for x in allTolar:
                        print(x)

          #Dæmi þrjú
    elif val =="3":
        def fall(x):
            pawTre = [3** x for x in range[20]]
            return pawTre

#fjol1 = int(input("Sladu inn fyrsta tolu: "))
#fjol2 = int(input("Sladu inn adra tolu: "))

print(add(fjol1,fjol2))

#print(myFunc())

#print(fall())

'''
#Timaverkefni 3 Skriflegt próf

#1.  what will be the output of the following code?
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x+1
        self.y = y+1

p1 = Point()
print(p1.x, p1.y) #answer 1 1


#2.  what will be the output of the following code?
class Test:
    def __init__(self, s):
        self.s = s

    def print(self):
      print(s)#answer is,change the code to be: print(self.s) and it will output: Python Class

a = Test("Python Class")
a.print()


#3.  what will be the output of the following code?
class Test:
    def __init__(self, s):
        self.s = s

    def print(self):
      print(self.s)

msg = Test()#answer is write an arguments like these: msg = Test("adidi") or else it will be an error because of the constructor call is made without an argument.
msg.print()


#4. what will be the output of the following code?
class Test:
    def __init__(self, s = "Welcome"):
        self.s = s

    def print(self):
      print(self.s)

msg = Test()
msg.print()#the programme executes successfully and prints Welcome


#5. what will be the output of the following code?
class Sales:
    def __init__(self,id):
        self.id = id
        id = 100

val = Sales(123)
print(val.id)#Answer, the output will be: 123.


#??6. which of the following statements Are correct about the Given code snippet?
class A:
    def __init__(self, i = 0):
      self.i = i

class B(A):
    def __init__(self, j = 0):
      self.j = j

def main():
  b = B()
  print(b.i)#.
  print(b.j)
main()


#7 what will be the output of the following code?
class A:
    def __init__(self, x = 1):
      self.x = x

class B(A):
    def __init__(self, y = 2):
         A.__init__(self)
         self.y = y

def main():
  b = B()
  print(b.x, b.y)#the Answer will output: 1 2

main()


#8.  what will be the output of the following code?
class test:
    def __init__(self, a= "Hello World"):
        self.a=a

    def display(self):
      print(self.a)

obj=test()
obj.display()#Answer, the output is : Hello World


#?9.  what will be the output of the following code?
class test:
    def __init__(self,a):
        self.a=a

    def display(self):
        print(self.a)
obj=test()
obj.display()#Answer : Runs normally, doesn't display anything or shows ---line 170, in <module>
             #obj=test()
             #TypeError: __init__() missing 1 required positional argument: 'a'--


#10. what will be the output of the following code?
class test:
    def __init__(self):
        self.variable = 'Old'
        self.Change(self.variable)
    def Change(self, var):
        var = 'New'
obj = test()
print(obj.variable)#Answer, the output will be : Old
'''
