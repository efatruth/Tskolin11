# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QtDesignerProject/service.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ServiceWindow(object):
    def setupUi(self, ServiceWindow):
        ServiceWindow.setObjectName("ServiceWindow")
        ServiceWindow.resize(570, 430)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ServiceWindow.sizePolicy().hasHeightForWidth())
        ServiceWindow.setSizePolicy(sizePolicy)
        ServiceWindow.setMinimumSize(QtCore.QSize(570, 430))
        ServiceWindow.setMaximumSize(QtCore.QSize(570, 430))
        ServiceWindow.setStyleSheet("QFrame#frame, QFrame#frame_2, #scrollArea, #scrollAreaWidgetContents {\n"
"background-color: #3F4045;\n"
"color: #fff;\n"
"border: none;\n"
"}\n"
"\n"
"QToolButton#toolButton, QToolButton#toolButton_2, QToolButton#toolButton_3, QToolButton#toolButton_4, QToolButton#toolButton_5, QToolButton#toolButton_6 {\n"
"background-color: #7BB2D9;\n"
"border-radius: 7px;\n"
"color: #3F4045;\n"
"}\n"
"\n"
"#frame QToolButton:checked, #frame QToolButton:pressed, #frame QToolButton:hover {\n"
"color: #fff;\n"
"}\n"
"QLabel#labelTopName, QLabel#labelTopTitle {\n"
"color: #fff;\n"
"}\n"
"QVBoxLayout#verticalLayout_5 {\n"
"border-bottom: 1px solid #000;\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"QLabel#labelBorder, QLabel#labelBorder_2, QLabel#labelBorder_3, QLabel#labelBorder_4, QLabel#labelBorder_5, QLabel#labelBorder_6 {\n"
"border-top: 1px solid rgba(0,0,0,0.2);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(ServiceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, 49, 101, 381))
        self.frame.setMaximumSize(QtCore.QSize(16777215, 381))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolButton_2 = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_2.sizePolicy().hasHeightForWidth())
        self.toolButton_2.setSizePolicy(sizePolicy)
        self.toolButton_2.setMinimumSize(QtCore.QSize(51, 51))
        self.toolButton_2.setMaximumSize(QtCore.QSize(51, 51))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/hotel_and_services/png/ring.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_2.setIcon(icon)
        self.toolButton_2.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_2.setCheckable(True)
        self.toolButton_2.setChecked(True)
        self.toolButton_2.setAutoExclusive(True)
        self.toolButton_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_2.setObjectName("toolButton_2")
        self.verticalLayout_2.addWidget(self.toolButton_2, 0, QtCore.Qt.AlignHCenter)
        self.toolButton_5 = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_5.sizePolicy().hasHeightForWidth())
        self.toolButton_5.setSizePolicy(sizePolicy)
        self.toolButton_5.setMinimumSize(QtCore.QSize(51, 51))
        self.toolButton_5.setMaximumSize(QtCore.QSize(51, 51))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/hotel_and_services/png/notebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_5.setIcon(icon1)
        self.toolButton_5.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_5.setCheckable(True)
        self.toolButton_5.setAutoExclusive(True)
        self.toolButton_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_5.setObjectName("toolButton_5")
        self.verticalLayout_2.addWidget(self.toolButton_5, 0, QtCore.Qt.AlignHCenter)
        self.toolButton_3 = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton_3.sizePolicy().hasHeightForWidth())
        self.toolButton_3.setSizePolicy(sizePolicy)
        self.toolButton_3.setMinimumSize(QtCore.QSize(51, 51))
        self.toolButton_3.setMaximumSize(QtCore.QSize(51, 51))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/hotel_and_services/png/trolley.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_3.setIcon(icon2)
        self.toolButton_3.setIconSize(QtCore.QSize(32, 32))
        self.toolButton_3.setCheckable(True)
        self.toolButton_3.setAutoExclusive(True)
        self.toolButton_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_3.setObjectName("toolButton_3")
        self.verticalLayout_2.addWidget(self.toolButton_3, 0, QtCore.Qt.AlignHCenter)
        self.toolButton = QtWidgets.QToolButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(51, 51))
        self.toolButton.setMaximumSize(QtCore.QSize(51, 51))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/hotel_and_services/png/bellboy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon3)
        self.toolButton.setIconSize(QtCore.QSize(32, 32))
        self.toolButton.setCheckable(True)
        self.toolButton.setAutoExclusive(True)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton.setObjectName("toolButton")
        self.verticalLayout_2.addWidget(self.toolButton, 0, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 571, 51))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 0, 401, 51))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTopName = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelTopName.setFont(font)
        self.labelTopName.setObjectName("labelTopName")
        self.verticalLayout.addWidget(self.labelTopName, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 171, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setContentsMargins(30, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelTopTitle = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelTopTitle.setFont(font)
        self.labelTopTitle.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelTopTitle.setObjectName("labelTopTitle")
        self.verticalLayout_3.addWidget(self.labelTopTitle)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 50, 471, 381))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        ServiceWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ServiceWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 570, 22))
        self.menubar.setObjectName("menubar")
        self.menuForrit = QtWidgets.QMenu(self.menubar)
        self.menuForrit.setObjectName("menuForrit")
        ServiceWindow.setMenuBar(self.menubar)
        self.actionLista_pantanir = QtWidgets.QAction(ServiceWindow)
        self.actionLista_pantanir.setObjectName("actionLista_pantanir")
        self.actionSkra_ut = QtWidgets.QAction(ServiceWindow)
        self.actionSkra_ut.setObjectName("actionSkra_ut")
        self.actionH_tta = QtWidgets.QAction(ServiceWindow)
        self.actionH_tta.setObjectName("actionH_tta")
        self.menuForrit.addAction(self.actionSkra_ut)
        self.menuForrit.addAction(self.actionH_tta)
        self.menubar.addAction(self.menuForrit.menuAction())

        self.retranslateUi(ServiceWindow)
        QtCore.QMetaObject.connectSlotsByName(ServiceWindow)

    def retranslateUi(self, ServiceWindow):
        _translate = QtCore.QCoreApplication.translate
        ServiceWindow.setWindowTitle(_translate("ServiceWindow", "Hraun Hótel - Þjónustuaðili"))
        self.toolButton_2.setText(_translate("ServiceWindow", "Panta"))
        self.toolButton_5.setText(_translate("ServiceWindow", "Pantanir"))
        self.toolButton_3.setText(_translate("ServiceWindow", "Þjónustur"))
        self.toolButton.setText(_translate("ServiceWindow", "Um mig"))
        self.labelTopName.setText(_translate("ServiceWindow", "Name"))
        self.labelTopTitle.setText(_translate("ServiceWindow", "ActionTitle"))
        self.menuForrit.setTitle(_translate("ServiceWindow", "Forrit"))
        self.actionLista_pantanir.setText(_translate("ServiceWindow", "Lista pantanir"))
        self.actionSkra_ut.setText(_translate("ServiceWindow", "Skrá út"))
        self.actionH_tta.setText(_translate("ServiceWindow", "Hætta"))

import icons_rc
