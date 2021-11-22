"""
Add your GUI code here.


from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
Form, Window = uic.loadUiType("teamproject/dialog.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec()
"""
import json
from teamproject.models import BaselineAlgo
#from PyQt5 import QtWidgets
#from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
import sys
    


#from teamproject.crawler import fetch_data
from teamproject.models import ExperienceAlwaysWins

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

f = open('teamproject/matches.json',)
data = json.load(f)
model = BaselineAlgo(data)
winner = model.predict_winner('VfL Osnabrück', '1. FC Nürnberg')
print(winner)
f.close()



   # second way to start the application     
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
"""
def main():
    """
    Creates and shows the main window.
    """
    # For demo purposes, this is how you could access methods from other
    # modules:
    
    f = open('teamproject/matches.json',)
    data = json.load(f)
    model = BaselineAlgo(data)
    winner = model.predict_winner('VfL Osnabrück', '1. FC Nürnberg')
    print(winner)
    f.close()
    # Add code here to create and initialize window.
    #window()
    class Ui_Dialog(object):
        def setupUi(self, Dialog):
            Dialog.setObjectName("Dialog")
            Dialog.resize(1055, 841) # Set the window size
        
            # create the ok and cancel buttons
            self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
            self.buttonBox.setGeometry(QtCore.QRect(700, 800, 341, 32))
            self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
            self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
            self.buttonBox.setObjectName("buttonBox")
            
            # combobox for the home team
            self.comboBox = QtWidgets.QComboBox(Dialog)
            self.comboBox.setGeometry(QtCore.QRect(60, 80, 301, 61))
            self.comboBox.setObjectName("comboBox")
            self.comboBox.addItem("")
            
            #Combobox 2 for the guest team
            self.comboBox_2 = QtWidgets.QComboBox(Dialog)
            self.comboBox_2.setGeometry(QtCore.QRect(670, 80, 301, 61))
            self.comboBox_2.setObjectName("comboBox_2")
            self.comboBox_2.addItem("")

            #Crawler Button
            self.pushButton = QtWidgets.QPushButton(Dialog)
            self.pushButton.setGeometry(QtCore.QRect(0, 680, 331, 101))
            self.pushButton.setObjectName("Activate Crawler")
            self.pushButton.clicked.connect(self.crawlercall)
            
        
            #Training button
            self.pushButton_2 = QtWidgets.QPushButton(Dialog)
            self.pushButton_2.setGeometry(QtCore.QRect(330, 680, 331, 101))
            self.pushButton_2.setObjectName("Start training")
            self.pushButton_2.clicked.connect(self.trainingcall)
            
            #Show results button
            self.pushButton_3 = QtWidgets.QPushButton(Dialog)
            self.pushButton_3.setGeometry(QtCore.QRect(660, 680, 331, 101))
            self.pushButton_3.setObjectName("Show results")

            #call the retranslate
            self.retranslateUi(Dialog)
            
            #ok button
            self.buttonBox.accepted.connect(Dialog.accept)
            
            #cancel button
            self.buttonBox.rejected.connect(Dialog.reject)
            
            QtCore.QMetaObject.connectSlotsByName(Dialog)
        
        #this will get called when you press the activate crawler button
        def crawlercall(self):
            self.pushButton.setText("Crawler running")
        
        #this will get called when you press the Start training button
        def trainingcall(self):
            self.pushButton_2.setText(str(winner))

        #this will get called when you press the Show results button, I think i will do a popup with the winner.
        def resultscall(self):
            self.pushButton_2.setText("insert winner here")



            
        def retranslateUi(self, Dialog): # Rename all the objects to the desired names
            _translate = QtCore.QCoreApplication.translate
            Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
            self.comboBox.setItemText(0, _translate("Dialog", "Choose the home team"))
            self.pushButton.setText(_translate("Dialog", "Activate Crawler"))
            self.comboBox_2.setItemText(0, _translate("Dialog", "Choose the guest team"))
            self.pushButton_3.setText(_translate("Dialog", "Show results"))
            self.pushButton_2.setText(_translate("Dialog", "Start training"))

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
    
    
    """
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200,200,300,300) # sets the windows x, y, width, height
    win.setWindowTitle("My first window!") # setting the window title
    label = QLabel(win)
    label.setText("my first label")
    label.move(50, 50)  # x, y from top left hand corner.
    win.show()
    sys.exit(app.exec_())
    """
   
