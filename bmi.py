from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import sys
 
class Bmi(QtWidgets.QMainWindow):
    def __init__(self):
        super(Bmi, self).__init__()
        uic.loadUi('bmi.ui', self)
        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):

        if self.lineEdit.text() == '' or self.lineEdit_2.text() == '':
            QtWidgets.QMessageBox.about(self, "BMI", "Type something")            
        else:
            height = float(self.lineEdit.text())
            mass = float(self.lineEdit_2.text())

            bmi = mass / (height*height)
            bmi = round(bmi,2)
            self.outputLabel.setText(str(bmi))
            print('BMI ' + str(bmi))


app = QtWidgets.QApplication([])
win = Bmi()
win.show()
sys.exit(app.exec())
