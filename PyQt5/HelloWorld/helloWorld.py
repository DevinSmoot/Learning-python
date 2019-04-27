import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi

class HelloWorld(QDialog):
    def __init__(self):
        super(HelloWorld,self).__init__()
        loadUi('helloworld.ui',self)
        self.setWindowTitle('My Hello World Program!')
        self.btnHelloWorld.clicked.connect(self.btnHelloWorld_clicked)
        self.btnReset.clicked.connect(self.btnReset_clicked)
    @pyqtSlot()
    def btnHelloWorld_clicked(self):
        self.lblOutput.setText('Hello, world!')

    def btnReset_clicked(self):
        self.lblOutput.setText('')


app=QApplication(sys.argv)
widget=HelloWorld()
widget.show()
sys.exit(app.exec_())

