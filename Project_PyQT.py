import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

class Mistake(QMainWindow):
    def __init__(self):
        super(Mistake, self).__init__()
        self.setWindowTitle('Mistake')
        uic.loadUi("mistake.ui", self)

class Window2(QMainWindow):
    def __init__(self, *args):
        super(Window2, self).__init__()
        self.setWindowTitle('Window2')
        uic.loadUi("svodka_project.ui", self)
        self.init(args[0])

    def init(self, res):
        self.name.setText(res[2])
        self.vin.setText(res[3])
        self.power.setText(res[4])
        self.workV.setText(res[5])
        self.year.setText(res[6])
        self.color.setText(res[7])
        self.people.setText(res[8])
        self.weight.setText(res[9])
        self.dtp.setText(res[10])
        self.taxi.setText(res[11])


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("Project_PyQT.ui", self)
        self.pushButton.clicked.connect(self.search_number)
        self.con = sqlite3.connect("project.db")

    def search_number(self):
        cur = self.con.cursor()
        query = f"SELECT * FROM Base_cars WHERE number = '{self.number.text()}' and reg = '{self.reg.text()}'"
        res = cur.execute(query).fetchall()
        if res:
            self.setWindowTitle('Window2')
            uic.loadUi("svodka_project.ui", self)
            self.Window2 = Window2(res[0])
            self.Window2.show()
        else:
            self.mistake = Mistake()
            self.mistake.show()

    def search_vin_number(self):
        cur = self.con.cursor()
        q = f"SELECT * FROM Base_cars WHERE VIN_number = '{self.vin_number.text()}'"
        res = cur.execute(q).fetchall()
        if len(res) > 1:
            self.setWindowTitle('Window2')
            uic.loadUi("svodka_project.ui", self)
            self.Window2 = Window2(res[0])
            self.Window2.show()
        else:
            self.mistake = Mistake()
            self.mistake.show()

    def adm_menu(self):
        self.pushButton.clicked.connect(self.admin)
        self.Admin_menu = Admin_menu()
        self.Admin_menu.show()

class Admin_menu(QMainWindow):
    def __init__(self):
        super(Admin_menu, self).__init__()
        uic.loadUi("admin_menu.ui", self)
        self.pushButton.clicked.connect(self.admin)
        cur = self.con.cursor()

    def delete_number(self):
        self.pushButton.clicked.connect(self.delete)
        cur = self.con.cursor()
        query = f"SELECT * FROM Base_cars WHERE number = '{self.number.text()}' and reg = '{self.reg.text()}'"
        res = cur.execute(query).fetchall()
        if res:
            f"DELETE FROM table WHERE {res}"

    def addnumber(self):
        self.pushButton.clicked.connect(self.add)
        cur = self.con.cursor()
        if len(self.number.text()) == 6 and 2 <=len(self.reg.text) <= 3:
            self.setWindowTitle('edit')
            uic.loadUi("edit.ui", self)
            self.Add = Add()
            self.Add.show()

    def editnumber(self):
        self.pushButton.clicked.connect(self.redactor)
        cur = self.con.cursor()
        query = f"SELECT * FROM Base_cars WHERE number = '{self.number.text()}' and reg = '{self.reg.text()}'"
        res = cur.execute(query).fetchall()
        if res:
            self.setWindowTitle('Edit')
            uic.loadUi("edit.ui", self)
            self.Window2 = Window2(res[0])
            self.Window2.show()
        else:
            self.mistake = Mistake()
            self.mistake.show()

class Add(QMainWindow):
    def __init__(self):
        super(Add, self).__init__()
        uic.loadUi("edit.ui", self)
        self.pushButton.clicked.connect(self.save)
        self.con = sqlite3.connect("project.db")

    def add_number(self):
        cur = self.con.cursor()
        if self.save.clicked():
            f"INSERT INTO Base_cars (number, reg, name auto, VIN number, power, workingV, year, color, " \
            f"peoples, weight, DTP, taxi) VALUES('{self.number.text()}', '{self.reg.text()}'), '{self.name.text()}', " \
            f"'{self.vin.text()}', '{self.power.text()}', '{self.workV.text()}', '{self.year.text()}', " \
            f"'{self.color.text()}', '{self.people.text()}', '{self.weight.text()}', '{self.dtp.text()}'," \
            f"'{self.taxi.text()}'"

class Edit(QMainWindow):
    def __init__(self):
        super(Edit, self).__init__()
        uic.loadUi("edit.ui", self)
        self.pushButton.clicked.connect(self.save)
        self.con = sqlite3.connect("project.db")

    def edit_number(self):
        cur = self.con.cursor()
        if self.save.clicked():
            f"REPLASE INTO Base_cars (name auto, VIN number, power, workingV, year, color, " \
            f"peoples, weight, DTP, taxi) VALUES('{self.name.text()}', " \
            f"'{self.vin.text()}', '{self.power.text()}', '{self.workV.text()}', '{self.year.text()}', " \
            f"'{self.color.text()}', '{self.people.text()}', '{self.weight.text()}', '{self.dtp.text()}'," \
            f"'{self.taxi.text()}')"

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Window()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())