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
        self.DB.convert1()


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
        self.agree_button.clicked.connect(self.agree)
        self.label_2.setText('')

    def back(self):
        mainWin.show()
        self.close()
    def agree(self):
        F = Orders(r'DB\orders.db')
        flag = F.item_in_product(self.good_line_2.text())
        self.LS = Orders(r'DB\orders.db')
        if flag:
            try:
                c = self.count_line.text()
                c = int(c)
                b = self.count_line_2.text()
                b = int(b)
                self.LS.add_order(self.name_line.text(), self.good_line.text(), self.good_line_2.text(), c, b)
                self.label_8.setText(b * c)
            except:
               #self.label_8.setText('Ошибка')
                pass
        else:
            self.label_8.setText('Ошибка')
            print(flag)

class OrderListWindow(QMainWindow):
    spis = []
    a = 0
    def __init__(self):
        super().__init__()
        uic.loadUi('orderList.ui', self)
        self.load_button.clicked.connect(self.reload)
        self.back_button.clicked.connect(self.back)
        self.delete_button.clicked.connect(self.delete)
        self.order_list.currentItemChanged.connect(self.values)
        self.reload()
    def back(self):
        mainWin.show()
        self.close()

    def reload(self):
        self.order_list.clear()
        self.LS = Orders(r'DB\orders.db')
        a = self.LS.product_lst('order1')
        for i in a:
            self.order_list.addItem('№' + str(i[0]) + '  ' + i[1] + ' ' + i[2])
            self.spis.append('№' + str(i[0]) + '  ' + i[1] + '  ' + i[2])
    def delete(self):
        c = self.spis[self.a].split()
        c = c[0].replace('№', '')
        print('Удалён заказ номер', c)

    def values(self):
        self.a = self.order_list.currentRow()
        print(self.spis[self.a])
        self.LS = Orders(r'DB\orders.db')
        b = self.LS.get_list_order(self.spis[self.a])
        self.name_label.setText('Имя заказчика: '+b[1])
        self.number_label.setText('Номер заказа: '+b[0])
        self.mail_label.setText('Почта заказчика: ' + b[2])
        self.good_label.setText('Наименование товара: ' + b[3])
        self.count_label.setText('Количество: ' + b[4])
        self.sum_label.setText('Сумма: ' + b[4])

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
        a = self.LS.product_lst('product')
        for i in a:
            self.goods_list.addItem('ID:' + str(i[0]) + '  ' + str(i[1]) + ' ' + str(i[3]) + ' ' + 'шт.')

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
        self.delete_button.clicked.connect(self.deleting)

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
        a = self.LS.product_lst('product')
        a = a[-1][0]
        temp = [str(self.name_line.text()), self.count_line.text(), self.price_line.text()]
        try:
            self.LS.add_admin_product(a+1, temp[0],int(temp[2]) , int(temp[1]))
            self.massage.setText('')
        except:
            self.massage.setText('Ошибка')
    def deleting(self):
        self.LS = Orders(r'DB\orders.db')
        try:
            t = int(self.id_line.text())
            self.LS.delete('product', t)
            self.massage.setText('')
        except:
            self.massage.setText('Ошибка')
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
