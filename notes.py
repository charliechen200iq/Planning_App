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

#get the current user that's using the app
username =  cursor.execute("select username from current_user").fetchone()[0]

#connection closed for app_data_base.db
connection.commit()
cursor.close()
connection.close()
#a list of all the invalid charater that would rise error to the program 
invalid = ["'"]
#the colour of tasks that's being acrossed off
crossed_off_colour = "#808080"



#fetch and add all the user's saved task from user's note data table to notes
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

#delete sekected tasks from the notes
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

#save all the notes to the database
def save_file():
    #connection established for app_data_base.db
    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    #save all tasks to user's notes data table, and if error occur notify the user about invalid characters.
    try:
        cursor.execute(f"DELETE FROM {username}_notes_data")
        for i in range(my_listbox.size()):
            if my_listbox.itemcget(i, "fg") == crossed_off_colour:
                cursor.execute(f"insert into {username}_notes_data values('{i}', '{my_listbox.get(i)}', 'cross')")
            else:
                cursor.execute(f"insert into {username}_notes_data values('{i}', '{my_listbox.get(i)}', 'uncross')")
        messagebox.showinfo("Saved", "Your notes is successfully saved.")
    except:
        messagebox.showerror("error", "can't save these charaters properly:   " + " ".join(invalid) + "\nplease delete them to save")
    
    #connection closed for app_data_base.db
    connection.commit()
    cursor.close()
    connection.close()

#go to the homepage
def homepage():
    if exit_confirm() == True:
        subprocess.run(["python", "homepage.py"])

#go the calendar page
def calendar():
    if exit_confirm() == True:
        subprocess.run(["python", "calendar_page.py"])

#go to the timer page
def timer():
    if exit_confirm() == True:
        subprocess.run(["python", "timer.py"])

#remind the user to save their notes when exiting 
def exit_confirm():
    response = messagebox.askyesno("exit confirm", """Do you wish to exit? \nMake sure to save your notes in the file menu.""")
    
    if response == True:
         root.destroy()
         return True



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

#user entry label
entry_frame = Frame(root, pady=10)
entry_frame.pack()
my_entry = Entry(entry_frame)
my_entry.grid(row=0, column=0)
message = "can't save these charaters properly:   " + " ".join(invalid)
Label(entry_frame, text=message).grid(row=0, column=1)

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
delete_cross_off_button = Button(button_frame, text="delete_cross_off_button", command=delete_cross_off_tasks)
delete_cross_off_button.grid(row=1, column=2, padx=5)

#menu
main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)

navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Calendar", command=calendar)
navigate_menu.add_command(label="Timer", command=timer)



#when exiting run the exit_confirm function to remind the user to save their notes 
root.protocol("WM_DELETE_WINDOW", exit_confirm)
root.mainloop()