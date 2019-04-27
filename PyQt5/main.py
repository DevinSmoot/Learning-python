import sys
from PyQt5.QtCore import pyqtSlot #Required for this program
from PyQt5.QtWidgets import QApplication,QDialog #Required for this program
from PyQt5.uic import loadUi #Required for this program
#Any objects used in the Designer will need to be imported for use

class Life2Coding(QDialog): #Create class for eash dialog with name(type)
    def __init__(self): #Create initialization function
        super(Life2Coding,self).__init__() #Intialize using name of dialog class; defined as self
        loadUi('life2coding.ui',self) #Load UI based on filename; defined as self
        self.setWindowTitle('Life2Coding PyQt5 Gui') #Set window title
        self.pushButton.clicked.connect(self.on_pushButton_clicked) #Create button click reference to call function; pushButton is object name; on_pushButton_clicked is function name
    @pyqtSlot() #Used to define a callable object; in this case the function for pushButton
    def on_pushButton_clicked(self): #Create on_pushButton_clicked function
        self.label1.setText('Welcome: '+self.lineEdit.text()) #Sets label1 text message

#Required components to activate dialog window
app=QApplication(sys.argv)
widget=Life2Coding()
widget.show()
sys.exit(app.exec_())
