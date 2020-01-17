from PyQt5 import QtCore, QtWidgets, uic
from PyQt5.uic import loadUi
import sys
import os

#import server_bbb


class rc_p(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        loadUi("uir.ui",self)
        self.setWindowTitle("SERVER CoAP")
        self.start_button.clicked.connect(self.start_button_function)
        self.stop_button.clicked.connect(self.stop_button_function)
        self.refresh_button.clicked.connect(self.refresh_button_function)
        self.data = []
        self.row_number = 0

    def start_button_function(self):
        # execfile("server_bbb.py")
        os.system("python server_bbb.py")
    def stop_button_function(self):
        os.system("pkill -f server_bbb.py")
        #server.exit_function()
    def refresh_button_function(self):
        self.data = server_bbb.get_data
        self.tableWidget.insertRow(row_number)
        column_number = 0
        for result in data:
            self.tableWidget.setItem(self.row_number, column_number, QtWidgets.QTableWidgetItem(str(result)))
            column_number += 1
        self.row_number += 1


app = QtWidgets.QApplication(sys.argv)
window = rc_p()
window.show()
app.exec_()
