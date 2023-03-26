from calculator_pretty import Ui_Dialog
import sys
from PyQt5.QtWidgets import *
import math


class Main(QDialog, Ui_Dialog):

    
    def __init__(self):
        self.current_text = ""
        self.numbers_set = []
        self.operations = []
        self.flag = False
        super().__init__()
        self.setupUi(self)
        self.pushButton_1.clicked.connect(lambda: self.buttons("1"))
        self.pushButton_2.clicked.connect(lambda: self.buttons("2"))
        self.pushButton_3.clicked.connect(lambda: self.buttons("3"))
        self.pushButton_4.clicked.connect(lambda: self.buttons("4"))
        self.pushButton_5.clicked.connect(lambda: self.buttons("5"))
        self.pushButton_6.clicked.connect(lambda: self.buttons("6"))
        self.pushButton_7.clicked.connect(lambda: self.buttons("7"))
        self.pushButton_8.clicked.connect(lambda: self.buttons("8"))
        self.pushButton_9.clicked.connect(lambda: self.buttons("9"))
        self.pushButton_0.clicked.connect(lambda: self.buttons("0"))
        self.pushButton_plus.clicked.connect(lambda: self.operation("plus"))
        self.pushButton_minus.clicked.connect(lambda: self.operation("minus"))
        self.pushButton_division.clicked.connect(lambda: self.operation("division"))
        self.pushButton_multi.clicked.connect(lambda: self.operation("multi"))
        self.pushButton_power.clicked.connect(lambda: self.operation("power"))
        self.pushButton_root.clicked.connect(lambda: self.operation("root"))
        self.pushButton_equal.clicked.connect(lambda: self.equal())
        self.pushButton_clear.clicked.connect(lambda: self.clear())
        self.pushButton_clearAll.clicked.connect(lambda: self.clearAll())
        
    def test(self):
        print("-" , self.numbers_set)
        print("-" , self.operations)
        print(20*"-")

    
    def buttons(self, evt):
        if self.flag == True:
            self.flag = False
            self.clearAll()
        
        self.current_text += evt
        self.textEdit.setText(self.current_text)

    def clear(self):
        self.textEdit.setText("")
        self.current_text = ""

    def clearAll(self):
        self.clear()
        self.numbers_set = []
        self.operations = []

    def operation(self, which_operation):
        shiet = int(self.current_text)
        self.numbers_set.append(shiet)
        self.operations.append(which_operation)
        self.clear()

        self.test()
        
    
    def equal(self):
        if self.current_text != "" :
            self.numbers_set.append(int(self.current_text))
        self.test()

        if(self.operations[0] == "plus"):
            output = self.numbers_set[0] + self.numbers_set[1]
        elif(self.operations[0] == "minus"):
            output = self.numbers_set[0] - self.numbers_set[1]
        elif(self.operations[0] == "division"):
            if self.numbers_set[1] == 0:
                self.textEdit.setText("Co ty co ty")
                return
            output = self.numbers_set[0] / self.numbers_set[1]
        elif(self.operations[0] == "multi"):
            output = self.numbers_set[0] * self.numbers_set[1]
        elif(self.operations[0] == "root"):
            output = format(math.sqrt(self.numbers_set[0]), '.6f')
        elif(self.operations[0] == "power"):
            output = self.numbers_set[0] ** self.numbers_set[1]
        output = str(output)
        self.textEdit.setText(output)
        
        self.flag = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
