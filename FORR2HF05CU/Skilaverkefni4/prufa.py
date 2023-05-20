
class Person():
    def __init__(self, name, age):
        self.name=name
        self.age =age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def set_name(self,newName):
        self.name=newName
    def set_age(self,newAge):
        self.age =newAge

    def __str__(self):
        return "Persóna " + self.name+" aldur: "+ str(self.age)

class Student(Person):
    def __init__(self, name, age, school, yearsLeft):
        Person.__init__(name, age)
        self.school = school
        self.yearsLeft = yearsLeft

    def __str__(self):
        return "Studen " + self.name+" aldur: "+ str(self.age) + self.school



person1 = Person("Sigga", 54)
person2 = Person("Konni", 25)

#Getting the name of the person instances
print(person1.get_age())
print(person2.get_age())

#Change the name of person2
person2.set_age(100)

print(person2.get_age())

print(person1)


