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
        self.admin.clicked.connect(self.adm_menu)
        self.con = sqlite3.connect("project.db")

    def search_number(self):
        cur = self.con.cursor()
        query = f"SELECT * FROM Base_cars WHERE number = '{self.number.text()}' and reg = '{self.reg.text()}'" \
                f"or VIN_number = '{self.vin_number.text()}'"
        res = cur.execute(query).fetchall()
        if res:
            self.setWindowTitle('Window2')
            uic.loadUi("svodka_project.ui", self)
            self.Window2 = Window2(res[0])
            self.Window2.show()
        else:
            self.mistake = Mistake()
            self.mistake.show()

    def adm_menu(self):
        self.Admin_menu = Admin_menu()
        self.Admin_menu.show()

class Admin_menu(QMainWindow):
    def __init__(self):
        super(Admin_menu, self).__init__()
        uic.loadUi("admin_menu.ui", self)
        self.add.clicked.connect(self.addnumber)
        self.delete_2.clicked.connect(self.delete_number)
        self.redactor.clicked.connect(self.editnumber)
        self.con = sqlite3.connect("project.db")


    def delete_number(self):
        cur = self.con.cursor()
        query = f"SELECT * FROM Base_cars WHERE number = '{self.number.text()}' and reg = '{self.reg.text()}'"
        res = cur.execute(query).fetchall()
        if res:
            f"DELETE FROM table WHERE {res}"
        else:
            self.mistake = Mistake()
            self.mistake.show()

    def addnumber(self):
        if self.number.text() == 6 and 2 <= self.reg.text() <= 3:
            self.setWindowTitle('edit')
            uic.loadUi("edit.ui", self)
            self.Add = Add()
            self.Add.show()

    def editnumber(self):
        query = f"SELECT * FROM Base_cars WHERE number = '{self.number.text()}' and reg = '{self.reg.text()}'"
        cur = self.con.cursor()
        res = cur.execute(query).fetchall()
        if res:
            self.setWindowTitle('Edit')
            uic.loadUi("edit.ui", self)
            self.Edit = Edit()
            self.Edit.show()
        else:
            self.mistake = Mistake()
            self.mistake.show()

class Add(QMainWindow):
    def __init__(self):
        super(Add, self).__init__()
        uic.loadUi("edit.ui", self)
        self.save.clicked.connect(self.add_number)
        self.con = sqlite3.connect("project.db")

    def add_number(self):
        f"INSERT INTO Base_cars (number, reg, name auto, VIN number, power, workingV, year, color, " \
        f"peoples, weight, DTP, taxi) VALUES('{self.number.text()}', '{self.reg.text()}'), '{self.name.text()}', " \
        f"'{self.vin.text()}', '{self.power.text()}', '{self.workV.text()}', '{self.year.text()}', " \
        f"'{self.color.text()}', '{self.people.text()}', '{self.weight.text()}', '{self.dtp.text()}'," \
        f"'{self.taxi.text()}'"

class Edit(QMainWindow):
    def __init__(self):
        super(Edit, self).__init__()
        uic.loadUi("edit.ui", self)
        self.save.clicked.connect(self.edit_number)
        self.con = sqlite3.connect("project.db")
        self.init()

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