from tkinter import *
import subprocess

root = Tk()
root.title("alarm")
root.geometry("500x500")

alarm_label = Label(root, text="alarm")
alarm_label.grid(row=0, column=0)



#menu
#menus bar
main_menu = Menu(root)
root.config(menu=main_menu)

#functions
def homepage():
    root.destroy()
    subprocess.run(["python", "homepage.py"])

def calendar():
    root.destroy()
    subprocess.run(["python", "calendar_page.py"])

def notes():
    root.destroy()
    subprocess.run(["python", "notes.py"])

#Create a menu items
navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Calendar page", command=calendar)
navigate_menu.add_command(label="Notes page", command=notes)


root.mainloop()