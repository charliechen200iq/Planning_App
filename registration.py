from tkinter import *
from tkinter import messagebox
import sqlite3
import re



root = Tk()
root.title("Registration")



#variables:
#a list of all the invalid charater that would rise error to the program
invalid = ['/', "\\", "'", ',']



#check if the username and password meet the requirements to be registered
def create_account():
    username = e1.get()
    password = e2.get()
    confirm_password = e3.get()

    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

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

    for charater in username:
        for i in invalid:
            if charater == i:
                messagebox.showerror("error", "username can't be these charaters:  " + " ".join(invalid))
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
        
    #register the user and create relevent tables to store their data. 
    cursor.execute(f"INSERT INTO user_detail VALUES ('{username}','{password}')")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {username}_notes_items(items)")
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {username}_notes_cross_off_items(item_index)")
    messagebox.showinfo("registration complete", "Successfully registered. You can now login to the app.")
    root.destroy()
    
    connection.commit()
    cursor.close()
    connection.close()



#creating and displaying entry labels for user
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
