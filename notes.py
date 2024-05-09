from tkinter import *
from tkinter import ttk
import subprocess

root = Tk()
root.title("notes")

notes_label = ttk.Label(root, text="notes")
notes_label.grid(row=0, column=0)

root.mainloop()