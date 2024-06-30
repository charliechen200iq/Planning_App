import sqlite3

connection = sqlite3.connect("app_data_base.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS user_detail(username, password)")

cursor.execute("CREATE TABLE IF NOT EXISTS current_user(username, password)")

connection.commit()
cursor.close()
connection.close()
