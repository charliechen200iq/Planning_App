from tkinter import *
from tkinter import messagebox
import subprocess
import time

root = Tk()
root.title("alarm")
root.geometry("500x500")

#countdown timer
#variables
countdown_second = StringVar()
countdown_second.set("00")
countdown_minute = StringVar()
countdown_minute.set("00")
countdown_hour = StringVar()
countdown_hour.set("00")



#display the countdown timer
countdown_frame = Frame(root, pady=50)
countdown_frame.pack()

Label(countdown_frame, text="Countdown Timer").grid(row=0, column=1)

Label(countdown_frame, text="second").grid(row=1, column=2)
second_entry = Entry(countdown_frame, textvariable=countdown_second)
second_entry.grid(row=2, column=2)

Label(countdown_frame, text="minute").grid(row=1, column=1)
minute_entry = Entry(countdown_frame, textvariable=countdown_minute)
minute_entry.grid(row=2, column=1)

Label(countdown_frame, text="hour").grid(row=1, column=0)
hour_entry = Entry(countdown_frame, textvariable=countdown_hour)
hour_entry.grid(row=2, column=0)



#countdown timer function
def start_countdown():
    try:
        total_seconds = int(hour_entry.get())*3600 + int(minute_entry.get())*60  + int(second_entry.get())
        if total_seconds < 0:
            messagebox.showerror("error", "Please input postive numebers")
    except:
        messagebox.showerror("error", "Please input valid numbers.")
    else:
        global time_running
        time_running = True
        while total_seconds > 0 and time_running:
            time.sleep(1)
            total_seconds -= 1
            
            sec = total_seconds%60
            min = int(total_seconds/60) % 60
            hou = int(total_seconds/3600) 
        
            countdown_second.set(f"{sec:02}")
            countdown_minute.set(f"{min:02}")
            countdown_hour.set(f"{hou:02}")

            root.update()

        if total_seconds == 0:
            messagebox.showinfo("Info", "Time is up!")

def stop_countdown():
    global time_running 
    time_running = False

def reset_countdown():
    global time_running 
    time_running = False
    countdown_second.set("00")
    countdown_minute.set("00")
    countdown_hour.set("00")



#countdown button
countdown_button_frame = Frame(root)
countdown_button_frame.pack()

Button(countdown_button_frame, text="start", command=start_countdown).grid(row=0, column=0, padx=10)
Button(countdown_button_frame, text="stop", command=stop_countdown).grid(row=0, column=1, padx=10)
Button(countdown_button_frame, text="reset", command=reset_countdown).grid(row=0, column=2, padx=10)



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