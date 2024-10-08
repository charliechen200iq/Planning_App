from tkinter import *
from tkinter import messagebox
import sqlite3
import re
import subprocess



root = Tk()
root.title("Registration")
root.geometry("300x150")



#check if the username and password meet the requirements and then register the user
def create_account():
    username = e1.get()
    password = e2.get()
    confirm_password = e3.get()

    #connection established for app_data_base.db
    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    #make sure there are inputs
    if username == "" or password == "" or confirm_password == "":
        messagebox.showerror("error", "Input can't be empty.")
        return 
    
    #check that the username meet the requirements
    for item in cursor.execute("SELECT * FROM user_detail"):
        if item[0] == username:
            messagebox.showerror("error", "Username already exist. Pick another one.")
            return
    
    if username[0].isnumeric() == True:
        messagebox.showerror("error", "Username can't start with numbers 0-9.")
        return

    #check that the password meet the requirements
    if len(password) < 8 or len(password) > 20:
        messagebox.showerror("error", "Password must be between 8 and 20 characters.")
        return 
    
    if not re.search(r'[A-Z]', password) or not re.search(r'\d', password):
        messagebox.showerror("error", "Password must contain at least one\n uppercase letter and one number.")
        return 
    
    if password != confirm_password:
        messagebox.showerror("error", "Passwords don't match.")
        return
    
    try:    
        #create relevent tables to store their data and register the user
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {username}_notes_data(indexes, tasks, cross_or_uncross)")
        cursor.execute(f"INSERT INTO user_detail VALUES ('{username}','{password}')")
        
        #changes saved and connection closed for app_data_bade.db
        connection.commit()
        cursor.close()
        connection.close()
    
        messagebox.showinfo("registration complete", "Successfully registered. You can now login to the app.")
        root.destroy()
        subprocess.run(["python", "login_page.py"])
    except:
        #display messages when username or password can't be saved due to special characters affecting the code
        messagebox.showerror("error", "Username and Password containing special characters can't be saved properly, please delete them.")
        
        #changes discarded and connection closed for app_data_bade.db
        connection.rollback()
        cursor.close()
        connection.close()

#take the user back to login page in case they want to
def login_page():
    root.destroy()
    subprocess.run(["python", "login_page.py"])



#centre the registration frame
registration_frame = Frame(root)
registration_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#entry labels
Label(registration_frame, text="Choose a UserName").grid(row=0, column=0)
e1 = Entry(registration_frame)
e1.grid(row=0, column=1)

Label(registration_frame, text="Choose a Password").grid(row=1, column=0)
e2 = Entry(registration_frame)
e2.grid(row=1, column=1)
e2.config(show="*")

Label(registration_frame, text="Confirm Password").grid(row=2, column=0)
e3 = Entry(registration_frame)
e3.grid(row=2, column=1)
e3.config(show="*")

#buttons
Button(registration_frame, text="Register", command=create_account).grid(row=3, column=0, columnspan=2, pady=5)
Button(registration_frame, text="Back to Login", command=login_page).grid(row=4, column=0, columnspan=2, pady=5)



root.mainloop()
