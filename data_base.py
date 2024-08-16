import sqlite3

#connection established for app_data_base.db
connection = sqlite3.connect("app_data_base.db")
cursor = connection.cursor()

#create a table containing all the users
cursor.execute("CREATE TABLE IF NOT EXISTS user_detail(username, password)")

#create a table that keep track the current user that's using the app
cursor.execute("CREATE TABLE IF NOT EXISTS current_user(username, password)")

#connection closed for app_data_base.db
connection.commit()
cursor.close()
connection.close()