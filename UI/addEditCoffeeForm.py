# Form implementation generated from reading ui file 'addEditCoffeeForm.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class addEditCoffeeFormUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(74, 75, 161, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 130, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 180, 141, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 236, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 340, 131, 16))
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(90, 290, 55, 16))
        self.label_5.setObjectName("label_5")
        self.nameEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.nameEdit.setGeometry(QtCore.QRect(240, 80, 361, 22))
        self.nameEdit.setObjectName("nameEdit")
        self.stepEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.stepEdit.setGeometry(QtCore.QRect(250, 130, 341, 22))
        self.stepEdit.setObjectName("stepEdit")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(250, 180, 361, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.descriptionEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.descriptionEdit.setGeometry(QtCore.QRect(250, 240, 361, 22))
        self.descriptionEdit.setObjectName("descriptionEdit")
        self.priceEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.priceEdit.setGeometry(QtCore.QRect(250, 290, 361, 22))
        self.priceEdit.setObjectName("priceEdit")
        self.packageEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.packageEdit.setGeometry(QtCore.QRect(250, 340, 351, 22))
        self.packageEdit.setObjectName("packageEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 490, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.backButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(80, 490, 75, 24))
        self.backButton.setObjectName("backButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "название:"))
        self.label_2.setText(_translate("MainWindow", "степень обжарки:"))
        self.label_3.setText(_translate("MainWindow", "молотый/в зернах:"))
        self.label_4.setText(_translate("MainWindow", "описание вкуса:"))
        self.label_6.setText(_translate("MainWindow", "Объем упаковки:"))
        self.label_5.setText(_translate("MainWindow", "Цена:"))
        self.pushButton.setText(_translate("MainWindow", "add"))
        self.backButton.setText(_translate("MainWindow", "back"))
