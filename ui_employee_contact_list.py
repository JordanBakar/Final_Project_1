# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employee_contact_listSnJGmV.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_ContactListMainScreen(object):
    def setupUi(self, ContactListMainScreen: None) -> None:
        """
        Constructor that loads up the Contact List Main Screen
        :param self: the instance of the __init__ class
        :param ContactListMainScreen: This is the Contact List Main Screen
        :return: none
        """
        if not ContactListMainScreen.objectName():
            ContactListMainScreen.setObjectName(u"ContactListMainScreen")
        ContactListMainScreen.resize(1000, 750)
        ContactListMainScreen.setMinimumSize(QSize(1000, 700))
        self.centralwidget = QWidget(ContactListMainScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.Backgrondframe = QFrame(self.centralwidget)
        self.Backgrondframe.setObjectName(u"Backgrondframe")
        self.Backgrondframe.setStyleSheet(u"QFrame{\n"
                                          "	\n"
                                          "	background-color: qlineargradient(spread:pad, x1:0.539773, y1:1, x2:0.528636, y2:0.266, stop:0 rgba(158, 139, 101, 255), stop:1 rgba(57, 66, 136, 255));\n"
                                          "	color: rgb(230, 230, 230);\n"
                                          "	border-radius: 12px;\n"
                                          "}")
        self.Backgrondframe.setFrameShape(QFrame.StyledPanel)
        self.Backgrondframe.setFrameShadow(QFrame.Raised)
        self.label_mainTitle = QLabel(self.Backgrondframe)
        self.label_mainTitle.setObjectName(u"label_mainTitle")
        self.label_mainTitle.setGeometry(QRect(0, 20, 981, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(33)
        self.label_mainTitle.setFont(font)
        self.label_mainTitle.setStyleSheet(u"color: rgb(238, 238, 238);\n"
                                           "background: transparent;")
        self.label_mainTitle.setAlignment(Qt.AlignCenter)
        self.lineEdit_firstName = QLineEdit(self.Backgrondframe)
        self.lineEdit_firstName.setObjectName(u"lineEdit_firstName")
        self.lineEdit_firstName.setGeometry(QRect(160, 100, 311, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(15)
        self.lineEdit_firstName.setFont(font1)
        self.lineEdit_firstName.setStyleSheet(u"QLineEdit {\n"
                                              "	border: 3px solid rgb(0, 108, 154);\n"
                                              "	border-radius: 12px;\n"
                                              "	color: rgb(0, 0, 0);\n"
                                              "	padding-left: 20px;\n"
                                              "	padding-right: 20px; \n"
                                              "	background-color: rgb(255, 255, 255);\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:hover {\n"
                                              "	border: 2px solid rgb(0, 165, 230);\n"
                                              "}\n"
                                              "\n"
                                              "QLineEdit:focus{\n"
                                              "	border: 2px solid rgb(85, 170, 255);\n"
                                              "	\n"
                                              "	background-color: rgb(198, 198, 198);\n"
                                              "}")
        self.label_firstName = QLabel(self.Backgrondframe)
        self.label_firstName.setObjectName(u"label_firstName")
        self.label_firstName.setGeometry(QRect(0, 80, 161, 71))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(17)
        self.label_firstName.setFont(font2)
        self.label_firstName.setStyleSheet(u"color: rgb(238, 238, 238);\n"
                                           "background: transparent;")
        self.label_firstName.setAlignment(Qt.AlignCenter)
        self.label_emailAddress = QLabel(self.Backgrondframe)
        self.label_emailAddress.setObjectName(u"label_emailAddress")
        self.label_emailAddress.setGeometry(QRect(10, 170, 171, 71))
        self.label_emailAddress.setFont(font2)
        self.label_emailAddress.setStyleSheet(u"color: rgb(238, 238, 238);\n"
                                              "background: transparent;")
        self.label_emailAddress.setAlignment(Qt.AlignCenter)
        self.lineEdit_emailAddress = QLineEdit(self.Backgrondframe)
        self.lineEdit_emailAddress.setObjectName(u"lineEdit_emailAddress")
        self.lineEdit_emailAddress.setGeometry(QRect(190, 190, 771, 41))
        self.lineEdit_emailAddress.setFont(font1)
        self.lineEdit_emailAddress.setStyleSheet(u"QLineEdit {\n"
                                                 "	border: 3px solid rgb(0, 108, 154);\n"
                                                 "	border-radius: 12px;\n"
                                                 "	color: rgb(0, 0, 0);\n"
                                                 "	padding-left: 20px;\n"
                                                 "	padding-right: 20px; \n"
                                                 "	background-color: rgb(255, 255, 255);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:hover {\n"
                                                 "	border: 2px solid rgb(0, 165, 230);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:focus{\n"
                                                 "	border: 2px solid rgb(85, 170, 255);\n"
                                                 "	\n"
                                                 "	background-color: rgb(198, 198, 198);\n"
                                                 "}")
        self.lineEdit_lastName = QLineEdit(self.Backgrondframe)
        self.lineEdit_lastName.setObjectName(u"lineEdit_lastName")
        self.lineEdit_lastName.setGeometry(QRect(650, 100, 311, 41))
        self.lineEdit_lastName.setFont(font1)
        self.lineEdit_lastName.setStyleSheet(u"QLineEdit {\n"
                                             "	border: 3px solid rgb(0, 108, 154);\n"
                                             "	border-radius: 12px;\n"
                                             "	color: rgb(0, 0, 0);\n"
                                             "	padding-left: 20px;\n"
                                             "	padding-right: 20px; \n"
                                             "	background-color: rgb(255, 255, 255);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:hover {\n"
                                             "	border: 2px solid rgb(0, 165, 230);\n"
                                             "}\n"
                                             "\n"
                                             "QLineEdit:focus{\n"
                                             "	border: 2px solid rgb(85, 170, 255);\n"
                                             "	\n"
                                             "	background-color: rgb(198, 198, 198);\n"
                                             "}")
        self.label_lastName = QLabel(self.Backgrondframe)
        self.label_lastName.setObjectName(u"label_lastName")
        self.label_lastName.setGeometry(QRect(490, 80, 151, 71))
        self.label_lastName.setFont(font2)
        self.label_lastName.setStyleSheet(u"color: rgb(238, 238, 238);\n"
                                          "background: transparent;")
        self.label_lastName.setAlignment(Qt.AlignCenter)
        self.label_phoneNumber = QLabel(self.Backgrondframe)
        self.label_phoneNumber.setObjectName(u"label_phoneNumber")
        self.label_phoneNumber.setGeometry(QRect(20, 260, 151, 71))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(16)
        self.label_phoneNumber.setFont(font3)
        self.label_phoneNumber.setStyleSheet(u"color: rgb(238, 238, 238);\n"
                                             "background: transparent;")
        self.label_phoneNumber.setAlignment(Qt.AlignCenter)
        self.comboBox_jobPosition = QComboBox(self.Backgrondframe)
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.addItem("")
        self.comboBox_jobPosition.setObjectName(u"comboBox_jobPosition")
        self.comboBox_jobPosition.setGeometry(QRect(720, 280, 241, 41))
        self.comboBox_jobPosition.setFont(font1)
        self.comboBox_jobPosition.setEditable(False)
        self.lineEdit_phoneNumber1 = QLineEdit(self.Backgrondframe)
        self.lineEdit_phoneNumber1.setObjectName(u"lineEdit_phoneNumber1")
        self.lineEdit_phoneNumber1.setGeometry(QRect(190, 280, 91, 41))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_phoneNumber1.sizePolicy().hasHeightForWidth())
        self.lineEdit_phoneNumber1.setSizePolicy(sizePolicy)
        self.lineEdit_phoneNumber1.setFont(font1)
        self.lineEdit_phoneNumber1.setStyleSheet(u"QLineEdit {\n"
                                                 "	setMaxLength: 3;\n"
                                                 "	border: 3px solid rgb(0, 108, 154);\n"
                                                 "	border-radius: 12px;\n"
                                                 "	color: rgb(0, 0, 0);\n"
                                                 "	padding-left: 20px;\n"
                                                 "	padding-right: 20px; \n"
                                                 "	background-color: rgb(255, 255, 255);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:hover {\n"
                                                 "	border: 2px solid rgb(0, 165, 230);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:focus{\n"
                                                 "	border: 2px solid rgb(85, 170, 255);\n"
                                                 "	\n"
                                                 "	background-color: rgb(198, 198, 198);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit::setMaxLength(3);\n"
                                                 "QLineEdit::setMaxLenght (3);")
        self.lineEdit_phoneNumber2 = QLineEdit(self.Backgrondframe)
        self.lineEdit_phoneNumber2.setObjectName(u"lineEdit_phoneNumber2")
        self.lineEdit_phoneNumber2.setGeometry(QRect(330, 280, 91, 41))
        self.lineEdit_phoneNumber2.setFont(font1)
        self.lineEdit_phoneNumber2.setStyleSheet(u"QLineEdit {\n"
                                                 "	border: 3px solid rgb(0, 108, 154);\n"
                                                 "	border-radius: 12px;\n"
                                                 "	color: rgb(0, 0, 0);\n"
                                                 "	padding-left: 20px;\n"
                                                 "	padding-right: 20px; \n"
                                                 "	background-color: rgb(255, 255, 255);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:hover {\n"
                                                 "	border: 2px solid rgb(0, 165, 230);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:focus{\n"
                                                 "	border: 2px solid rgb(85, 170, 255);\n"
                                                 "	\n"
                                                 "	background-color: rgb(198, 198, 198);\n"
                                                 "}")
        self.lineEdit_phoneNumber3 = QLineEdit(self.Backgrondframe)
        self.lineEdit_phoneNumber3.setObjectName(u"lineEdit_phoneNumber3")
        self.lineEdit_phoneNumber3.setGeometry(QRect(470, 280, 101, 41))
        self.lineEdit_phoneNumber3.setFont(font1)
        self.lineEdit_phoneNumber3.setStyleSheet(u"QLineEdit {\n"
                                                 "	border: 3px solid rgb(0, 108, 154);\n"
                                                 "	border-radius: 12px;\n"
                                                 "	color: rgb(0, 0, 0);\n"
                                                 "	padding-left: 20px;\n"
                                                 "	padding-right: 20px; \n"
                                                 "	background-color: rgb(255, 255, 255);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:hover {\n"
                                                 "	border: 2px solid rgb(0, 165, 230);\n"
                                                 "}\n"
                                                 "\n"
                                                 "QLineEdit:focus{\n"
                                                 "	border: 2px solid rgb(85, 170, 255);\n"
                                                 "	\n"
                                                 "	background-color: rgb(198, 198, 198);\n"
                                                 "}")
        self.label_hyphen1 = QLabel(self.Backgrondframe)
        self.label_hyphen1.setObjectName(u"label_hyphen1")
        self.label_hyphen1.setGeometry(QRect(280, 270, 51, 51))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(20)
        self.label_hyphen1.setFont(font4)
        self.label_hyphen1.setStyleSheet(u"color: rgb(238, 238, 238);\n"
                                         "background: transparent;")
        self.label_hyphen1.setAlignment(Qt.AlignCenter)
        self.label_hyphen2 = QLabel(self.Backgrondframe)
        self.label_hyphen2.setObjectName(u"label_hyphen2")
        self.label_hyphen2.setGeometry(QRect(420, 270, 51, 51))
        self.label_hyphen2.setFont(font4)
        self.label_hyphen2.setStyleSheet(u"color: rgb(238, 238, 238);\n"
                                         "background: transparent;")
        self.label_hyphen2.setAlignment(Qt.AlignCenter)
        self.label_jobPosition = QLabel(self.Backgrondframe)
        self.label_jobPosition.setObjectName(u"label_jobPosition")
        self.label_jobPosition.setGeometry(QRect(590, 250, 121, 101))
        self.label_jobPosition.setFont(font3)
        self.label_jobPosition.setStyleSheet(u"color: rgb(238, 238, 238);\n"
                                             "background: transparent;")
        self.label_jobPosition.setAlignment(Qt.AlignCenter)
        self.pushButton_save = QPushButton(self.Backgrondframe)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setGeometry(QRect(40, 30, 91, 51))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.pushButton_save.setFont(font5)
        self.pushButton_save.setStyleSheet(u"QPushButton {\n"
                                           "	border: 3px solid rgb(0, 108, 154);\n"
                                           "	border-radius: 10px;\n"
                                           "	\n"
                                           "	color: rgb(255, 175, 46);\n"
                                           "	padding-left: 5px;\n"
                                           "	padding-right: 5px; \n"
                                           "	background-color: rgb(55, 55, 55);\n"
                                           "}\n"
                                           "")
        self.pushButton_save.setAutoDefault(False)
        self.label_errorEmail = QLabel(self.Backgrondframe)
        self.label_errorEmail.setObjectName(u"label_errorEmail")
        self.label_errorEmail.setGeometry(QRect(110, 240, 751, 21))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(8)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_errorEmail.setFont(font6)
        self.label_errorEmail.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                            "background: transparent;\n"
                                            "")
        self.label_errorEmail.setAlignment(Qt.AlignCenter)
        self.tableWidget_display = QTableWidget(self.Backgrondframe)
        self.tableWidget_display.setObjectName(u"tableWidget_display")
        self.tableWidget_display.setGeometry(QRect(70, 380, 841, 291))
        font7 = QFont()
        font7.setPointSize(15)
        self.tableWidget_display.setFont(font7)
        self.tableWidget_display.setStyleSheet(u"border: 3px solid rgb(0, 108, 154);\n"
                                               "border-radius: 10px;\n"
                                               "background-color: qlineargradient(spread:pad, x1:0.528, y1:0, x2:0.465909, y2:1, stop:0 rgba(92, 179, 255, 255), stop:0.982955 rgba(218, 218, 218, 255), stop:1 rgba(225, 225, 225, 255));\n"
                                               "color: rgb(0, 0, 0);")
        self.pushButton_clear = QPushButton(self.Backgrondframe)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setGeometry(QRect(840, 30, 91, 51))
        self.pushButton_clear.setFont(font5)
        self.pushButton_clear.setStyleSheet(u"QPushButton {\n"
                                            "	border: 3px solid rgb(0, 108, 154);\n"
                                            "	border-radius: 10px;\n"
                                            "	\n"
                                            "	color: rgb(255, 175, 46);\n"
                                            "	padding-left: 5px;\n"
                                            "	padding-right: 5px; \n"
                                            "	background-color: rgb(55, 55, 55);\n"
                                            "}\n"
                                            "")
        self.pushButton_clear.setAutoDefault(False)
        self.label_errorFirstname = QLabel(self.Backgrondframe)
        self.label_errorFirstname.setObjectName(u"label_errorFirstname")
        self.label_errorFirstname.setGeometry(QRect(60, 150, 371, 21))
        self.label_errorFirstname.setFont(font6)
        self.label_errorFirstname.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                "background: transparent;\n"
                                                "")
        self.label_errorFirstname.setAlignment(Qt.AlignCenter)
        self.label_errorLastname = QLabel(self.Backgrondframe)
        self.label_errorLastname.setObjectName(u"label_errorLastname")
        self.label_errorLastname.setGeometry(QRect(540, 150, 381, 21))
        self.label_errorLastname.setFont(font6)
        self.label_errorLastname.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                               "background: transparent;\n"
                                               "")
        self.label_errorLastname.setAlignment(Qt.AlignCenter)
        self.label_errorPhonenumber = QLabel(self.Backgrondframe)
        self.label_errorPhonenumber.setObjectName(u"label_errorPhonenumber")
        self.label_errorPhonenumber.setGeometry(QRect(30, 340, 541, 21))
        self.label_errorPhonenumber.setFont(font6)
        self.label_errorPhonenumber.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                  "background: transparent;\n"
                                                  "")
        self.label_errorPhonenumber.setAlignment(Qt.AlignCenter)
        self.label_errorPhonenumber3 = QLabel(self.Backgrondframe)
        self.label_errorPhonenumber3.setObjectName(u"label_errorPhonenumber3")
        self.label_errorPhonenumber3.setGeometry(QRect(460, 270, 121, 61))
        self.label_errorPhonenumber3.setFont(font6)
        self.label_errorPhonenumber3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                   "background-color: transparent;")
        self.label_errorPhonenumber3.setAlignment(Qt.AlignCenter)
        self.label_errorPhonenumber2 = QLabel(self.Backgrondframe)
        self.label_errorPhonenumber2.setObjectName(u"label_errorPhonenumber2")
        self.label_errorPhonenumber2.setGeometry(QRect(320, 270, 111, 61))
        self.label_errorPhonenumber2.setFont(font6)
        self.label_errorPhonenumber2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                   "background-color: transparent;")
        self.label_errorPhonenumber2.setAlignment(Qt.AlignCenter)
        self.label_errorPhonenumber1 = QLabel(self.Backgrondframe)
        self.label_errorPhonenumber1.setObjectName(u"label_errorPhonenumber1")
        self.label_errorPhonenumber1.setGeometry(QRect(180, 270, 111, 61))
        self.label_errorPhonenumber1.setFont(font6)
        self.label_errorPhonenumber1.setStyleSheet(u"color: rgb(255, 255, 255);\n"
                                                   "background-color: transparent;")
        self.label_errorPhonenumber1.setAlignment(Qt.AlignCenter)
        self.label_errorPhonenumber1.raise_()
        self.label_errorPhonenumber2.raise_()
        self.label_mainTitle.raise_()
        self.lineEdit_firstName.raise_()
        self.label_firstName.raise_()
        self.label_emailAddress.raise_()
        self.lineEdit_emailAddress.raise_()
        self.lineEdit_lastName.raise_()
        self.label_lastName.raise_()
        self.label_phoneNumber.raise_()
        self.comboBox_jobPosition.raise_()
        self.lineEdit_phoneNumber1.raise_()
        self.lineEdit_phoneNumber2.raise_()
        self.label_hyphen1.raise_()
        self.label_hyphen2.raise_()
        self.label_jobPosition.raise_()
        self.pushButton_save.raise_()
        self.label_errorEmail.raise_()
        self.tableWidget_display.raise_()
        self.pushButton_clear.raise_()
        self.label_errorFirstname.raise_()
        self.label_errorLastname.raise_()
        self.label_errorPhonenumber.raise_()
        self.label_errorPhonenumber3.raise_()
        self.lineEdit_phoneNumber3.raise_()

        self.horizontalLayout.addWidget(self.Backgrondframe)

        ContactListMainScreen.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ContactListMainScreen)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1000, 21))
        ContactListMainScreen.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ContactListMainScreen)
        self.statusbar.setObjectName(u"statusbar")
        ContactListMainScreen.setStatusBar(self.statusbar)

        self.retranslateUi(ContactListMainScreen)

        QMetaObject.connectSlotsByName(ContactListMainScreen)

    # setupUi

    def retranslateUi(self, ContactListMainScreen: None) -> None:
        """
        Constructor to load up the Contact List Main Screen correctly
        :param self: the instance of the __init__ class
        :param ContactListMainScreen: The Contact List Main Screen
        :return: None
        """
        ContactListMainScreen.setWindowTitle(QCoreApplication.translate("ContactListMainScreen", u"MainWindow", None))
        self.label_mainTitle.setText(QCoreApplication.translate("ContactListMainScreen",
                                                                u"<html><head/><body><p><span style=\" font-weight:600;\">EMPLOYEE</span> | CONTACT LIST</p></body></html>",
                                                                None))
        self.lineEdit_firstName.setPlaceholderText(
            QCoreApplication.translate("ContactListMainScreen", u"Enter Your First Name Here", None))
        self.label_firstName.setText(
            QCoreApplication.translate("ContactListMainScreen", u"<html><head/><body><p>First Name:</p></body></html>",
                                       None))
        self.label_emailAddress.setText(QCoreApplication.translate("ContactListMainScreen",
                                                                   u"<html><head/><body><p>Email Address:</p></body></html>",
                                                                   None))
        self.lineEdit_emailAddress.setPlaceholderText(
            QCoreApplication.translate("ContactListMainScreen", u"Input Your Email Address Here", None))
        self.lineEdit_lastName.setPlaceholderText(
            QCoreApplication.translate("ContactListMainScreen", u"Enter Your Last Name Here", None))
        self.label_lastName.setText(
            QCoreApplication.translate("ContactListMainScreen", u"<html><head/><body><p>Last Name:</p></body></html>",
                                       None))
        self.label_phoneNumber.setText(QCoreApplication.translate("ContactListMainScreen",
                                                                  u"<html><head/><body><p>Phone Number:</p></body></html>",
                                                                  None))
        self.comboBox_jobPosition.setItemText(0, QCoreApplication.translate("ContactListMainScreen", u"Receptionist",
                                                                            None))
        self.comboBox_jobPosition.setItemText(1, QCoreApplication.translate("ContactListMainScreen", u"Web Developer",
                                                                            None))
        self.comboBox_jobPosition.setItemText(2, QCoreApplication.translate("ContactListMainScreen", u"Data Analyst",
                                                                            None))
        self.comboBox_jobPosition.setItemText(3,
                                              QCoreApplication.translate("ContactListMainScreen", u"Software Engineer",
                                                                         None))
        self.comboBox_jobPosition.setItemText(4, QCoreApplication.translate("ContactListMainScreen", u"Designer", None))
        self.comboBox_jobPosition.setItemText(5,
                                              QCoreApplication.translate("ContactListMainScreen", u"Marketing Manager",
                                                                         None))
        self.comboBox_jobPosition.setItemText(6,
                                              QCoreApplication.translate("ContactListMainScreen", u"Illustrator", None))
        self.comboBox_jobPosition.setItemText(7, QCoreApplication.translate("ContactListMainScreen",
                                                                            u"Network Administrator", None))
        self.comboBox_jobPosition.setItemText(8,
                                              QCoreApplication.translate("ContactListMainScreen", u"Graphic Designer",
                                                                         None))
        self.comboBox_jobPosition.setItemText(9,
                                              QCoreApplication.translate("ContactListMainScreen", u"Brand Ambassador",
                                                                         None))

        self.comboBox_jobPosition.setCurrentText("")
        self.comboBox_jobPosition.setPlaceholderText(
            QCoreApplication.translate("ContactListMainScreen", u"Select Job Title Here", None))
        self.lineEdit_phoneNumber1.setPlaceholderText(QCoreApplication.translate("ContactListMainScreen", u"###", None))
        self.lineEdit_phoneNumber2.setPlaceholderText(QCoreApplication.translate("ContactListMainScreen", u"###", None))
        self.lineEdit_phoneNumber3.setPlaceholderText(
            QCoreApplication.translate("ContactListMainScreen", u"####", None))
        self.label_hyphen1.setText(
            QCoreApplication.translate("ContactListMainScreen", u"<html><head/><body><p>-</p></body></html>", None))
        self.label_hyphen2.setText(
            QCoreApplication.translate("ContactListMainScreen", u"<html><head/><body><p>-</p></body></html>", None))
        self.label_jobPosition.setText(QCoreApplication.translate("ContactListMainScreen",
                                                                  u"<html><head/><body><p>Job Position:</p></body></html>",
                                                                  None))
        self.pushButton_save.setText(QCoreApplication.translate("ContactListMainScreen", u"SAVE", None))
        self.label_errorEmail.setText("")
        self.pushButton_clear.setText(QCoreApplication.translate("ContactListMainScreen", u"CLEAR", None))
        self.label_errorFirstname.setText("")
        self.label_errorLastname.setText("")
        self.label_errorPhonenumber.setText("")
        self.label_errorPhonenumber3.setText("")
        self.label_errorPhonenumber2.setText("")
        self.label_errorPhonenumber1.setText("")
    # retranslateUi
