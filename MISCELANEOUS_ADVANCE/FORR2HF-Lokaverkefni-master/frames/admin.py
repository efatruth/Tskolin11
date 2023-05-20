# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtDesignerProject/admin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(511, 484)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        AdminWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AdminWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 22))
        self.menubar.setObjectName("menubar")
        self.menuForrit = QtWidgets.QMenu(self.menubar)
        self.menuForrit.setObjectName("menuForrit")
        AdminWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AdminWindow)
        self.statusbar.setObjectName("statusbar")
        AdminWindow.setStatusBar(self.statusbar)
        self.actionSkra_ut = QtWidgets.QAction(AdminWindow)
        self.actionSkra_ut.setObjectName("actionSkra_ut")
        self.actionH_tta = QtWidgets.QAction(AdminWindow)
        self.actionH_tta.setObjectName("actionH_tta")
        self.menuForrit.addAction(self.actionSkra_ut)
        self.menuForrit.addAction(self.actionH_tta)
        self.menubar.addAction(self.menuForrit.menuAction())

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Hraun Hótel - Stjórnandi"))
        self.label.setText(_translate("AdminWindow", "Admin"))
        self.menuForrit.setTitle(_translate("AdminWindow", "Forrit"))
        self.actionSkra_ut.setText(_translate("AdminWindow", "Skrá út"))
        self.actionH_tta.setText(_translate("AdminWindow", "Hætta"))

