# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtDesignerProject/login.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        LoginForm.setObjectName("LoginForm")
        LoginForm.resize(282, 355)
        LoginForm.setInputMethodHints(QtCore.Qt.ImhNone)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LoginForm)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.logo = QtWidgets.QLabel(LoginForm)
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap(":/logo150.png"))
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelUser = QtWidgets.QLabel(LoginForm)
        self.labelUser.setObjectName("labelUser")
        self.verticalLayout_3.addWidget(self.labelUser)
        self.labelPass = QtWidgets.QLabel(LoginForm)
        self.labelPass.setObjectName("labelPass")
        self.verticalLayout_3.addWidget(self.labelPass)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEditUser = QtWidgets.QLineEdit(LoginForm)
        self.lineEditUser.setObjectName("lineEditUser")
        self.verticalLayout_4.addWidget(self.lineEditUser)
        self.lineEditPass = QtWidgets.QLineEdit(LoginForm)
        self.lineEditPass.setObjectName("lineEditPass")
        self.verticalLayout_4.addWidget(self.lineEditPass)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btncancellogin = QtWidgets.QPushButton(LoginForm)
        self.btncancellogin.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btncancellogin.setObjectName("btncancellogin")
        self.horizontalLayout_4.addWidget(self.btncancellogin)
        self.btnlogin = QtWidgets.QPushButton(LoginForm)
        self.btnlogin.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.btnlogin.setObjectName("btnlogin")
        self.horizontalLayout_4.addWidget(self.btnlogin)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.retranslateUi(LoginForm)
        QtCore.QMetaObject.connectSlotsByName(LoginForm)

    def retranslateUi(self, LoginForm):
        _translate = QtCore.QCoreApplication.translate
        LoginForm.setWindowTitle(_translate("LoginForm", "Hraun Hótel - Innskráning"))
        self.labelUser.setText(_translate("LoginForm", "Notandi"))
        self.labelPass.setText(_translate("LoginForm", "Lykilorð"))
        self.btncancellogin.setText(_translate("LoginForm", "Hætta"))
        self.btnlogin.setText(_translate("LoginForm", "Innskrá"))

import icons_rc
