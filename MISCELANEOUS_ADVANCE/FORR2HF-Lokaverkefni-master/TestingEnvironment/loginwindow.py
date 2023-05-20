# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from admin import Ui_AdminWindow
from service import Ui_ServiceWindow
from reception import Ui_ReceptionWindow
from Database.HotelConnect import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


#Address = Address()
#Common = CommonPS()
#Customer = Customer()
#Hotel = Hotel()
#Item = Item()
#Reservation = Reservation()
#Order_Has_Items = Order_Has_Items()
#Order_Has_Rooms = Order_Has_Rooms()
#Room = Room()
#RoomType = RoomType()
#ServiceOrder = ServiceOrder()
#Staff = Staff()

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(299, 326)
        LoginForm.setInputMethodHints(QtCore.Qt.ImhNone)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LoginForm)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(LoginForm)
        self.label.setTextFormat(QtCore.Qt.RichText)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(LoginForm)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.inputuser = QtWidgets.QLineEdit(LoginForm)
        self.inputuser.setObjectName("inputuser")
        self.horizontalLayout.addWidget(self.inputuser)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(LoginForm)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.inputpass = QtWidgets.QLineEdit(LoginForm)
        self.inputpass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.inputpass.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.inputpass.setClearButtonEnabled(False)
        self.inputpass.setObjectName("inputpass")
        self.horizontalLayout_3.addWidget(self.inputpass)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.btnlogin = QtWidgets.QPushButton(LoginForm)
        self.btnlogin.setObjectName("btnlogin")
        # Login button event! #
        self.btnlogin.clicked.connect(self.check_login)
        self.horizontalLayout_4.addWidget(self.btnlogin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btncancellogin = QtWidgets.QPushButton(LoginForm)
        self.btncancellogin.setObjectName("btncancellogin")
        self.btncancellogin.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.horizontalLayout_4.addWidget(self.btncancellogin)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)



    def mainReceptionWindow(self):
        self.receptionWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ReceptionWindow()
        self.ui.setupUi(self.receptionWindow)
        Dialog.hide()
        self.receptionWindow.show()

    def mainAdminWindow(self):
        self.adminWindow = QtWidgets.QMainWindow()
        self.ui = Ui_AdminWindow()
        self.ui.setupUi(self.adminWindow)
        Dialog.hide()
        self.adminWindow.show()

    def mainServiceWindow(self):
        self.serviceWindow = QtWidgets.QMainWindow()
        self.ui = Ui_ServiceWindow()
        self.ui.setupUi(self.serviceWindow)
        Dialog.hide()
        self.serviceWindow.show()

    def showMessageBox(self, title, message):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Warning)
        msgBox.setWindowTitle(title)
        msgBox.setText(message)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()

    def check_login(self):
        User = Employee()
        user = self.inputuser.text()
        passwd = self.inputpass.text()
        print(user)
        print(passwd)
        result = User.EmployeeList()
        for i in result:
            if user == i[8] and passwd == i[9]:
                print("Login successful!")
                EmpID = i[0]
                EmpTitle = i[3]
                print('EmpID:', EmpID)
                print('Title:', EmpTitle)
                if EmpTitle == "Admin":
                    self.mainAdminWindow()
                elif EmpTitle == "Recept":
                    self.mainReceptionWindow()
                elif EmpTitle == "Service":
                    self.mainServiceWindow()
                break

        else:
            print("Login unsuccessful!")
            self.showMessageBox('Warning', 'User not found in database!')


    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Hraun Hótel - Innskráning"))
        #self.label.setText(_translate("LoginForm", "Hraun Hótel"))
        self.label.setPixmap(QPixmap('resources/logo150.png'))
        self.label_2.setText(_translate("LoginForm", "Username"))
        self.label_3.setText(_translate("LoginForm", "Password"))
        self.btncancellogin.setText(_translate("LoginForm", "Cancel"))
        self.btnlogin.setText(_translate("LoginForm", "Login"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_LoginForm()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
