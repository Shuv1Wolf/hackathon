import pandas as pd
import sqlite3

class Convert:

    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def convert(self, place):
        """функция для конвертирования БД в таблицу excel
        place -> место, куда будет конвертирован файл"""
        df1 = pd.read_sql('select * from product', self.connection)
        df1.to_excel(place + r'\file.xlsx', index=False)
        df2 = pd.read_excel(place + r'\file.xlsx')
        df2.to_csv(place + r'\file.csv', index=False)




