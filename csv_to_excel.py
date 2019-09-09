
import pymysql
import pandas as pd

db = pymysql.connect("localhost", "root", "password123", "bizbayadb" )

print("Database is Connected ", db)

data = pd.read_sql('SELECT * FROM bizbaytable', db)
print(data)

data.to_excel('bizbaya_all_state_data.xlsx')
