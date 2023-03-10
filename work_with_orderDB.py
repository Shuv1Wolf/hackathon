import sqlite3
import re

class Orders:

    def __init__(self, db_file):
        """Установка соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def add_admin_product(self, id, item_name, price, count):
        """добавление товара и цены в БД с продаваемым продуктом (только для админов)"""
        request = f"""INSERT INTO product VALUES({id}, '{item_name}', {price}, {count})"""
        self.cursor.execute(request)
        return self.connection.commit()

    def get_item_from_thePoduct(self, id):
        '''получение продукта для создания заказа'''
        sqlite_select_query = f"""SELECT * from product"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        return result[id-1]

    def add_order(self, name, mail, title, quantity, price):
        """создание заказа в БД"""
        request = f"""INSERT INTO order1(name, mail, title, quantity, price)
        VALUES('{name}', '{mail}', '{title}', {quantity}, {price})"""
        self.cursor.execute(request)
        return self.connection.commit()

    def product_lst(self, table):
        sqlite_select_query = f"""SELECT * from {table}"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        return result

    def delete(self, table, id):
        sql_delete_query = f"""DELETE from {table} where id = {id}"""
        self.cursor.execute(sql_delete_query)
        self.connection.commit()

    def delete1(self, table, id):
        sql_delete_query = f"""DELETE from {table} where id_order = {id}"""
        self.cursor.execute(sql_delete_query)
        self.connection.commit()

    def item_in_product(self, item):
        flag = False
        lst1 = []
        sqlite_select_query = f"""SELECT item from product"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        text = re.sub(r'[^а-яА-Яa-zA-z" ,]', r'', str(result))
        lst = text[1:len(text)-2].split(',,')
        for i in range(len(lst)):
            text = lst[i].strip()
            lst1.append(text)
        if item in lst1:
            flag = True
        return flag

    def get_list_order(self, string):
        lst = string.split('  ')
        num = re.sub(r'[^0-9]', r'', lst[0])
        sqlite_select_query = f"""SELECT * from order1 where id_order = {num}"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        info = re.sub(r'[^а-яА-Яa-zA-z0-9" ,.@]', r'', str(result)).replace('[', '').replace(']', '')
        return info.split(', ')

    def price_for_one(self, item):
        sqlite_select_query = f"""SELECT * from product"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        for i in range(len(result)):
            if item in result[i]:
                num = result[i]
                return num[2]
