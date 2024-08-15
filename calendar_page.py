from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import subprocess
import sqlite3



root = Tk()
root.title("Calendar")
root.geometry("500x300")



#a list of all the invalid charater that would rise error to the program 
invalid = ["'"]



#add event to notes page
def add_event():
    #get the event
    event = calendar.get_date() + " " + event_entry.get()  

    #connection established for app_data_base.db
    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    #get the current user that's using the app
    username = cursor.execute("select username from current_user").fetchone()[0]

    #added the event to notes data
    try:
        #the index start at 0, but the count is the number of items, so when I add the new item its index becomes the count. 
        task_index = cursor.execute(f"select count(*) from {username}_notes_data").fetchone()[0]
        cursor.execute(f"insert into {username}_notes_data values('{task_index}', '{event}', 'uncross')")
        event_entry.delete(0, END)
        messagebox.showinfo("added", "Your event is successfully added to notes.")
    except:
        messagebox.showerror("error", "can't save these charaters:   " + " ".join(invalid) + "\nplease delete them to save")

    #connection closed for app_data_base.db
    connection.commit()
    cursor.close()
    connection.close()

#go to the hompage
def homepage():
    root.destroy()
    subprocess.run(["python", "homepage.py"])

#go to the notes page
def notes():
    root.destroy()
    subprocess.run(["python", "notes.py"])

#go to the timer page
def timer():
    root.destroy()
    subprocess.run(["python", "timer.py"])



#display the calendar
calendar = Calendar(root, setmode="day")
calendar.pack(pady=20)

#event entry
add_event_frame = Frame(root) 
add_event_frame.pack()

add_event_label = Label(add_event_frame, text="Input event on selected day:")
add_event_label.grid(row=0, column=0, padx=5, pady=20)

event_entry = Entry(add_event_frame)
event_entry.grid(row=0, column=1, pady=20)

#buttons
add_event_button = Button(add_event_frame, text="add event to notes", command = add_event)
add_event_button.grid(row=0, column=3, padx=30, pady=20)

#menu
main_menu = Menu(root)
root.config(menu=main_menu)

navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Notes", command=notes)
navigate_menu.add_command(label="Timer", command=timer)



root.mainloop()