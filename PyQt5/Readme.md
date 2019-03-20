## PyQT5 QuickStart Guide

This quickstart guide will help you get PyQt5 installed and begin designing a GUI in just minutes.

### References

[QtGui Module](http://pyqt.sourceforge.net/Docs/PyQt4/qtgui.html)
[Python GUI's with PyQt5](https://www.youtube.com/watch?v=ksW59gYEl6Q)
[Create Python GUI Application using PyQt5 Designer with Python 3.6.3](https://www.youtube.com/watch?v=7SrD4l2o-uk)

### Install

> Step 1

Start a command prompt or terminal

> Step 2

Install PyQt5 and PyQt5 tools

```python
python -m pip install pyqt5
python -m pip install pyqt5-tools
```

> Step 3

Locate the Designer

Start an IDLE session or create a short Python script

```python
import site
print (site.getsitepackages())
```

The first path (before the comma) is the Python installation location.
The second path (after the comma) is the site packages folder.
Navigate to the site packages folder. Then open the `pyqt5-tools` folder. In this folder right click the file `designer.exe` and create a shortcut on the desktop.

### Using the Designer

Select `Main Window` and click **Create**.

Design your GUI window by adding widgets and setting properties.

In this example we will save ours as `SomeGUIWindow.ui`.

### Adding your code and tying it all together.

> Step 1

Start a new Python file. For this example we will use `main.py`.

> Step 2

Import required packages.

```python
import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
```

> Step 3

Initiate Window and GUI

```python
class SomeClassName(QDialog): #Begins the window class
     def __init__(self):
          super(SomeClassName,self).__init__()
          loadUi('SomeGUIWindow.ui',self) #Load the premade GUI made in Designer
          self.setWindowTitle('SomeGUIWindow PyQt5 Example') #Set window title
          self.btnOkButton.clicked.connect(self.btnOkButton_clicked) #Connect a button with click function
          @pyqtslot()

     def btnOkButton_clicked(self): #Button clicked function
          self.lblMessage.setText('Welcome: '+self.lineEdit.text()) # Adds a message to a label when the button is clicked;Hence it being in the button clicked function

app=QApplication(sys.argv)
widget=SomeClassName() #Must be the same as the window class above
widget.show() #Shows the widget/window
sys.exit(app.exit_()) #Clean exit
```

Click `Run` menu and select `Run configuration per file`.

Select `Execute in an external system terminal` and click `Run`.
