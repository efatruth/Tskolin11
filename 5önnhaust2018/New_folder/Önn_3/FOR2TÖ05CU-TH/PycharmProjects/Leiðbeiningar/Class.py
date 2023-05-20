"""
#Hvað eru object
class Ovinur:

    def __init__(self,lif,bonuslif):
        self.lif = lif
        self.bonuslif = bonuslif

    def attack(self):
        print("Á")
        #Tökum eitt líf af þessu tilviki
        self.lif-=1


    def athLif(self):
        if self.lif<= 0 and self.bonuslif <=0:
            print("Ég er dauður")
        elif self.lif<= 0 and self.bonuslif > 0:
            self.lif = self.bonuslif
            self.bonuslif = 0
            print("Ég er kominn með fleiri líf, hah  a. Owned.")
        else:
            print(str(self.lif)+ "Líf eftir")

ovinur1 = Ovinur(1, 2)
ovinur2 = Ovinur(3, 0)
ovinur1.attack()
ovinur1.attack()
ovinur1.athLif()
"""

class Parent():

    def __init__(self,lastName):
        self.lastName = lastName

    def printLastName(self):
        print(str(self.lastName))


class Child(Parent):

    def __init__(self, firstName):
        self.firstName = firstName

    def printFirstName(self):
        print(str(self.firstName))

barn = Child("Gunni")
barn.printFirstName()

