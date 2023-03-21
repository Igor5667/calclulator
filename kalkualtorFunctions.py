from kalkulator import Ui_Dialog
import sys
from PyQt5.QtWidgets import *



class Main(QDialog, Ui_Dialog):

    
    def __init__(self):
        self.cos = ""
        self.arr = []
        self.operation = ""
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.buttons("1"))
        self.pushButton_2.clicked.connect(lambda: self.buttons("2"))
        self.pushButton_3.clicked.connect(lambda: self.buttons("3"))
        self.pushButton_4.clicked.connect(lambda: self.buttons("4"))
        self.pushButton_5.clicked.connect(lambda: self.buttons("5"))
        self.pushButton_6.clicked.connect(lambda: self.buttons("6"))
        self.pushButton_7.clicked.connect(lambda: self.buttons("7"))
        self.pushButton_8.clicked.connect(lambda: self.buttons("8"))
        self.pushButton_9.clicked.connect(lambda: self.buttons("9"))
        self.pushButton_12.clicked.connect(lambda: self.buttons("0"))
        self.pushButton_10.clicked.connect(lambda: self.plus())
        self.pushButton_14.clicked.connect(lambda: self.equal())
        
    def buttons(self, evt):
        self.cos += evt
        self.textEdit.setText(self.cos)

    def plus(self):
        self.arr.append(self.cos)
        self.operation = "plus"
        self.textEdit.setText("")
    def equal(self):
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
