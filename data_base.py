import sqlite3

connection = sqlite3.connect("planing_app.db")
cursor = connection.cursor()

command1 = """ CREATE TABLE IF NOT EXISTS 
user_detail(username, password)"""
cursor.execute(command1)

connection.close()
cursor.close()
