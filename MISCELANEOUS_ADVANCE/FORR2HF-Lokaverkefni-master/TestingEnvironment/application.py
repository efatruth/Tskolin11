from Database.HotelConnect import *

Common = CommonPS()
Customer = Customer()
Address = Address()
Employee = Employee()
Hotel = Hotel()
Item = Item()
Reservation = Reservation()
Order_Has_Items = Order_Has_Items()
Order_Has_Rooms = Order_Has_Rooms()
Room = Room()
RoomType = RoomType()
ServiceOrder = ServiceOrder()
Staff = Staff()

def empgetinfo():
    print("EmpID: {}".format(EmpAccount.EmpID))
    print("EmpSSN: {}".format(EmpAccount.EmpSSN))
    print("Title: {}".format(EmpAccount.Title))
    print("LName: {}".format(EmpAccount.LName))
    print("FName: {}".format(EmpAccount.FName))
    print("Email: {}".format(EmpAccount.Email))
    print("Phone: {}".format(EmpAccount.Phone))
    print("HireDate: {}".format(EmpAccount.HireDate))
    print("Address: {}".format(EmpAccount.address))


class Account:
    def __init__(self, EmpID, EmpSSN, Title, LName, FName, Email, Phone, HireDate, Zip, CityName, CountryName, StreetName, BuildingNum, ApartNum=None):
        self.EmpID = EmpID
        self.EmpSSN = EmpSSN
        self.Title = Title
        self.LName = LName
        self.FName = FName
        self.Email = Email
        self.Phone = Phone
        self.HireDate = HireDate
        self.address = {'Zip': Zip, 'CityName': CityName, 'CountryName': CountryName, 'StreetName': StreetName, 'BuildingNum': BuildingNum, 'ApartNum': ApartNum}


# Login page
login = False
while login is not True:

    # Retrive all usernames & passwords
    result = Employee.EmployeeList()

    #user = input("Username: ")
    #passwd = input("Password: ")

    user = 'haraldurst181'#'johannath657' #'hermannbi920'
    passwd = 'password'

    for i in result:
        if user == i[8] and passwd == i[9]:
            print("Login successful!")
            login = True
            EmpID = i[0]
            break
    else:
        print("Login unsuccessful!")

if login:
    empinfo = Employee.EmployeeInfo(EmpID)
    addinfo = Address.AddressInfo(empinfo[0][2])

    EmpAccount = Account(EmpID=EmpID, EmpSSN=empinfo[0][1], Title=empinfo[0][3], LName=empinfo[0][4],
                         FName=empinfo[0][5], Email=empinfo[0][6], Phone=empinfo[0][7], HireDate=empinfo[0][10],
                         Zip=addinfo[0][1], CityName=addinfo[0][2], CountryName=addinfo[0][3], StreetName=addinfo[0][4],
                         BuildingNum=addinfo[0][5], ApartNum=addinfo[0][6])
    print('Welcome, {}'.format(EmpAccount.FName + ' ' + EmpAccount.LName))

    if EmpAccount.Title == "Admin":
        print("You're an admin!")

    elif EmpAccount.Title == "Recept":
        while True:
            print()
            print('Receptionist: {}'.format(EmpAccount.FName + ' ' + EmpAccount.LName))
            print("1.) Option 1")
            print("2.) Option 2")
            print("3.) Option 3")
            print("4.) Option 4")
            print("5.) Option 5")
            print("q.) Quit")
            choice = input("Choice: ")

            if choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "q":
                break
            else:
                print("Invalid input!")


    elif EmpAccount.Title == "Service":
        print("You're a servant!")







# Nokkur dæmi um virkni
#result = Common.HireEmployee(Param_Zip='000', Param_CityName='samplecity', Param_CountryName='samplecountry', Param_StreetName='samplestreet', Param_BuildingNum='45', Param_ApartNum=None, Param_HotelID=3, Param_EmpSSN='0000000000', Param_Title='Recept', Param_LName='samplelname', Param_FName='samplefname', Param_Email='sample@sample.com', Param_Phone='000-000-0000', Param_User='sampleuser', Param_Pass='samplepass')

#result = Common.RegisterCustomer(Param_Zip='000', Param_CityName='samplecity', Param_CountryName='samplecountry', Param_StreetName='samplestreet', Param_BuildingNum='100', Param_ApartNum='5C3', Param_CusSSN='0000000000', Param_LName='samplelname', Param_FName='samplefname', Param_Email='sample@sample.com', Param_Phone='000-000-0000', Param_User='sampleuser', Param_Pass='samplepass')

#result = Common.CheckAvailability(New_Start='2018-05-08 13:00:00', New_End='2018-05-12 13:00:00', Param_HotelID=3, Param_TypeID=1)

#result = Common.TotalServiceBill(2)

#result = Common.ServiceListOrdersByHotel(2)
#result = Common.TotalRoomBill(2)
#TotalAmountDue = 0
#for i in result:
#    TotalAmountDue += i[5]
#print(TotalAmountDue)
#result = Common.ReservationAdd(Param_EmpID=1, Param_CusID=6, Param_OrderDate='2018-05-03')

#result = Employee.EmployeeAdd('0000000000', 13, 'sampletitle', 'samplelname', 'samplefname', 'sample@sample.com', '000-000-0000', 'sampleuser', 'samplepass', None)
#result = Common.ReservationRoomAdd()
#result = Common.Service_OrderAdd(Param_RoomID=156, Param_OrderID=2, Param_EmpID=1, Param_DateTimeOfService='2018-05-03 16:00:00')
#result = Common.ServiceAddItem()


#print(result)
