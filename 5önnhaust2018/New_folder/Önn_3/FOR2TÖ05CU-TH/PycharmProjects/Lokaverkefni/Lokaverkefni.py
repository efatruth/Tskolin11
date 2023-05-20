#Along A. Loftsson
import gc
import collections, json

class Customer:
    def __init__(self, name, address, ssn, nationality, driversID, phone, email, text):
        self.name = name
        self.address = address
        self.ssn = ssn
        self.nationality = nationality
        self.driversID = driversID
        self.phone = phone
        self.email = email
        self.text = text

class Car:
    def __init__(self, plate_number, year, category, text):
        self.plate_number = plate_number
        self.year = year
        self.category = category
        self.text = text

class Type(Car):
    def __init__(self, plate_number, year, category, text, manufacturer, type, seats):
        Car.__init__(self, plate_number, year, category, text)
        self.manufacturer = manufacturer
        self.type = type
        self.seats = seats

    def __iter__(self):
        yield 'plate_number', self.plate_number
        yield 'year', self.year
        yield 'category', self.category
        yield 'text', self.text
        yield 'manufacturer', self.manufacturer
        yield 'type', self.type
        yield 'seats', self.seats

    def __str__(self):
        return self.plate_number, self.year, self.category, self.text, self.manufacturer, self.type, self.seats

class Order(Customer):
    def __init__(self, name, address, ssn, nationality, driversID, phone, email, text,
                 customer_ID, order_date, ordertext):
        Customer.__init__(self, name, address, ssn, nationality, driversID, phone, email, text)
        self.customer_ID = customer_ID
        self.order_date = order_date
        self.ordertext = ordertext



car1 = collections.OrderedDict(Type("ASS69", "2006", "fólksbíll", "Góðurbill", "toyota", "corolla", "4"))
print(car1)
"""
open_file = open("carlist.txt", "r", encoding="utf-8")
read_file = open_file.read()
split_file = read_file.split('\n')

accounts = [] #Hér er lesið úr skrá og splittað.
for i in split_file:
    users = i.split(";")
    accounts.append(users) #Svo bætt inn í lista.

for i in accounts:
    print(i)

log_name = input("Sláðu inn notandanafn (EKKI CASE SENSITIVE): ")
log_pass = input("Sláðu inn lykilorð (CASE SENSITIVE): ") #Lykilorð eru venjulega case sensitive.

login = list((log_name.capitalize(), log_pass)) #Hér er sett í lista svo að er hægt að bera saman við notanda-listann.

for i, x in accounts: #If-lykkja in í for-lykkju til þess að sjá hvort lykilorð og notandanafnið passar.
    if login[0] == i and login[1] == x:
        print("VELKOMINN.")
        break
    elif login[0] == i and login[1] != x or login[0] != i and login[1] == x:
        print("RANGT.")
        break
else:
    print("EKKI TIL.")

open_file.close()

"""
with open('carlist.json', 'w') as open_file:
#open_file.write(getattr(car1, 'year'))
    open_file.write(json.dumps(car1))
"""
integ = 0
for i in new:
    integ += 1
    if integ != len(new):
        open_file.write(i+";")
    else:
        open_file.write(i+"\n")
open_file.close()
print(attrs)
"""


"""
open_file = open("carlist.txt", "r", encoding="utf-8")
read_file = open_file.read()
split_file = read_file.split('\n')
#print("\n".join("%s: %s" % item for item in attrs.items()))
cars = []
for i in split_file:
    car = i.split(",")
    cars.append(car)
for i in cars:
    print(i)
"""
