from tkinter import *
import subprocess

root = Tk()
root.title("notes")

notes_label = Label(root, text="notes")
notes_label.grid(row=0, column=0)

root.mainloop()