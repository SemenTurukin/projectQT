import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Window2(QMainWindow):
    def __init__(self):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        uic.loadUi("svodka_project.ui", self)


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("Project_PyQT-Lite.ui", self)
        self.pushButton.clicked.connect(self.search_number)
        self.con = sqlite3.connect("Project.db")

    def search_number(self):
        cur = self.con.cursor()
        query = f"SELECT * FROM Base_cars WHERE number = '{self.number.text()}' and reg = '{self.reg.text()}'"
        res = cur.execute(query).fetchall()
        if len(res) > 1:
            self.connect(self.show_window_2)
            self.name.setText(res[0])
            self.vin.setText(res[1])
            self.power.setText(res[2])
            self.workV.setText(res[3])
            self.year.setText(res[4])
            self.color.setText(res[5])
            self.people.setText(res[6])
            self.weight.setText(res[7])
            self.dtp.setText(res[8])
            self.taxi.setText(res[9])
        else:
            self.output.setText("Некорректный ввод")

    def show_window_2(self):
        self.w2 = Window2()
        self.w2.show()


    def search_vin_number(self):
        cur = self.con.cursor()
        query = f"SELECT * FROM Base_cars WHERE VIN_number = '{self.vin_number.text()}'"
        print(query)
        res = cur.execute(query).fetchall()
        print(res)

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())