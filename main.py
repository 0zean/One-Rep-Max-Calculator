import sys
import math

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from Ui_Calc import Ui_Dialog
from PyQt5 import QtCore


class calc(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(calc, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("One-Rep Max Calc")
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
    @pyqtSlot()
    def Epley(self):
        if int(self.lineEdit2.text()) > 1:
            orm = int(self.lineEdit1.text()) * (1 + (int(self.lineEdit2.text()) / 30))
        return round(orm, 2)

    def Bryzcki(self):
        orm = int(self.lineEdit1.text()) * (36 / (37 - int(self.lineEdit2.text())))
        return round(orm, 2)

    def Mayhew(self):
        orm = (100 * int(self.lineEdit1.text())) / (52.2 + 41.9 * (math.e ** (-0.055 * int(self.lineEdit2.text()))))
        return round(orm, 2)

    def avg(self):
        try:
            avg = int(5 * round(float(((int(self.Epley()) + int(self.Bryzcki()) + int(self.Mayhew())) / 3)) / 5))
        except:
            avg = "Enter Numbers"
        return avg

    def on_pushButton_clicked(self):
        self.label2.setText("ORM: " + str(self.avg()))
        

app = QApplication(sys.argv)
window = calc()
window.show()
sys.exit(app.exec_())
