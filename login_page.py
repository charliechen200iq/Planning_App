from tkinter import *
from tkinter import messagebox
import sqlite3
import subprocess



root = Tk()
root.title("Login")
root.geometry("300x150")



#check if the username and password is correct as registered to login
def login_check():
    username = e1.get()
    password = e2.get()

    #connection established for app_data_base.db
    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()
    
    #check if the input username and password is the same as registered 
    if username == "" or password == "":
        messagebox.showerror("error", "input can't be empty")
    else:
        for item in cursor.execute("SELECT * FROM user_detail"):
            if item[0] == username and item[1] == password:
                messagebox.showinfo("login", "Login Success")
                cursor.execute("DELETE FROM current_user")
                cursor.execute(f"INSERT INTO current_user VALUES ('{username}','{password}')")
                root.destroy()
                subprocess.run(["python", "homepage.py"])
                break
        else:
            messagebox.showerror("error", "incorrect username or password")
    
    #connection closed for app_data_base.db
    connection.commit()
    cursor.close()
    connection.close()

#go to a registration page
def create_account():
    root.destroy()
    subprocess.run(["python", "registration.py"])



#centre the login frame
login_frame = Frame(root)
login_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#entry labels
Label(login_frame, text="UserName").grid(row=0, column=0)
e1 = Entry(login_frame)
e1.grid(row=0, column=1)

Label(login_frame, text="Password").grid(row=1, column=0)
e2 = Entry(login_frame)
e2.grid(row=1, column=1)
e2.config(show="*")

#buttons
Button(login_frame, text="Login", command=login_check).grid(row=3, column=0, columnspan=2, pady=5)
Button(login_frame, text="Register for a new account", command=create_account).grid(row=4, column=0, columnspan=2, pady=5)



root.mainloop()
