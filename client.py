from ipaddress import ip_address
from PyQt5 import QtCore, QtWidgets
from client_gui import connection, chat

import sys
import socket


class ReceiveThread(QtCore.QThread):
    signal = QtCore.pyqtSignal(str)

    def __init__(self, client_socket):
        super(ReceiveThread, self).__init__()
        self.client_socket = client_socket

    def run(self):
        while True:
            self.receive_message()

    def receive_message(self):
        message = self.client_socket.recv(1024)
        message = message.decode()

        print(message)
        self.signal.emit(message)


class Client(object):
    def __init__(self):
        self.tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        self.messages = []
        self.mainWindow = QtWidgets.QMainWindow()

        # add widgets to the connection window
        self.connectWidget = QtWidgets.QWidget(self.mainWindow)
        self.chatWidget = QtWidgets.QWidget(self.mainWindow)

        self.chatWidget.setHidden(True)
        self.chat_ui = chat.Ui_Form()
        self.chat_ui.setupUi(self.chatWidget)
        self.chat_ui.pushButton.clicked.connect(self.send_message)

        self.connect_ui = connection.Ui_Form()
        self.connect_ui.setupUi(self.connectWidget)
        self.connect_ui.pushButton.clicked.connect(self.btn_connect_clicked)

        self.mainWindow.setGeometry(QtCore.QRect(480, 260, 360, 250))
        self.mainWindow.show()

        
    def btn_connect_clicked(self):
        ip_address = self.connect_ui.ipAddressLineEdit.text()
        port = int(self.connect_ui.portLineEdit.text())
        nickname = self.connect_ui.nickNameLineEdit.text()

        if self.connect(ip_address, port, nickname):
            self.connectWidget.setHidden(True)
            self.chatWidget.setVisible(True)

            self.recv_thread = ReceiveThread(self.tcp_client)
            self.recv_thread.signal.connect(self.show_message)
            self.recv_thread.start()
            print("[INFO] recv thread started")


    def show_message(self, message):
        self.chat_ui.textBrowser.append(message)
        

    def connect(self, host, port, nickname):

        try:
            self.tcp_client.connect((host, port))
            self.tcp_client.send(nickname.encode())

            print("[INFO] Connected to server")

            return True
        except Exception as e:
            error = "Unable to connect to server \n'{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Connection Error", error)
            self.connect_ui.ipAddressLineEdit.clear()
            self.connect_ui.portLineEdit.clear()
            
            return False
        

    def send_message(self):
        message = self.chat_ui.textEdit.toPlainText()
        self.chat_ui.textBrowser.append("Me: " + message)

        print("sent: " + message)

        try:
            self.tcp_client.send(message.encode())
        except Exception as e:
            error = "Unable to send message '{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Server Error", error)
        self.chat_ui.textEdit.clear()


    def show_error(self, error_type, message):
        errorDialog = QtWidgets.QMessageBox()
        errorDialog.setText(message)
        errorDialog.setWindowTitle(error_type)
        errorDialog.setStandardButtons(QtWidgets.QMessageBox.Ok)
        errorDialog.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    c = Client()
    sys.exit(app.exec())