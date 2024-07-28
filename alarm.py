from tkinter import *
import subprocess

root = Tk()
root.title("alarm")
root.geometry("500x500")


#variables
hour = StringVar()
hour.set("00")
minute = StringVar()
minute.set("00")
second = StringVar()
second.set("00")



#display the timer
timer_frame = Frame(root, pady=50)
timer_frame.pack()

Label(timer_frame, text="hour").grid(row=0, column=0)
hour_entry = Entry(timer_frame, textvariable=hour)
hour_entry.grid(row=1, column=0)

Label(timer_frame, text="minute").grid(row=0, column=1)
minute_entry = Entry(timer_frame, textvariable=minute)
minute_entry.grid(row=1, column=1)

Label(timer_frame, text="second").grid(row=0, column=2)
second_entry = Entry(timer_frame, textvariable=second)
second_entry.grid(row=1, column=2)



#timer function
def countdown():
    pass

def stop():
    pass

def reset():
    pass



#button
button_frame = Frame(root)
button_frame.pack()

Button(button_frame, text="start", command=countdown).grid(row=0, column=0, padx=10)
Button(button_frame, text="stop", command=stop).grid(row=0, column=1, padx=10)
Button(button_frame, text="reset", command=reset).grid(row=0, column=2, padx=10)





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