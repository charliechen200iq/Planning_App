from tkinter import *
import subprocess



root = Tk()
root.title("Planning App")



#go the calendar page
def calendar():
    root.destroy()
    subprocess.run(["python", "calendar_page.py"])

#go to the notes page
def notes():
    root.destroy()
    subprocess.run(["python", "notes.py"])

#go to the alarm page
def alarm():
    root.destroy()
    subprocess.run(["python", "alarm.py"])



#display calendar, notes, alarm buttons
Label(root, text="calendar").grid(row=0, column=0, padx=50)
calendar_button = Button(root, text="calendar", command=calendar)
calendar_button.grid(row=1, column=0, padx=50)

Label(root, text="notes").grid(row=0, column=1, padx=50)
notes_button = Button(root, text="notes", command=notes)
notes_button.grid(row=1, column=1, padx=50)

Label(root, text="alarm").grid(row=0, column=2, padx=50)
alarm_button = Button(root, text="alarm", command=alarm)
alarm_button.grid(row=1, column=2, padx=50)



root.mainloop()
