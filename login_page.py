from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess


def login_check():
    username = e1.get()
    password = e2.get()

    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()
    
    if username == "" or password == "":
        messagebox.showwarning("error", "input can't be empty")
    else:
        for item in cursor.execute("SELECT * FROM user_detail"):
            if item[0] == username and item[1] == password:
                messagebox.showinfo("login", "Login Success")
                cursor.execute("DELETE FROM current_user")
                cursor.execute(f"INSERT INTO current_user VALUES ('{username}','{password}')")
                connection.commit()
                cursor.close()
                connection.close()
                root.destroy()
                subprocess.run(["python", "homepage.py"])
                break
        else:
            messagebox.showwarning("error", "incorrect username or password")


def create_account():
    subprocess.run(["python", "registration.py"])


root = Tk()
root.title("Login")

Label(root, text="UserName").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="Password").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
e2.config(show="*")

Button(root, text="Login", command=login_check).grid(row=3, column=0, columnspan=2)
Button(root, text="Register for a new account", command=create_account).grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
