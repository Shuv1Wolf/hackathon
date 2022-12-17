import sqlite3
import re

class Orders:

    def __init__(self, db_file):
        """Установка соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_admin_product(self, item_name, price, count):
        """добавление товара и цены в БД с продаваемым продуктом (только для админов)"""
        request = f"""INSERT INTO product VALUES('{item_name}', {price}, {count})"""
        self.cursor.execute(request)
        return self.connection.commit()

    def get_item_from_thePoduct(self, id):
        '''получение продукта для создания заказа'''
        sqlite_select_query = f"""SELECT * from product"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        return result[id-1]

    def get_list(self):
        '''функция со списком товара для создания выподающего выбора товара'''
        sqlite_select_query = f"""SELECT item from product"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        string = re.sub(r'[^а-яА-Яa-zA-z" ,]', r'', str(result))
        return string[1:len(string)-2].split(',,')

    def add_order(self, name, mail, title, quantity, price):
        """создание заказа в БД"""
        request = f"""INSERT INTO order1(name, mail, title, quantity, price)
        VALUES('{name}', '{mail}', '{title}', {quantity}, {price})"""
        self.cursor.execute(request)
        return self.connection.commit()

    def product_lst(self):
        sqlite_select_query = """SELECT * from product"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        return result

    def delete(self, table, id):
        sql_delete_query = f"""DELETE from {table} where id = {id}"""
        self.cursor.execute(sql_delete_query)
        self.connection.commit()





