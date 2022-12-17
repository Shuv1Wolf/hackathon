from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from authorization import Authorization
import sys


class EnterWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('enter.ui', self)
        self.agree_button.clicked.connect(self.agree)
        self.DB = Authorization(r"DB\authorization.db")
    def agree(self):
        self.check(self.login_place.text(), self.password_place.text())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Enter:
            self.agree()

    def check(self, log, pas):
        flag = self.DB.check('admin', log, pas)
        flag1 = self.DB.check('users',log, pas)
        if flag:
            self.massage.setText('')
            mainWindowApplication()
            self.close()
            mainWin.reg_menu.setEnabled(True)
            mainWin.bases_menu.setEnabled(True)
        elif flag1:
            self.massage.setText('')
            mainWindowApplication()
            self.close()
            mainWin.reg_menu.setEnabled(False)
            mainWin.bases_menu.setEnabled(False)
        else:
            self.massage.setText('Отклонено')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainUI.ui', self)
        self.reg_menu.clicked.connect(self.regWin)

    def regWin(self):
        regWindowApplication()
        self.close()

class RegWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('regist.ui', self)
        self.agree_button.clicked.connect(self.registr)
        self.DB = Authorization(r"DB\authorization.db")
        self.back_button.clicked.connect(self.back)
    def registr(self):
        print('Зарегестрировано')
        print('Логин:', self.login_place.text())
        print('Пароль:', self.password_place.text())
        temp = tuple((self.login_place.text(), self.password_place.text()))
        reg = self.DB.registration(table='users', user_log=temp[0], password=temp[1])
    def back(self):
        mainWin.show()
        self.close()
def application():
    app = QApplication(sys.argv)
    global enterWin
    global mainWin
    global orderWin
    global orderListWin
    global goodsWin
    global regWin
    regWin = RegWindow()
    enterWIn = EnterWindow()
    enterWIn.show()
    mainWin = MainWindow()
    sys.exit(app.exec_())
def mainWindowApplication():
    mainWin.show()
def regWindowApplication():
    regWin.show()

if __name__ == '__main__':
    application()
