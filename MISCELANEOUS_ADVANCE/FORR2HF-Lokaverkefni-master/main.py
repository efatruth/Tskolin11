import sys, datetime, time
from frames.login import Ui_LoginForm
from frames.admin import Ui_AdminWindow
from frames.reception import Ui_ReceptionWindow
from frames.service import Ui_ServiceWindow
from Database.HotelConnect import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
from PyQt5.QtGui import QPixmap

com = CommonPS()
res = Reservation()
addr = Address()
emp = Employee()
cus = Customer()
hote = Hotel()
itm = Item()
ohi = Order_Has_Items()
ohr = Order_Has_Rooms()
room = Room()
rty = RoomType()
sor= ServiceOrder()
stf = Staff()



class Account:
    def __init__(self, EmpID, EmpSSN, Title, LName, FName, Email, Phone, EmpUser, HireDate, Zip, CityName, CountryName, StreetName, BuildingNum, ApartNum=None):
        self.EmpID = EmpID
        self.EmpSSN = EmpSSN
        self.EmpUser = EmpUser
        self.Title = Title
        self.LName = LName
        self.FName = FName
        self.Email = Email
        self.Phone = Phone
        self.HireDate = HireDate
        self.address = {'Zip': Zip, 'CityName': CityName, 'CountryName': CountryName, 'StreetName': StreetName, 'BuildingNum': BuildingNum, 'ApartNum': ApartNum}

    def empgetinfo(self):
        print("EmpID: {}".format(self.EmpID))
        print("EmpSSN: {}".format(self.EmpSSN))
        print("Title: {}".format(self.Title))
        print("LName: {}".format(self.LName))
        print("FName: {}".format(self.FName))
        print("Email: {}".format(self.Email))
        print("Phone: {}".format(self.Phone))
        print("HireDate: {}".format(self.HireDate))
        print("Address: {}".format(self.address))




class LoginWindow(QtWidgets.QDialog, Ui_LoginForm):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.setupUi(self)

        self.btnlogin.clicked.connect(self.check_login)
        self.lineEditPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btncancellogin.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.logo.setPixmap(QPixmap('resources/logo150.png'))

        self.show()


    def mainReceptionWindow(self):
        self.receptionWindow = ReceptWindow()
        self.hide()

    def mainAdminWindow(self):
        self.adminWindow = AdminWindow()
        self.hide()

    def mainServiceWindow(self):
        self.serviceWindow = ServiceWindow()
        self.hide()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def check_login(self):
        emp = Employee()
        addr = Address()
        user = self.lineEditUser.text()
        passwd = self.lineEditPass.text()
        result = emp.EmployeeList()
        for i in result:
            if user == i[8] and passwd == i[9]:
                print("Login successful!")
                userAddr = addr.AddressInfo(i[2])

                global loggedInUser
                loggedInUser = Account(EmpID=i[0], EmpSSN=i[1], Title=i[3],
                               LName=i[4], FName=i[5], Email=i[6],
                               Phone=i[7], EmpUser=i[8], HireDate=i[10], Zip=userAddr[0][1],
                               CityName=userAddr[0][2], CountryName=userAddr[0][3], StreetName=userAddr[0][4],
                               BuildingNum=userAddr[0][5], ApartNum=userAddr[0][6])

                if i[3] == "Admin":
                    self.mainAdminWindow()
                elif i[3] == "Recept":
                    self.mainReceptionWindow()
                elif i[3] == "Service":
                    self.mainServiceWindow()
                break

        else:
            print("Login unsuccessful!")
            self.showMessageBox('Viðvörðun!', 'Notandi ekki til!')


class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self):
        super(AdminWindow, self).__init__()
        self.setupUi(self)
        self.actionSkra_ut.triggered.connect(self.logOut)
        self.actionH_tta.triggered.connect(self.close)

        self.show()

    def logOut(self):
        self.menubar.clear()
        self.loginWindow = LoginWindow()
        self.hide()

class ReceptWindow(QtWidgets.QMainWindow, Ui_ReceptionWindow):
    def __init__(self):
        super(ReceptWindow, self).__init__()
        self.setupUi(self)

        self.btnCreateOrder.clicked.connect(self.createOrder)
        self.btnAddRoomToOrder.clicked.connect(self.addRoomToOrder)
        self.btnFindAvailableRooms.clicked.connect(self.checkAvailableRooms)
        self.dateTimeEditCheckIn.setDate(QtCore.QDate.currentDate())
        self.dateTimeEditCheckOut.setDate(QtCore.QDate.currentDate())
        self.selectHotelPlace.currentTextChanged.connect(self.selectAvailableRoom.clear)
        self.selectRoomType.currentTextChanged.connect(self.selectAvailableRoom.clear)
        self.dateTimeEditCheckIn.dateChanged.connect(self.selectAvailableRoom.clear)
        self.dateTimeEditCheckOut.dateChanged.connect(self.selectAvailableRoom.clear)
        self.selectHotelPlace.addItem("Hraun Hótel Reykjavík", 1)
        self.selectHotelPlace.addItem("Hraun Hótel Akureyri", 2)
        self.selectHotelPlace.addItem("Hraun Hótel Selfoss", 3)
        self.selectRoomType.addItem("Guest", 3)
        self.selectRoomType.addItem("Suite", 2)
        self.selectRoomType.addItem("Executive", 1)
        self.toolButton.clicked.connect(lambda: self.display(self.page, "Hefja bókun"))
        self.toolButton_2.clicked.connect(lambda: self.display(self.page_3, "Panta herbergi"))
        self.toolButton_3.clicked.connect(lambda: self.display(self.page_4, "Nýskrá viðskiptavin"))
        self.toolButton_4.clicked.connect(lambda: self.display(self.page_5, "Skoða pantanir"))
        self.toolButton_5.clicked.connect(lambda: self.display(self.page_6, "Um mig"))
        self.labelTopTitle.setText("Hefja bókun")
        self.labelTopName.setText(loggedInUser.FName + " " + loggedInUser.LName)
        self.btnRegCus.clicked.connect(self.registerCustomer)
        self.btnSearchCusHistory.clicked.connect(self.searchCusHistory)
        self.treeCustHistory.setHeaderLabel("Fullt nafn")
        self.actionSkra_ut.triggered.connect(self.logOut)
        self.actionH_tta.triggered.connect(self.close)
        loggedInUser.empgetinfo()

        # About user

        self.labelAboutID.setText("Auðkenni: {}".format(loggedInUser.EmpID))
        self.labelAboutName.setText("Nafn: {}".format(loggedInUser.FName + " " + loggedInUser.LName))
        self.labelAboutTitle.setText("Starfsheiti: {}".format(loggedInUser.Title))
        self.labelAboutSSN.setText("Kennitala: {}".format(loggedInUser.EmpSSN))
        self.labelAboutEmail.setText("Netfang: {}".format(loggedInUser.Email))
        self.labelAboutPhone.setText("Sími: {}".format(loggedInUser.Phone))
        if loggedInUser.address['ApartNum'] == None:
            self.labelAboutAddress.setText("Heimilisfang: {}, {}, {}, {}, {}".format(loggedInUser.address['StreetName'], loggedInUser.address['BuildingNum'], loggedInUser.address['Zip'], loggedInUser.address['CityName'], loggedInUser.address['CountryName']))
        else:
            self.labelAboutAddress.setText("Heimilisfang: (Dyr {}), {}, {}, {}, {}, {}".format(loggedInUser.address['ApartNum'], loggedInUser.address['StreetName'], loggedInUser.address['BuildingNum'], loggedInUser.address['Zip'], loggedInUser.address['CityName'], loggedInUser.address['CountryName']))
        self.labelAboutUser.setText("Notandanafn: {}".format(loggedInUser.EmpUser))
        workplaces = com.GetWorkplaces(loggedInUser.EmpID)
        tmp = str()
        if len(workplaces) == 1: tmp = workplaces[0][0]
        else:
            for i in workplaces:
                if workplaces[-1][0] != i[0]: tmp += i[0] + ", "
                else: tmp += i[0]

        self.labelAboutWorkplaces.setText("Vinnustaður/ir: {}".format(tmp))


        self.show()

    def display(self,i, action):
        self.stackedWidget.setCurrentWidget(i)
        self.labelTopTitle.setText(action)

    def logOut(self):
        self.menubar.clear()
        self.loginWindow = LoginWindow()
        self.hide()

    def createOrder(self):
        print("Create order was clicked!")
        cus = Customer()
        res = Reservation()

        result = cus.CustomerList()
        for i in result:
            if i[1] == self.lineEditNewOrderCusSSN.text():
                print("Customer: {} does exist".format(i[1]))
                result = res.ReservationAdd(Param_EmpID=loggedInUser.EmpID,
                                            Param_CusID=i[0],
                                            Param_OrderDate=datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
                self.lineEditOrderID.setPlaceholderText(str(result))
                self.showMessageBox("Upplýsing!", "Pöntunarnúmer: {}".format(str(result)))
                break

        else:
            self.showMessageBox("Viðvörðun!", "Viðskiptavinur með kennitöluna: {} er ekki til!".format(self.lineEditNewOrderCusSSN.text()))

    def addRoomToOrder(self):
        print("Reynt var að bæta við herbergi!")
        res = Reservation()
        com = CommonPS()
        self.orderID = self.lineEditOrderID.text()

        self.roomID = self.selectAvailableRoom.currentData()

        if self.orderID:
            if self.roomID:
                result = res.ReservationList()
                for i in result:
                    if int(self.orderID) == i[0]:
                        print("Official pöntun hafin!")
                        print("Eftirfarandi verður notað til pöntunar:")
                        print("OrderID:  {}".format(self.orderID))
                        print("RoomID:   {}".format(self.roomID))
                        print("CheckIn:  {}".format(self.dateCheckIn))
                        print("CheckOut: {}".format(self.dateCheckOut))
                        print("Pöntunarferli lokið...")

                        result = com.ReservationRoomAdd(Param_OrderID=int(self.orderID), Param_RoomID=int(self.roomID),
                                                        Param_CheckInDate=self.dateCheckIn, Param_CheckOutDate=self.dateCheckOut)
                        print(result)
                        self.showMessageBox("Upplýsing!", "Herbergi númer {} hefur verið bætt við á pöntun {}".format(self.selectAvailableRoom.currentText(), self.orderID))
                        self.checkAvailableRooms()
                        break



                else:
                    self.showMessageBox("Viðvörðun!", "OrderID er ekki til!")

            else:
                self.showMessageBox("Viðvörðun!", "Ekker er búið að velja herbergi")

        else:
            self.showMessageBox("Viðvörðun!", "Ekki er búið að velja orderID")



    def registerCustomer(self):
        print("Reynt var að skrá nýann viðskiptavin!")
        cus = Customer()
        com = CommonPS()

        result = cus.CustomerList()
        for i in result:
            if i[1] == self.lineEditCusRegSSN.text():
                self.showMessageBox("Viðvörðun!", "Viðskiptavinur er núþegar til í kerfinu og er með númerið {}".format(i[0]))
                break
            elif i[7] == self.lineEditCusRegUser.text():
                self.showMessageBox("Viðvörðun!", "Notandanafnið {} er núþegar í notkun".format(self.lineEditCusRegUser.text()))
                break

        else:

            if self.lineEditCusRegLName.text() and \
                self.lineEditCusRegFName.text() and \
                self.lineEditCusRegLName.text() and \
                self.lineEditCusRegSSN.text() and \
                self.lineEditCusRegEmail.text() and \
                self.lineEditCusRegPhone.text() and \
                self.lineEditCusRegCountry.text() and \
                self.lineEditCusRegCity.text() and \
                self.lineEditCusRegZip.text() and \
                self.lineEditCusRegStreet.text() and \
                self.lineEditCusRegBuildingNum.text() and \
                self.lineEditCusRegUser.text() and \
                self.lineEditCusRegPassword.text():

                if len(self.lineEditCusRegPassword.text()) <= 5:
                    self.showMessageBox("Viðvörðun!", "Æskilegt er að lykilorð sé meira en fimm stafir!")

                else:


                    if len(self.lineEditCusRegApartNum.text()) == 0:
                        tmp = None

                    else:
                        tmp = self.lineEditCusRegApartNum.text()

                    result = com.RegisterCustomer(Param_LName=self.lineEditCusRegLName.text(),
                                                  Param_FName=self.lineEditCusRegFName.text(),
                                                  Param_CusSSN=self.lineEditCusRegSSN.text(),
                                                  Param_Email=self.lineEditCusRegEmail.text(),
                                                  Param_Phone=self.lineEditCusRegPhone.text(),
                                                  Param_CountryName=self.lineEditCusRegCountry.text(),
                                                  Param_CityName=self.lineEditCusRegCity.text(),
                                                  Param_Zip=self.lineEditCusRegZip.text(),
                                                  Param_StreetName=self.lineEditCusRegStreet.text(),
                                                  Param_BuildingNum=self.lineEditCusRegBuildingNum.text(),
                                                  Param_ApartNum=tmp,
                                                  Param_User=self.lineEditCusRegUser.text(),
                                                  Param_Pass=self.lineEditCusRegPassword.text())


                    if result != 0:
                        self.showMessageBox("Upplýsing!", "Aðgerð tókst! {} hefur eftirfarandi númer: {}".format(self.lineEditCusRegFName.text() + " " + self.lineEditCusRegLName.text(), result))

                    else:
                        self.showMessageBox("Viðvörðun!", "Eitthvað fór úrskeyðist...")



            else:
                self.showMessageBox("Viðvörðun!", "Ekki er búið að fylla í þá dálka sem þarf!")

    def checkAvailableRooms(self):
        com = CommonPS()

        self.hotelID = self.selectHotelPlace.currentData()
        self.roomTypeID = self.selectRoomType.currentData()

        # Convert datetime into MySql friendly string and UNIX time
        tmp = str(self.dateTimeEditCheckIn.text()).split(".")
        if len(tmp[0]) == 1: tmp[0] = "0" + tmp[0]
        if len(tmp[1]) == 1: tmp[1] = "0" + tmp[1]
        tmpDate = tmp[0] + "." + tmp[1] + "." + tmp[2]
        self.dateCheckIn = datetime.datetime.strptime(tmpDate, '%d.%m.%Y %H:%M')
        self.absoluteCheckIn = time.mktime(self.dateCheckIn.timetuple())

        # Convert datetime into MySql friendly string and UNIX time
        tmp = str(self.dateTimeEditCheckOut.text()).split(".")
        if len(tmp[0]) == 1: tmp[0] = "0" + tmp[0]
        if len(tmp[1]) == 1: tmp[1] = "0" + tmp[1]
        tmpDate = tmp[0] + "." + tmp[1] + "." + tmp[2]
        self.dateCheckOut = datetime.datetime.strptime(tmpDate, '%d.%m.%Y %H:%M')
        self.absoluteCheckOut = time.mktime(self.dateCheckOut.timetuple())

        # Results of converting datetime into MySql friendly string and UNIX time
        #print("AbsoluteCheckIn:  {}".format(absoluteCheckIn))
        #print("AbsoluteCheckOut: {}".format(absoluteCheckOut))
        #print("CheckIn: {} --> {}".format(self.dateTimeEditCheckIn.text(), dateCheckIn))
        #print("CheckOut: {} --> {}".format(self.dateTimeEditCheckOut.text(), dateCheckOut))


        if self.absoluteCheckOut <= self.absoluteCheckIn or self.absoluteCheckIn < time.time():
            self.showMessageBox("Viðvörðun!", "Vitlaus dagsetning!")

        else:
            result = com.CheckAvailability(New_Start=self.dateCheckIn, New_End=self.dateCheckOut,
                                           Param_HotelID=self.hotelID, Param_TypeID=self.roomTypeID)

            self.selectAvailableRoom.clear()
            for i in result:
                print(i)
                i[0] = str(i[0])
                self.selectAvailableRoom.addItem(str(i[1]), i[0])

        # Check availability
        print("CheckIn:  {}".format(self.dateCheckIn))
        print("CheckOut: {}".format(self.dateCheckOut))
        print("HotelID:  {}".format(self.hotelID))
        print("TypeID:   {}".format(self.roomTypeID))


    def searchCusHistory(self):
        print("Reynt var að leita af customer history")
        cus = Customer()
        com = CommonPS()

        #cusOrders = QtWidgets.QTreeWidgetItem(["1"])
        #item = QtWidgets.QTreeWidgetItem(["Hello World!"])
        #item.addChild(QtWidgets.QTreeWidgetItem(["Hello"]))

        #int(self.lineEditCusHistorySearchSSN.text())

        result = cus.CustomerList()
        for i in result:
            if i[1] == self.lineEditCusHistorySearchSSN.text():
                print("Customer: {} does exist".format(i[1]))
                cusID = i[0]
                self.treeCustHistory.clear()
                self.treeCustHistory.setHeaderLabel(i[4] + " " + i[3])
                cusOrders = com.CustomerOrders(cusID)

                for order in cusOrders:
                    tmpOrder = QtWidgets.QTreeWidgetItem(["Bókunarnúmer: {}".format(order[0])])
                    self.treeCustHistory.addTopLevelItem(tmpOrder)
                    #roomsOnOrder = com.RoomsOnOrder(order[0])   <-- VIRKAR
                    roomsOnOrder = com.TotalRoomBill(order[0])

                    tmpOrderDate = QtWidgets.QTreeWidgetItem(["Bókunartími: {}".format(order[3])])
                    tmpOrderEmp = QtWidgets.QTreeWidgetItem(["Starfsmaður: {}".format(str(order[9]) + " " + str(order[8]))])
                    tmpOrder.addChild(tmpOrderDate)
                    tmpOrder.addChild(tmpOrderEmp)

                    for room in roomsOnOrder:
                        tmpRoomNum = QtWidgets.QTreeWidgetItem(["Herbergi: {}".format(room[3])])

                        tmpRoomCheckIn = QtWidgets.QTreeWidgetItem(["Innskráning: {}".format(room[0])])
                        tmpRoomCheckOut = QtWidgets.QTreeWidgetItem(["Útskráning: {}".format(room[1])])
                        tmpRoomHotel = QtWidgets.QTreeWidgetItem(["Staðsetning: {}".format(room[7])])
                        tmpRoomType = QtWidgets.QTreeWidgetItem(["Tegund: {}".format(room[2])])
                        tmpRoomDays = QtWidgets.QTreeWidgetItem(["Dagar: {}".format(room[5])])
                        tmpRoomCost = QtWidgets.QTreeWidgetItem(["Verð: {:,},- kr".format(room[4])])
                        tmpRoomTotal = QtWidgets.QTreeWidgetItem(["Heildarverð: {:,},- kr".format(room[6])])

                        tmpOrder.addChild(tmpRoomNum)
                        tmpRoomNum.addChild(tmpRoomCheckIn)
                        tmpRoomNum.addChild(tmpRoomCheckOut)
                        tmpRoomNum.addChild(tmpRoomHotel)
                        tmpRoomNum.addChild(tmpRoomType)
                        tmpRoomNum.addChild(tmpRoomDays)
                        tmpRoomNum.addChild(tmpRoomCost)
                        tmpRoomNum.addChild(tmpRoomTotal)


                        servicesOnRoom = com.ServicesOnRooms(room[9], room[8])

                        for service in servicesOnRoom:
                            tmpService = QtWidgets.QTreeWidgetItem(["Pöntunarnúmer: {}".format(service[0])])
                            tmpRoomNum.addChild(tmpService)
                            serviceDetails = com.ServiceDetails(service[0]) # taka þetta

                            tmpServiceEmp = QtWidgets.QTreeWidgetItem(["Starfsmaður: {}".format(str(service[10]) + " " + str(service[9]))])
                            tmpServiceDate = QtWidgets.QTreeWidgetItem(["Dagsetning: {}".format(service[4])])
                            tmpService.addChild(tmpServiceEmp)
                            tmpService.addChild(tmpServiceDate)
                            print(service)

                            for detail in serviceDetails:
                                tmpServiceDetail = QtWidgets.QTreeWidgetItem(["{}".format(detail[5])])
                                tmpService.addChild(tmpServiceDetail)
                                tmpServiceDetailQty = QtWidgets.QTreeWidgetItem(["Magn: {} stk".format(detail[3])])
                                try:
                                    tmpServiceDetailCost = QtWidgets.QTreeWidgetItem(["Verð: {:,},- kr".format(detail[7])])
                                    tmpServiceDetailTotalCost = QtWidgets.QTreeWidgetItem(["Heildarverð: {:,},- kr".format(detail[8])])
                                except:
                                    tmpServiceDetailCost = QtWidgets.QTreeWidgetItem(["Verð: {}".format(detail[7])])
                                    tmpServiceDetailTotalCost = QtWidgets.QTreeWidgetItem(["Heildarverð: {}".format(detail[8])])

                                tmpServiceDetail.addChild(tmpServiceDetailQty)
                                tmpServiceDetail.addChild(tmpServiceDetailCost)
                                tmpServiceDetail.addChild(tmpServiceDetailTotalCost)

                break

        else:
            self.showMessageBox("Viðvörðun!", "Viðskiptavinur með kennitöluna: {} er ekki til!".format(self.lineEditCusHistorySearchSSN.text()))


    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        if title == "Viðvörðun!": msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        if title == "Upplýsing!": msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

class ServiceWindow(QtWidgets.QMainWindow, Ui_ServiceWindow):
    def __init__(self):
        super(ServiceWindow, self).__init__()
        self.setupUi(self)
        self.actionSkra_ut.triggered.connect(self.logOut)
        self.actionH_tta.triggered.connect(self.close)


        self.show()

    def logOut(self):
        self.menubar.clear()
        self.loginWindow = LoginWindow()
        self.hide()



if __name__ == "__main__":
    #global loggedInUser
    #loggedInUser = Account(EmpID=1, EmpSSN="", Title="Recept",
    #               LName="", FName="Website", Email="",
    #               Phone="", EmpUser="", HireDate="", Zip="",
    #               CityName="", CountryName="", StreetName="",
    #               BuildingNum="", ApartNum="")
    app = QtWidgets.QApplication(sys.argv)
    #window = ReceptWindow()
    window = LoginWindow()
    sys.exit(app.exec_())
    # lineEditCusID
    # Láta selectAvailableRoom reseta eftir að pantað hefur verið herbergi

