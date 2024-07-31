from tkinter import *
from tkcalendar import *
import subprocess



root = Tk()
root.title("calendar")
root.geometry("500x500")



#display the calendar
calendar = Calendar(root, setmode="day")
calendar.pack(pady=20)

#get the date 
def get_date():
    date_label.config(text=calendar.get_date())

#display the get date button
get_date_button = Button(root, text="get date", command=get_date)
get_date_button.pack(pady=20)

#display the date
date_label = Label(root, text="")
date_label.pack(pady=20)



#menu section:
#go to the hompage
def homepage():
    root.destroy()
    subprocess.run(["python", "homepage.py"])

#go to the alarm page
def alarm():
    root.destroy()
    subprocess.run(["python", "alarm.py"])

#go to the notes page
def notes():
    root.destroy()
    subprocess.run(["python", "notes.py"])

#creating and displaying menu
main_menu = Menu(root)
root.config(menu=main_menu)

navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Alarm page", command=alarm)
navigate_menu.add_command(label="Notes page", command=notes)



root.mainloop()