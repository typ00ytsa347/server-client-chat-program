from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(324, 336)
        self.ipAddressLineEdit = QtWidgets.QLineEdit(Form)
        self.ipAddressLineEdit.setGeometry(QtCore.QRect(160, 40, 145, 30))
        self.ipAddressLineEdit.setObjectName("hostTextEdit")
        self.portLineEdit = QtWidgets.QLineEdit(Form)
        self.portLineEdit.setGeometry(QtCore.QRect(160, 80, 145, 31))
        self.portLineEdit.setObjectName("portTextEdit")
        self.nickNameLineEdit = QtWidgets.QLineEdit(Form)
        self.nickNameLineEdit.setGeometry(QtCore.QRect(160, 140, 145, 31))
        self.nickNameLineEdit.setObjectName("nameTextEdit")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(40, 40, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(40, 80, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(40, 140, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(115, 200, 90, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(215, 200, 90, 30))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Connection")
        self.label.setText(_translate("Form", "IP Address"))
        self.label_2.setText(_translate("Form", "Port"))
        self.label_3.setText(_translate("Form", "Nick Name"))
        self.pushButton.setText(_translate("Form", "Connect"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))