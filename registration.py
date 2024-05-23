from tkinter import *
from tkinter import messagebox
import sqlite3


def create_account():
    username = e1.get()
    password = e2.get()
    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    cursor.execute(f"INSERT INTO user_detail VALUES ('{username}','{password}')")

    print("user added to database")
    connection.commit()
    connection.close()

    messagebox.showinfo("registration complete", "Successfully registered. You can now login to the app.")
    root.destroy()


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
