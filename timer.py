from tkinter import *
from tkinter import messagebox
import subprocess
import time
import sqlite3



root = Tk()
root.title("Timer")
root.geometry("500x500")



#connection established for app_data_base.db
connection = sqlite3.connect("app_data_base.db")
cursor = connection.cursor()

#fetching the username of the current user that's using the app
username = cursor.execute("select username from current_user").fetchone()[0]

#connection closed for app_data_base.db
connection.commit()
cursor.close()
connection.close()
#a list of the all the uncrossed tasks from notes
tasks = []
#keep track of the seconds
countdown_second = StringVar()
countdown_second.set("00")
#keep track of the mintues 
countdown_minute = StringVar()
countdown_minute.set("00")
#keep track of the hours
countdown_hour = StringVar()
countdown_hour.set("00")
#check if the countdown should continue or stop
time_running = True


 
#fetch all the uncrossed tasks from the notes pages and add it on the tasks list. 
def fetch_tasks():
    #connection established for app_data_base.db
    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    #add the uncrossed tasks along with it's index from the user's notes data table to the tasks list
    for task in cursor.execute(f"select * from {username}_notes_data"):
        if task[2] == "uncross":
            #combine the task and it's index together and add it to the tasks list
            tasks.append(task[0] + ":   " + task[1])

    #connection closed for app_data_bade.db
    connection.commit()
    cursor.close()
    connection.close()

#start counting down the time that the user inputted and displaying it
def start_countdown():
    #get the total seconds needed to countdown, and display input error if unexpected input
    try:
        total_seconds = int(hour_entry.get())*3600 + int(minute_entry.get())*60  + int(second_entry.get())
    except:
        messagebox.showerror("error", "Please input postive integers.")
    else:
        #make sure it's a positive number and then start countdowning down
        if total_seconds <= 0:
            messagebox.showerror("error", "Please input postive integers.")
        else:        
            global time_running
            time_running = True
            while total_seconds > 0 and time_running:
                time.sleep(1)
                total_seconds -= 1
                
                #convert total seconds remaining into hour:minute:seconds each time and displaying it. 
                sec = total_seconds%60
                min = int(total_seconds/60) % 60
                hou = int(total_seconds/3600) 
            
                countdown_second.set(f"{sec:02}")
                countdown_minute.set(f"{min:02}")
                countdown_hour.set(f"{hou:02}")

                root.update()

            #alert the user when time is up and cross off their task if they want
            if total_seconds == 0:
                time_up()

#alert the user when time is up and cross of their task if they want
def time_up():
    #if there is tasks then alert the user and ask if they to cross it off
    if len(tasks) != 0:
        response = messagebox.askyesno("Time's up", "Time is up! Would you like to cross off this task?")
        if response == True:
            #get the task_index
            task_index = chosen_task.get().split(":   ")[0]
            
            #connection established for app_data_base.db
            connection = sqlite3.connect("app_data_base.db")
            cursor = connection.cursor()
            
            #update task to be crossed off
            cursor.execute(f"UPDATE {username}_notes_data SET cross_or_uncross = 'cross' WHERE indexes='{task_index}'")

            #connection closed for app_data_base.db
            connection.commit()
            cursor.close()
            connection.close()

            root.destroy()
            subprocess.run(["python", "timer.py"])
    #if there is no tasks simple alert the user
    else:
        messagebox.showinfo("Time's up", "Time is up!")

#pause the countdown timer
def stop_countdown():
    global time_running 
    time_running = False

#reset the countdown timer to 0. 
def reset_countdown():
    global time_running 
    time_running = False
    countdown_second.set("00")
    countdown_minute.set("00")
    countdown_hour.set("00")

#go to homepage
def homepage():
    root.destroy()
    subprocess.run(["python", "homepage.py"])

#go to calendar page 
def calendar_page():
    root.destroy()
    subprocess.run(["python", "calendar_page.py"])

#go to notes page
def notes():
    root.destroy()
    subprocess.run(["python", "notes.py"])

#stop the countdown when existing the program 
def close_program():
    global time_running 
    time_running = False
    root.destroy()



#fetch all the uncrossed tasks from the notes pages and add it to the tasks list
fetch_tasks()

#display the drop down menu containing uncrossed tasks, or display 'None' when there is no tasks. 
dropdown_menu_frame = Frame(root)
dropdown_menu_frame.pack(pady=20)

Label(dropdown_menu_frame, text="select task from notes:").grid(row=0, column=0, padx=10)
try:
    chosen_task = StringVar()
    chosen_task.set(tasks[0])
    option_menu = OptionMenu(dropdown_menu_frame, chosen_task, *tasks)
    option_menu.grid(row=0, column=1)
except:
    Label(dropdown_menu_frame, text="None").grid(row=0, column=1, padx=10)

#display the countdown timer
countdown_frame = Frame(root)
countdown_frame.pack(pady=20)

Label(countdown_frame, text="input countdown time").grid(row=0, column=1, pady=10)

Label(countdown_frame, text="second").grid(row=1, column=2)
second_entry = Entry(countdown_frame, textvariable=countdown_second)
second_entry.grid(row=2, column=2)

Label(countdown_frame, text="minute").grid(row=1, column=1)
minute_entry = Entry(countdown_frame, textvariable=countdown_minute)
minute_entry.grid(row=2, column=1)

Label(countdown_frame, text="hour").grid(row=1, column=0)
hour_entry = Entry(countdown_frame, textvariable=countdown_hour)
hour_entry.grid(row=2, column=0)

#countdown timer buttons
countdown_button_frame = Frame(root)
countdown_button_frame.pack(pady=20)
Button(countdown_button_frame, text="start", command=start_countdown).grid(row=0, column=0, padx=10)
Button(countdown_button_frame, text="stop", command=stop_countdown).grid(row=0, column=1, padx=10)
Button(countdown_button_frame, text="reset", command=reset_countdown).grid(row=0, column=2, padx=10)

#menu
main_menu = Menu(root)
root.config(menu=main_menu)

navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Calendar", command=calendar_page)
navigate_menu.add_command(label="Notes", command=notes)


#when existing run the close program funtion to stop the timer
root.protocol("WM_DELETE_WINDOW", close_program)
root.mainloop()