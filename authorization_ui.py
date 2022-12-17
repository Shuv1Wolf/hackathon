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
        self.regist_button.clicked.connect(self.registr)
        self.DB = Authorization(r"DB\authorization.db")
    def agree(self):
        self.check(self.login_place.text(), self.password_place.text())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Enter:
            self.agree()

    def registr(self):

        print('Зарегестрировано')
        print('Логин:', self.login_place.text())
        print('Пароль:', self.password_place.text())
        temp = tuple((self.login_place.text(), self.password_place.text()))
        reg = self.DB.registration(table='users', user_log=temp[0], password=temp[1])


    def check(self, log, pas):
        flag = self.DB.check('admin', log, pas)
        flag1 = self.DB.check('users',log, pas)
        if flag:
            print('Успешно')
            self.massage.setText('')
            mainWindowApplication()
            self.close()
        elif flag1:
            print('Успешно')
            self.massage.setText('')
            mainWindowApplication()
            self.close()
        else:
            print('Отклонено')
            self.massage.setText('Отклонено')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainUI.ui', self)

def application():
    app = QApplication(sys.argv)
    global enterWin
    global mainWin
    global orderWin
    global orderListWin
    global goodsWin
    enterWIn = EnterWindow()
    enterWIn .show()
    mainWin = MainWindow()
    sys.exit(app.exec_())
def mainWindowApplication():
    mainWin.show()

if __name__ == '__main__':
    application()
