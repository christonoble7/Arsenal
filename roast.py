from PyQt5 import QtCore, QtGui, QtWidgets
import random  
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1109, 945)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(570, 230, 361, 251))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(8, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.verticalLayout.addWidget(self.comboBox)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(110, 230, 341, 251))
        self.widget_3.setObjectName("widget_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(100, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(80, 100, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(120, 190, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(360, 650, 361, 141))
        self.widget_4.setObjectName("widget_4")
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setGeometry(QtCore.QRect(60, 50, 211, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(-320, -650, 951, 791))
        self.widget_5.setObjectName("widget_5")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(320, 60, 431, 81))
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(90, 0, 251, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.on_generate_roasts)
  
        self.roasts = [
            "Hey {user_name}, I hope you’re ready to roast yourself at {temperature}. You're really cooking up a storm!",
            "Why did you choose to roast yourself, {user_name}? Because you're already the roast of the day!",
            "Look out, {user_name}! With that temperature, you're either cooking a roast or starting a fire!",
            "If roasting were an Olympic sport, {user_name}, you'd take home the gold at {temperature}!",
            "Cooking at {temperature}? You must be trying to roast your own reputation, {user_name}!",
        ]

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(1, _translate("MainWindow", "RARE"))
        self.comboBox.setItemText(2, _translate("MainWindow", "MEDIUM RARE"))
        self.comboBox.setItemText(3, _translate("MainWindow", "MEDIUM"))
        self.comboBox.setItemText(4, _translate("MainWindow", "WELL DONE"))
        self.label_2.setText(_translate("MainWindow", "ENTER USER NAME "))
        self.label_3.setText(_translate("MainWindow", "ENTER TARGET NAME"))  # This label can be removed if not needed
        self.label_4.setText(_translate("MainWindow", "SET TEMP"))
        self.pushButton.setText(_translate("MainWindow", "GENERATE ROASTS"))
        self.label.setText(_translate("MainWindow", "THE OVEN"))

    def on_generate_roasts(self):
        user_name = self.lineEdit.text()
        temperature = self.comboBox.currentText()  
        if not user_name or not temperature:
            QtWidgets.QMessageBox.warning(None, "Input Error", "Please fill in all fields.")
            return  
        random_roast = random.choice(self.roasts)
        roast_message = random_roast.format(user_name=user_name, temperature=temperature)    
        QtWidgets.QMessageBox.information(None, "Roast Generated", roast_message)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())