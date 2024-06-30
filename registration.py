from tkinter import *
from tkinter import messagebox
import sqlite3


def create_account():
    username = e1.get()
    password = e2.get()

    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    if username == "" or password == "":
        messagebox.showwarning("error", "Input can't be empty")
    else:
        for item in cursor.execute("SELECT * FROM user_detail"):
            if item[0] == username:
                messagebox.showwarning("error", "Username already exist. Pick another one.")
                break
        else:
            cursor.execute(f"INSERT INTO user_detail VALUES ('{username}','{password}')")
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {username}_notes_items(items)")
            cursor.execute(f"CREATE TABLE IF NOT EXISTS {username}_notes_cross_off_items(item_index)")
            messagebox.showinfo("registration complete", "Successfully registered. You can now login to the app.")
            root.destroy()
    
    connection.commit()
    cursor.close()
    connection.close()


root = Tk()
root.title("registration")

Label(root, text="Choose a UserName").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="Choose a Password").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
e2.config(show="*")

Button(root, text="Register", command=create_account).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
