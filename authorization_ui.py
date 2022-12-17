from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from authorization import Authorization
import sys
import getpass
from covertDB import Convert
from work_with_orderDB import Orders


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
        flag1 = self.DB.check('users', log, pas)
        if flag:
            self.massage.setText('')
            mainWindowApplication()
            self.close()
            mainWin.reg_menu.setEnabled(True)
            mainWin.bases_menu.setEnabled(True)
            goodsWin.append_button.setEnabled(True)
        elif flag1:
            self.massage.setText('')
            mainWindowApplication()
            self.close()
            mainWin.reg_menu.setEnabled(False)
            mainWin.bases_menu.setEnabled(False)
            goodsWin.append_button.setEnabled(False)
        else:
            self.massage.setText('Отклонено')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('mainUI.ui', self)
        self.DB = Convert(r"DB\orders.db")
        self.reg_menu.clicked.connect(self.regWin)
        self.order_button.clicked.connect(self.orderWin)
        self.orders_button.clicked.connect(self.ordersWin)
        self.goods_button.clicked.connect(self.goodsWin)
        self.bases_menu.clicked.connect(self.inst)

    def regWin(self):
        regWindowApplication()
        self.close()

    def orderWin(self):
        orderWindowApplication()
        self.close()

    def ordersWin(self):
        orderListWindowApplication()
        self.close()

    def goodsWin(self):
        goodsWindowApplication()
        self.close()

    def inst(self):
        self.DB.convert()


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
        if self.checkBox.checkState():
            reg = self.DB.registration(table='admin', user_log=temp[0], password=temp[1])
            print('admin')
        else:
            reg = self.DB.registration(table='users', user_log=temp[0], password=temp[1])
            print('user')

    def back(self):
        mainWin.show()
        self.close()


class OrderWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('order.ui', self)
        self.back_button.clicked.connect(self.back)

    def back(self):
        mainWin.show()
        self.close()


class OrderListWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('orderList.ui', self)
        self.back_button.clicked.connect(self.back)

    def back(self):
        mainWin.show()
        self.close()


class GoodsWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('goods.ui', self)
        self.back_button.clicked.connect(self.back)
        self.load_button.clicked.connect(self.reload)
        self.append_button.clicked.connect(self.appending)
        self.reload()

    def back(self):
        mainWin.show()
        self.close()

    def reload(self):
        self.goods_list.clear()
        self.LS = Orders(r'DB\orders.db')
        a = self.LS.product_lst()
        for i in a:
            self.goods_list.addItem('№' + str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[3]) + ' ' + 'шт.')

    def appending(self):
        goodsLWindowApplication()
        self.close()


class GoodsListWindow(QMainWindow):
    sha, shd = False, False
    def __init__(self):
        super().__init__()
        uic.loadUi('goodslist.ui', self)
        self.back_button.clicked.connect(self.back)
        self.appending_button.clicked.connect(self.showappend)
        self.deleting_button.clicked.connect(self.showdelete)
        self.append_button.clicked.connect(self.appending)

        self.label.hide()
        self.label_2.hide()
        self.label_3.hide()
        self.name_line.hide()
        self.count_line.hide()
        self.price_line.hide()
        self.append_button.hide()

        self.label_4.hide()
        self.id_line.hide()
        self.delete_button.hide()

    def back(self):
        goodsWin.show()
        self.close()
    def showappend(self):
        if not self.sha:
            self.label.show()
            self.label_2.show()
            self.label_3.show()

            self.name_line.show()
            self.count_line.show()
            self.price_line.show()
            self.append_button.show()

            self.sha = True
        else:
            self.label.hide()
            self.label_2.hide()
            self.label_3.hide()

            self.name_line.hide()
            self.count_line.hide()
            self.price_line.hide()
            self.append_button.hide()

            self.sha = False
    def showdelete(self):
        if not self.shd:
            self.label_4.show()

            self.label_4.show()
            self.id_line.show()
            self.delete_button.show()

            self.shd = True
        else:
            self.label_4.hide()

            self.label_4.hide()
            self.id_line.hide()
            self.delete_button.hide()

            self.shd = False
    def appending(self):
        self.LS = Orders(r'DB\orders.db')
        self.LS.add_admin_product(80, 'СтулСтул', 12, 12)
def application():
    app = QApplication(sys.argv)
    global enterWin
    global mainWin
    global orderWin
    global orderListWin
    global goodsWin
    global regWin
    global goodsListWin

    enterWIn = EnterWindow()
    enterWIn.show()

    mainWin = MainWindow()

    regWin = RegWindow()

    orderWin = OrderWindow()

    orderListWin = OrderListWindow()

    goodsWin = GoodsWindow()

    goodsListWin = GoodsListWindow()
    sys.exit(app.exec_())


def mainWindowApplication():
    mainWin.show()


def regWindowApplication():
    regWin.show()


def orderWindowApplication():
    orderWin.show()


def orderListWindowApplication():
    orderListWin.show()


def goodsWindowApplication():
    goodsWin.show()

def goodsLWindowApplication():
    goodsListWin.show()

if __name__ == '__main__':
    application()
