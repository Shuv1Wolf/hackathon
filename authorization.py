import sqlite3
import hashlib

class Authorization:

    def __init__(self, db_file):
        """Установка соединения с БД"""
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def check(self, table, login, password):
        """
        Проверка, есть ли пароль и логин в базе данных
        table -> сама таблица в БД
        login -> логин для авторизации, который вводит пользователь
        password -> пароль для авторизации, который вводит пользователь
        """
        sqlite_select_query = f"""SELECT * from {table}"""
        self.cursor.execute(sqlite_select_query)
        result = self.cursor.fetchall()
        flag = False
        hach_log = hashlib.sha384(login.encode())
        hach_pas = hashlib.sha384(password.encode())
        for i in range(len(result)):
            users = result[i]
            if users[0] == hach_log.hexdigest() and users[1] == hach_pas.hexdigest():
                flag = True
        return flag

    def registration(self, table, user_log, password):
        """Регистрация новых данныз для авторизации в БД
        table -> сама редактируемая таблица в БД
        user_log -> логин пользователя, который мы регистрируем
        password -> пароль пользователя, который мы регистрируем"""
        hash_log = hashlib.sha384(user_log.encode())
        hash_pas = hashlib.sha384(password.encode())
        request = f"""INSERT INTO {table} VALUES('{hash_log.hexdigest()}', '{hash_pas.hexdigest()}')"""
        self.cursor.execute(request)
        return self.connection.commit()





