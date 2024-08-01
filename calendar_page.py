from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import subprocess
import sqlite3



root = Tk()
root.title("Calendar")
root.geometry("500x500")



#display the calendar
calendar = Calendar(root, setmode="day")
calendar.pack(pady=20)



#add event to notes 
def add_event():
    #get the event
    event = calendar.get_date() + " " + event_entry.get()  

    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    #get the current user that's using the app
    username =  cursor.execute("select username from current_user").fetchone()[0]

    #save event to notes data
    cursor.execute(f"insert into {username}_notes_items values('{event}')")
    event_entry.delete(0, END)
    messagebox.showinfo("Added", "Your event is successfully added to notes.")

    connection.commit()
    cursor.close()
    connection.close()



#event entry
add_event_frame = Frame(root) 
add_event_frame.pack()

add_event_label = Label(add_event_frame, text="Input event on selected day:")
add_event_label.grid(row=0, column=0, padx=5, pady=20)

event_entry = Entry(add_event_frame)
event_entry.grid(row=0, column=1, pady=20)

add_event_button = Button(add_event_frame, text="add event to notes", command = add_event)
add_event_button.grid(row=0, column=3, padx=30, pady=20)



#menu section:
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

#creating and displaying menu
main_menu = Menu(root)
root.config(menu=main_menu)

navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Notes", command=notes)
navigate_menu.add_command(label="Timer", command=timer)


root.mainloop()