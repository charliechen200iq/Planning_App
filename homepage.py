from tkinter import *
import subprocess



root = Tk()
root.title("Planning App")
root.geometry("700x300")


#go the calendar page
def calendar():
    root.destroy()
    subprocess.run(["python", "calendar_page.py"])

#go to the notes page
def notes():
    root.destroy()
    subprocess.run(["python", "notes.py"])

#go to the timer page
def timer():
    root.destroy()
    subprocess.run(["python", "timer.py"])



#centre the homepage frame
homepage_frame = Frame(root)
homepage_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

#display calendar image buttons
calendar_picture = PhotoImage(file='pictures/calendar@0.12x.png')
Label(homepage_frame, text="Calendar").grid(row=0, column=0, padx=50)
calendar_button = Button(homepage_frame, image=calendar_picture, borderwidth=0, command=calendar)
calendar_button.grid(row=1, column=0, padx=50, pady=20)

#display notes labels and image buttons
notes_picture = PhotoImage(file='pictures/todolist@0.12x.png')
Label(homepage_frame, text="Notes").grid(row=0, column=1, padx=50)
notes_button = Button(homepage_frame, image=notes_picture, borderwidth=0, command=notes)
notes_button.grid(row=1, column=1, padx=50, pady=20)

#display timer labels and image buttons
timer_picture = PhotoImage(file='pictures/timer@0.12x.png')
Label(homepage_frame, text="Timer").grid(row=0, column=2, padx=50)
timer_button = Button(homepage_frame, image=timer_picture, borderwidth=0, command=timer)
timer_button.grid(row=1, column=2, padx=50, pady=20)



root.mainloop()
