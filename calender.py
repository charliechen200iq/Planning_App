from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.title("calender")

calender_label = ttk.Label(root, text="calender")
calender_label.grid(row=0, column=0)

root.mainloop()