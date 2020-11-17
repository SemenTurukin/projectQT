import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi("Project_PyQT-Lite.ui", self)

    def search_number(self):
        self.pushButton.clicked.connect(self.select_data)
        num = self.number.setPlainText("SELECT * FROM Base_cars")
        self.con = sqlite3.connect("Project.db")
        cur = self.con.cursor()
        number = self.number
        if self.search.clicked:
            res = cur.execute("""SELECT * FROM Base_cars
                    WHERE number = ? and reg > ?""", (self.number, self.reg)).fetchall()
            self.plainTextEdit.add(res)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec_())