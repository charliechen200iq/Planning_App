from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.title("alarm")

alarm_label = ttk.Label(root, text="alarm")
alarm_label.grid(row=0, column=0)

root.mainloop()