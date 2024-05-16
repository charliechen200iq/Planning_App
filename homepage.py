from tkinter import *
import subprocess

root = Tk()
root.title("Planning App")


def calender():
    root.destroy()
    subprocess.run(["python", "calender.py"])


def notes():
    root.destroy()
    subprocess.run(["python", "notes.py"])


def alarm():
    root.destroy()
    subprocess.run(["python", "alarm.py"])


# calender
Label(root, text="calender").grid(row=0, column=0, padx=50)
calender_button = Button(root, text="calender", command=calender)
calender_button.grid(row=1, column=0, padx=50)

# notes
Label(root, text="notes").grid(row=0, column=1, padx=50)
notes_button = Button(root, text="notes", command=notes)
notes_button.grid(row=1, column=1, padx=50)

Label(root, text="alarm").grid(row=0, column=2, padx=50)
alarm_button = Button(root, text="alarm", command=alarm)
alarm_button.grid(row=1, column=2, padx=50)

root.mainloop()
