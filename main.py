import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
import pandas as pd

from ui_employee_contact_list import Ui_ContactListMainScreen

import csv
data_list = []

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_ContactListMainScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.comboBox_jobPosition.setCurrentIndex(-1)




        self.show()

        self.ui.pushButton_save.clicked.connect(self.save_clicked)
        self.ui.pushButton_save.clicked.connect(self.ShowDataFile)
        self.ui.pushButton_clear.clicked.connect(self.clear_clicked)

    def save_clicked(self):
        try:
            first_name = str(self.ui.lineEdit_firstName.text())
            last_name = str(self.ui.lineEdit_lastName.text())
            email_address = str(self.ui.lineEdit_emailAddress.text())
            phone_number1 = int(self.ui.lineEdit_phoneNumber1.text())
            phone_number2 = int(self.ui.lineEdit_phoneNumber2.text())
            phone_number3 = int(self.ui.lineEdit_phoneNumber3.text())
            job_position = self.ui.comboBox_jobPosition.currentText()

            # if (len(phone_number1) > 3) or (len(phone_number2) > 3) or (len(phone_number3) > 4):
            #     raise ValueError(self.ui.label_information.setText("*** Phone Number must be numeric, with max amounts of values inputed i.e. ###-###-#### ***"))


            display = self.ui.tableWidget_display

            if job_position == 0:
                job_position = "Receptionist"
            elif job_position == 1:
                job_position = "Web Developer"
            elif job_position == 2:
                job_position = "Data Analyst"
            elif job_position == 3:
                job_position = "Software Engineer"
            elif job_position == 4:
                job_position = "Designer"
            elif job_position == 5:
                job_position = "Marketing Manager"
            elif job_position == 6:
                job_position = "Illustrator"
            elif job_position == 7:
                job_position = "Network Administrator"
            elif job_position == 8:
                job_position = "Graphic Designer"
            elif job_position == 9:
                job_position = "Brand Ambassador"

            phone_number = (f'{phone_number1}-{phone_number2}-{phone_number3}')

            empty_list = [first_name, last_name, email_address, phone_number, job_position]

            with open("contact_database.csv", "a", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(empty_list)

        except ValueError:
            self.ui.label_information.setText("*** Please check if you inputted the correct values. Nothing was added to the database. ***\n"
                                              "*** First & Last Name must be letters. Emails can be Alphanumeric or non Alphanumeric. ***\n"
                                              "*** Phone Number must be numeric, with max amounts of values inputed i.e. ###-###-#### ***")



    def ShowDataFile(self):
        self.all_data = pd.read_csv("contact_database.csv")
        self.ui.tableWidget_display.setColumnCount(len(self.all_data.columns))
        self.ui.tableWidget_display.setRowCount(len(self.all_data.index))
        self.ui.tableWidget_display.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(len(self.all_data.index)):
            for j in range(len(self.all_data.columns)):
                self.ui.tableWidget_display.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.ui.tableWidget_display.resizeColumnsToContents()
        self.ui.tableWidget_display.resizeRowsToContents()

    def clear_clicked(self):
        self.ui.lineEdit_firstName.setText("")
        self.ui.lineEdit_lastName.setText("")
        self.ui.lineEdit_emailAddress.setText("")
        self.ui.lineEdit_phoneNumber1.setText("")
        self.ui.lineEdit_phoneNumber2.setText("")
        self.ui.lineEdit_phoneNumber3.setText("")
        self.ui.comboBox_jobPosition.setCurrentIndex(-1)
        self.ui.label_information.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())