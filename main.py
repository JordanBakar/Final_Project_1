import sys
from PyQt5.QtWidgets import *
from PySide2 import QtCore
from PySide2.QtWidgets import *
import pandas as pd

from ui_employee_contact_list import Ui_ContactListMainScreen

import csv

data_list = []


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """
        Constructor to open up the User Interface and link up the save and clear button to this .py file
        :param self: the instance of the __init__ class
        :return: None
        """
        QMainWindow.__init__(self)
        self.ui = Ui_ContactListMainScreen()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.comboBox_jobPosition.setCurrentIndex(0)

        self.show()

        self.ui.pushButton_save.clicked.connect(self.save_clicked)
        self.ui.pushButton_save.clicked.connect(self.ShowDataFile)
        self.ui.pushButton_clear.clicked.connect(self.clear_clicked)

    def save_clicked(self) -> None:
        """
        Method to save correct user input to the .csv file and clear previous errors that occurred. Additionally, it displays any errors that are persistant.
        param self: the instance of the __init__ class
        :return: None
        """
        self.ui.label_errorFirstname.setText("")
        self.ui.label_errorLastname.setText("")
        self.ui.label_errorEmail.setText("")
        self.ui.label_errorPhonenumber.setText("")
        self.ui.label_errorFirstname.setStyleSheet("background-color: transparent;")
        self.ui.label_errorLastname.setStyleSheet("background-color: transparent;")
        self.ui.label_errorEmail.setStyleSheet("background-color: transparent;")
        self.ui.label_errorPhonenumber.setStyleSheet("background-color: transparent;")
        self.ui.label_errorPhonenumber1.setStyleSheet("background-color: transparent;")
        self.ui.label_errorPhonenumber2.setStyleSheet("background-color: transparent;")
        self.ui.label_errorPhonenumber3.setStyleSheet("background-color: transparent;")
        try:
            first_name: str = str(self.ui.lineEdit_firstName.text())
            last_name: str = str(self.ui.lineEdit_lastName.text())
            email_address: str = str(self.ui.lineEdit_emailAddress.text())

            phone_number1: int = self.ui.lineEdit_phoneNumber1.text()
            phone_number2: int = self.ui.lineEdit_phoneNumber2.text()
            phone_number3: int = self.ui.lineEdit_phoneNumber3.text()

            job_position = self.ui.comboBox_jobPosition.currentText()

            allowed_first_name = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'`"
            allowed_last_name = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'`"
            allowed_email_address = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-!@#$%."

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

            if all((ch in allowed_first_name for ch in first_name)) is False:
                raise ValueError

            if all((ch in allowed_last_name for ch in last_name)) is False:
                raise ValueError

            if len(first_name) == 0 or len(last_name) == 0:
                raise ValueError

            if '@' not in email_address:
                raise ValueError

            if '.' not in email_address:
                raise ValueError

            if len(email_address) == 0:
                raise ValueError

            if all((ch in allowed_email_address for ch in email_address)) is False:
                raise ValueError

            if len(phone_number1) != 3 or len(phone_number2) != 3 or len(phone_number3) != 4:
                raise ValueError

            if not phone_number1.isnumeric() or not phone_number2.isnumeric() or not phone_number3.isnumeric():
                raise ValueError

            # for letters in first_name:
            #     if ((ord(letters) >= 0 and ord(letters) <= 38) or (ord(letters) >= 40 and ord(letters) >= 44) or (
            #             ord(letters) >= 46 and ord(letters) <= 64) or (ord(letters) >= 91 and ord(letters) <= 95) or (
            #             ord(letters) >= 123 and ord(letters) <= 127)):
            #         raise ValueError

            # for letters in last_name:
            #     if ((ord(letters) >= 0 and ord(letters) <= 38) or (ord(letters) >= 40 and ord(letters) >= 44) or (
            #             ord(letters) >= 46 and ord(letters) <= 64) or (ord(letters) >= 91 and ord(letters) <= 95) or (
            #             ord(letters) >= 123 and ord(letters) <= 127)):
            #         raise ValueError

            with open("contact_database.csv", "a", newline="") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(empty_list)

        except ValueError:
            if all((ch in allowed_first_name for ch in first_name)) is False:
                self.ui.label_errorFirstname.setStyleSheet("background-color: red;")
                self.ui.label_errorFirstname.setText(
                    "Invalid First Name! Make sure there is no numeric & special values.")

            if all((ch in allowed_last_name for ch in last_name)) is False:
                self.ui.label_errorLastname.setStyleSheet("background-color: red;")
                self.ui.label_errorLastname.setText(
                    "Invalid Last Name! Make sure there is no numeric and special values.")

            if len(first_name) == 0:
                self.ui.label_errorFirstname.setStyleSheet("background-color: red;")
                self.ui.label_errorFirstname.setText("Invalid First Name! No input was entered.")

            if len(last_name) == 0:
                self.ui.label_errorLastname.setStyleSheet("background-color: red;")
                self.ui.label_errorLastname.setText("Invalid Last Name! No input was entered.")

            if '@' not in email_address:
                self.ui.label_errorEmail.setStyleSheet("background-color: red;")
                self.ui.label_errorEmail.setText(
                    "Invalid Email! Please check if there is an '@' sign and reenter your email address. Email can be alphanumeric.")

            if '.' not in email_address:
                self.ui.label_errorEmail.setStyleSheet("background-color: red;")
                self.ui.label_errorEmail.setText(
                    "Invalid Email! Please check if there is an '.' sign and reenter your email address. Email can be alphanumeric.")

            if all((ch in allowed_email_address for ch in email_address)) is False:
                self.ui.label_errorEmail.setStyleSheet("background-color: red;")
                self.ui.label_errorEmail.setText(
                    "Invalid Email! Please check if you are using improper special characters such as '()*&^:~`?/'. Email can be alphanumeric.")

            if len(email_address) == 0:
                self.ui.label_errorEmail.setStyleSheet("background-color: red;")
                self.ui.label_errorEmail.setText(
                    "Invalid Email! No input was entered. Email can be alphanumeric.")

            if len(phone_number1) != 3 or not phone_number1.isnumeric():
                self.ui.label_errorPhonenumber1.setStyleSheet("background-color: red;")
                self.ui.label_errorPhonenumber.setStyleSheet("background-color: red;")
                self.ui.label_errorPhonenumber.setText(
                    "Invalid Phone Number! Make sure it follows this format (###-###-####) and is numeric.")
            if len(phone_number2) != 3 or not phone_number2.isnumeric():
                self.ui.label_errorPhonenumber2.setStyleSheet("background-color: red;")
                self.ui.label_errorPhonenumber.setStyleSheet("background-color: red;")
                self.ui.label_errorPhonenumber.setText(
                    "Invalid Phone Number! Make sure it follows this format (###-###-####) and is numeric.")
            if len(phone_number3) != 4 or not phone_number3.isnumeric():
                self.ui.label_errorPhonenumber3.setStyleSheet("background-color: red;")
                self.ui.label_errorPhonenumber.setStyleSheet("background-color: red;")
                self.ui.label_errorPhonenumber.setText(
                    "Invalid Phone Number! Make sure it follows this format (###-###-####) and is numeric.")


        except RuntimeError:
            print("Program has crashed and needs to be restarted")

    def ShowDataFile(self) -> None:
        """
        Method that presents the .csv file in the GUI with real-time updates and additions.
        param self: the instance of the __init__ class
        :return: None
        """
        self.all_data = pd.read_csv("contact_database.csv")
        self.ui.tableWidget_display.setColumnCount(len(self.all_data.columns))
        self.ui.tableWidget_display.setRowCount(len(self.all_data.index))
        self.ui.tableWidget_display.setHorizontalHeaderLabels(self.all_data.columns)

        for i in range(len(self.all_data.index)):
            for j in range(len(self.all_data.columns)):
                self.ui.tableWidget_display.setItem(i, j, QTableWidgetItem(str(self.all_data.iat[i, j])))

        self.ui.tableWidget_display.resizeColumnsToContents()
        self.ui.tableWidget_display.resizeRowsToContents()

    def clear_clicked(self) -> None:
        """
        Method to clear all user input in the GUI to its original state and clears all previous errors that occurred prior.
        param self: the instance of the __init__ class
        :return: None
        """
        self.ui.lineEdit_firstName.setText("")
        self.ui.lineEdit_lastName.setText("")
        self.ui.lineEdit_emailAddress.setText("")
        self.ui.lineEdit_phoneNumber1.setText("")
        self.ui.lineEdit_phoneNumber2.setText("")
        self.ui.lineEdit_phoneNumber3.setText("")
        self.ui.comboBox_jobPosition.setCurrentIndex(0)
        self.ui.label_errorFirstname.setText("")
        self.ui.label_errorLastname.setText("")
        self.ui.label_errorEmail.setText("")
        self.ui.label_errorPhonenumber.setText("")
        self.ui.label_errorFirstname.setStyleSheet("background-color: transparent;")
        self.ui.label_errorLastname.setStyleSheet("background-color: transparent;")
        self.ui.label_errorEmail.setStyleSheet("background-color: transparent;")
        self.ui.label_errorPhonenumber.setStyleSheet("background-color: transparent;")
        self.ui.label_errorPhonenumber1.setStyleSheet("background-color: transparent;")
        self.ui.label_errorPhonenumber2.setStyleSheet("background-color: transparent;")
        self.ui.label_errorPhonenumber3.setStyleSheet("background-color: transparent;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
