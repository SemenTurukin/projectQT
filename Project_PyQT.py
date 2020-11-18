import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("Project_PyQT-Lite.ui", self)
        self.pushButton.clicked.connect(self.search_number)
        self.con = sqlite3.connect("Project.db")

    def search_number(self):
        cur = self.con.cursor()
        query = f"SELECT * FROM Base_cars WHERE number = '{self.number.text()}' and reg = '{self.reg.text()}'"
        print(query)
        res = cur.execute(query).fetchall()
        print(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec_())