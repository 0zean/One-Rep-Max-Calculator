from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 413)
        self.lineEdit1 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit1.setGeometry(QtCore.QRect(240, 100, 113, 20))
        self.lineEdit1.setObjectName("lineEdit1")
        self.lineEdit2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit2.setGeometry(QtCore.QRect(240, 130, 113, 20))
        self.lineEdit2.setObjectName("lineEdit2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 100, 47, 13))
        self.label.setObjectName("label")
        self.label1 = QtWidgets.QLabel(Dialog)
        self.label1.setGeometry(QtCore.QRect(190, 130, 47, 13))
        self.label1.setObjectName("label1")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(240, 160, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.label2 = QtWidgets.QLabel(Dialog)
        self.label2.setGeometry(QtCore.QRect(120, 240, 341, 121))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(22)
        self.label2.setFont(font)
        self.label2.setText("")
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setObjectName("label2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 20, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Arial Narrow")
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Weight"))
        self.label1.setText(_translate("Dialog", "Reps"))
        self.pushButton.setText(_translate("Dialog", "Enter"))
        self.label_2.setText(_translate("Dialog", "One-Rep Max Calculator"))