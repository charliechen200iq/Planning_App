import sqlite3

connection = sqlite3.connect("app_data_base.db")
cursor = connection.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS user_detail(username, password)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS notes(items)""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS cross_off(item number)""")

cursor.close()
connection.close()
