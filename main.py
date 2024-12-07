import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from mainUI import MainUI
from addEditCoffeeForm import addEditCoffeeFormUI

class MyWidget(QMainWindow, MainUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.run)
        self.initUI()

    def initUI(self):
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        res = self.connection.cursor().execute("""SELECT * FROM coffee""").fetchall()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def run(self):
        self.AddWidget = AddWidget()
        self.AddWidget.show()
        self.close()

    def closeEvent(self, event):
        self.connection.close()


class AddWidget(QMainWindow, addEditCoffeeFormUI):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.connection = sqlite3.connect("coffee.sqlite")
        self.pushButton.clicked.connect(self.run)
        self.backButton.clicked.connect(self.back)

    def run(self):
        name = self.nameEdit.text()
        step = self.stepEdit.text()
        line = self.lineEdit.text()
        description = self.descriptionEdit.text()
        price = self.priceEdit.text()
        package = self.packageEdit.text()
        self.connection.cursor().execute(f'''INSERT INTO coffee(variety_name, degree_of_roasting, ground_in_grains, 
        taste_description, price, package_volume) VALUES 
                    (?, ?, ?, ?, ?, ?)''', (name, step, line, description, price, package,))

    def back(self):
        self.MyWidget = MyWidget()
        self.MyWidget.show()
        self.close()

    def closeEvent(self, event):
        self.connection.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())