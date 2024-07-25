from tkinter import *
from tkinter import messagebox
import sqlite3
import re


root = Tk()
root.title("registration")

def create_account():
    username = e1.get()
    password = e2.get()
    confirm_password = e3.get()

    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    if username == "" or password == "" or confirm_password == "":
        messagebox.showwarning("error", "Input can't be empty.")
        return 
    
    for item in cursor.execute("SELECT * FROM user_detail"):
        if item[0] == username:
            messagebox.showwarning("error", "Username already exist. Pick another one.")
            return
        
    if username[0].isnumeric() == True:
        messagebox.showwarning("error", "Username can't start with numbers 0-9.")
        return


    unvalid = ['/', "\\", "'", ',']
    for charater in username:
        for i in unvalid:
            if charater == i:
                messagebox.showwarning("error", "username can't be these charaters:  " + " ".join(unvalid))
                return
    

    if len(password) < 8 or len(password) > 20:
        messagebox.showwarning("error", "Password must be between 8 and 20 characters.")
        return 
    
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        messagebox.showwarning("error", "Password must contain at least one\n uppercase letter and one number.")
        return 
    
    if password != confirm_password:
        messagebox.showwarning("error", "Passwords don't match.")
        return
        
    cursor.execute(f"INSERT INTO user_detail VALUES ('{username}','{password}')")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {username}_notes_items(items)")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {username}_notes_cross_off_items(item_index)")
    messagebox.showinfo("registration complete", "Successfully registered. You can now login to the app.")
    root.destroy()
    
    connection.commit()
    cursor.close()
    connection.close()

Label(root, text="Choose a UserName").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="Choose a Password").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
e2.config(show="*")

Label(root, text="Confirm Password").grid(row=2, column=0)
e3 = Entry(root)
e3.grid(row=2, column=1)
e3.config(show="*")

Button(root, text="Register", command=create_account).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
