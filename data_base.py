import sqlite3

connection = sqlite3.connect("app_data_base.db")
cursor = connection.cursor()

#a table containing all the users
cursor.execute("CREATE TABLE IF NOT EXISTS user_detail(username, password)")

#a table that keep track the current user that's using the app
cursor.execute("CREATE TABLE IF NOT EXISTS current_user(username, password)")

connection.commit()
cursor.close()
connection.close()


#recreate table structure (item, index, state)