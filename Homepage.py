from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Planning App")

calender_label = ttk.Label(root, text="Calender")
calender_label.grid(row=0, column=0)

root.mainloop()