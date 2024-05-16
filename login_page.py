from tkinter import *
from tkinter import messagebox
import subprocess


def check():
    username = e1.get()
    password = e2.get()

    if username == "" and password == "":
        messagebox.showinfo("", "Blank Not allowed")
    elif username == "Admin" and password == "123":
        messagebox.showinfo("", "Login Success")
        root.destroy()
        subprocess.run(["python", "homepage.py"])
    else:
        messagebox.showinfo("", "Incorrect Username and Password")


root = Tk()
root.title("Login")

Label(root, text="UserName").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="Password").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
e2.config(show="*")

Button(root, text="Login", command=check, height=3, width=13).grid(row=3, column=0, columnspan=2)

root.mainloop()
