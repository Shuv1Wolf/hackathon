from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
import sys


def check(log, pas):
    base = (('Kolya', '12354'), ('Misha', '0011'))
    if (log, pas) in base:
        print('Успешно')
    else:
        print('Отклонено')


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('enter.ui', self)
        self.agree_button.clicked.connect(self.agree)

    def agree(self):
        check(self.login_place.text(), self.password_place.text())

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        if e.key() == Qt.Key_Enter:
            self.agree()


def application():
    app = QApplication(sys.argv)
    window_ = MainWindow()
    window_.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    application()
