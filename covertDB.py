import pandas as pd
import sqlite3
import getpass

class Convert:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def convert1(self):
        """функция для конвертирования БД в таблицу excel"""
        name = getpass.getuser()
        df1 = pd.read_sql('select * from product', self.connection)
        df1.to_excel(rf'C:\Users\{name}\Downloads' + r'\file.xlsx', index=False)
        df2 = pd.read_excel(rf'C:\Users\{name}\Downloads' + r'\file.xlsx')
        df2.to_csv(rf'C:\Users\{name}\Downloads' + r'\file.csv', index=False)





