import sqlite3

connection = sqlite3.connect("app_data_base.db")
cursor = connection.cursor()

command1 = """ CREATE TABLE IF NOT EXISTS 
user_detail(username, password)"""
cursor.execute(command1)

command2 = """ CREATE TABLE IF NOT EXISTS 
notes(items)"""
cursor.execute(command2)

cursor.close()
connection.close()
