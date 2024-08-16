from tkinter import *
from tkinter import messagebox
import subprocess
import sqlite3



root = Tk()
root.title("Notes")
root.geometry("500x500")



#connection established for app_data_base.db
connection = sqlite3.connect("app_data_base.db")
cursor = connection.cursor()

#fetching the username of the current user that's using the app
username =  cursor.execute("select username from current_user").fetchone()[0]

#connection closed for app_data_base.db
connection.commit()
cursor.close()
connection.close()
#a list of all the invalid characters that would rise error to the program 
invalid = ["'"]
#the colour of tasks that's being acrossed off
crossed_off_colour = "#808080"



#fetch and add all the user's saved tasks from user's note data table to notes
def fetch_database_tasks():
    #connection established for app_data_base.db
    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    #Add the saved tasks from the database to the notes
    for task in cursor.execute(f"select tasks from {username}_notes_data"):
        my_listbox.insert("end", task[0])

    #Add all the saved cross off tasks from database to the notes
    for task in cursor.execute(f"select indexes, cross_or_uncross from {username}_notes_data"):
        if task[1] == "cross":
            my_listbox.itemconfig(task[0], fg=crossed_off_colour)

    #connection closed for app_data_base.db
    connection.commit()
    cursor.close()
    connection.close()

#add the user inputted tasks to the notes
def add_tasks():
    my_listbox.insert(END, my_entry.get()) 
    my_entry.delete(0, END)             

#delete selected tasks from the notes
def delete_tasks():
    for task in reversed(my_listbox.curselection()):
        my_listbox.delete(task)

#delete all the tasks from the notes
def delete_all_tasks():
    my_listbox.delete(0, END)

#cross off the selected task from the notes by changing its colour
def cross_off_tasks():
    for task in my_listbox.curselection():
        my_listbox.itemconfig(task, fg=crossed_off_colour)
    my_listbox.selection_clear(0, END)

#uncross the selected task from the notes by changing back to it's default colour
def uncross_off_tasks():
    for task in my_listbox.curselection():
        my_listbox.itemconfig(task, fg="")
    my_listbox.selection_clear(0, END)

#delete all the crossed off tasks from the notes
def delete_cross_off_tasks():
    for task in range(my_listbox.size()-1, -1, -1):
        if my_listbox.itemcget(task, "fg") == crossed_off_colour:
            my_listbox.delete(task)

#save all the notes to the database and exit the program
def save_and_exit():
    response = messagebox.askyesno("exit confirm", "Do you wish to save and exit?")
    
    if response == True:
        #connection established for app_data_base.db
        connection = sqlite3.connect("app_data_base.db")
        cursor = connection.cursor()

        #save all tasks to user's notes data table and exit
        try:
            cursor.execute(f"DELETE FROM {username}_notes_data")
            for i in range(my_listbox.size()):
                if my_listbox.itemcget(i, "fg") == crossed_off_colour:
                    cursor.execute(f"insert into {username}_notes_data values('{i}', '{my_listbox.get(i)}', 'cross')")
                else:
                    cursor.execute(f"insert into {username}_notes_data values('{i}', '{my_listbox.get(i)}', 'uncross')")
            messagebox.showinfo("Saved", "Your notes is successfully saved.")

            #save changes and connection closed for app_data_base.db
            connection.commit()
            cursor.close()
            connection.close()
            root.destroy()
            return True
        except:
        #display error if can't be saved
            messagebox.showerror("error", "can't save these special characters properly:   " + " ".join(invalid) + "\nplease delete them to save")
            
            #discard changes and connection closed for app_data_base.db
            connection.rollback()
            cursor.close()
            connection.close()
        
#go to the homepage
def homepage():
    if save_and_exit() == True:
        subprocess.run(["python", "homepage.py"])

#go the calendar page
def calendar():
    if save_and_exit() == True:
        subprocess.run(["python", "calendar_page.py"])

#go to the timer page
def timer():
    if save_and_exit() == True:
        subprocess.run(["python", "timer.py"])



#notes frame
notes_frame = Frame(root, pady=10)
notes_frame.pack()

#notes
my_listbox = Listbox(notes_frame, width=50, height=20, selectmode=MULTIPLE, activestyle="none")
my_listbox.pack(side=LEFT, fill=BOTH)

#scrollbar for the notes
my_scrollbar = Scrollbar(notes_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_listbox.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)

#user entry
entry_frame = Frame(root, pady=10)
entry_frame.pack()
Label(entry_frame, text="input tasks:").grid(row=0, column=0, padx=10)
my_entry = Entry(entry_frame)
my_entry.grid(row=0, column=1)

#fetch and add all the user's saved task from user's note data table to notes
fetch_database_tasks()

#buttons
button_frame = Frame(root)
button_frame.pack(pady=10)

add_button = Button(button_frame, text="add tasks", command=add_tasks)
add_button.grid(row=0, column=0, padx=5)
delete_button = Button(button_frame, text="delete tasks", command=delete_tasks)
delete_button.grid(row=0, column=1, padx=5)
delete_all_button = Button(button_frame, text="delete all tasks", command=delete_all_tasks)
delete_all_button.grid(row=0, column=2, padx=5)
cross_off_button = Button(button_frame, text="cross off tasks", command=cross_off_tasks)
cross_off_button.grid(row=1, column=0, padx=5)
uncross_off_button = Button(button_frame, text="uncross off tasks", command=uncross_off_tasks)
uncross_off_button.grid(row=1, column=1, padx=5)
delete_cross_off_button = Button(button_frame, text="delete crossed off tasks", command=delete_cross_off_tasks)
delete_cross_off_button.grid(row=1, column=2, padx=5)

#menu
main_menu = Menu(root)
root.config(menu=main_menu)

navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Calendar", command=calendar)
navigate_menu.add_command(label="Timer", command=timer)



#when exiting run the save_and_exit function to save the user's notes and exit the program
root.protocol("WM_DELETE_WINDOW", save_and_exit)
root.mainloop()