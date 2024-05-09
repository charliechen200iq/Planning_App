from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.title("Planning App")

def calender():
    print("calender")
    root.destroy()
    subprocess.run(["python", "calender.py"])

def notes():
    root.destroy()
    subprocess.run(["python", "notes.py"])

def alarm():
    root.destroy()
    subprocess.run(["python", "alarm.py"])


calender_label = ttk.Label(root, text="calender")
calender_label.grid(row=0, column=0)
calender_button = ttk.Button(root, text="Calender", command=calender)
calender_button.grid(row=1, column=0)

notes_label = ttk.Label(root, text="notes")
notes_label.grid(row=0, column=1)
notes_button = ttk.Button(root, text="notes", command=notes)
notes_button.grid(row=1, column=1)

alarm_label = ttk.Label(root, text="alarm")
alarm_label.grid(row=0, column=2)
alarm_button = ttk.Button(root, text="alarm", command=alarm)
alarm_button.grid(row=1, column=2)

root.mainloop()