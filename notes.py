from tkinter import *
from tkinter import messagebox
import subprocess
import sqlite3



root = Tk()
root.title("practice")
root.geometry("500x500")



#a list of all the invalid charater that would rise error to the program 
invalid = ['/', "'"]
#the colour of items that's being acrossed off
crossed_off_colour = "#808080"



#list frame
items_frame = Frame(root, pady=10)
items_frame.pack()

#listbox(SINGLE, MULTIPLE, EXTENDED, BROWSE)
my_listbox = Listbox(items_frame, width=50, height=20, selectmode=MULTIPLE, activestyle="none")
my_listbox.pack(side=LEFT, fill=BOTH)

#scrollbar
my_scrollbar = Scrollbar(items_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)
my_listbox.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_listbox.yview)

#user entry label
entry_frame = Frame(root, pady=10)
entry_frame.pack()
my_entry = Entry(entry_frame)
my_entry.grid(row=0, column=0)
message = "can't save these charaters:   " + " ".join(invalid)
Label(entry_frame, text=message).grid(row=0, column=1)



connection = sqlite3.connect("app_data_base.db")
cursor = connection.cursor()

#get the current user that's using the app
username =  cursor.execute("select username from current_user").fetchone()[0]

#Add the saved items from the database to the list
for item in cursor.execute(f"select * from {username}_notes_items"):
    my_listbox.insert("end", item[0])

#Add all the saved cross off items from database to the list
for item in cursor.execute(f"select * from {username}_notes_cross_off_items"):
    my_listbox.itemconfig(item[0], fg=crossed_off_colour)

connection.commit()
cursor.close()
connection.close()



#button frame
button_frame = Frame(root)
button_frame.pack(pady=10)

#add items to the list
def add_items():
    my_listbox.insert(END, my_entry.get()) 
    my_entry.delete(0, END)             

#delete item from the list
def delete_items():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)

#delete all the items from the list
def delete_all_items():
    my_listbox.delete(0, END)

#cross off an item that the user has done
def cross_off_items():
    for item in my_listbox.curselection():
        my_listbox.itemconfig(item, fg=crossed_off_colour)
    my_listbox.selection_clear(0, END)

#uncross an item
def uncross_off_items():
    for item in my_listbox.curselection():
        my_listbox.itemconfig(item, fg="")
    my_listbox.selection_clear(0, END)

#delete all the crossed off items
def delete_cross_off_items():
    for item in range(my_listbox.size()-1, -1, -1):
        if my_listbox.itemcget(item, "fg") == crossed_off_colour:
            my_listbox.delete(item)
    """ 
    #another way to do it
    count = 0
    while count < my_listbox.size():
        print(count)
        if my_listbox.itemcget(count, 'fg')==crossed_off_colour:
            my_listbox.delete(count)
        else:
            count += 1
    """



#buttons labels of the notes pages
add_button = Button(button_frame, text="add items", command=add_items)
add_button.grid(row=0, column=0, padx=5)
delete_button = Button(button_frame, text="delete items", command=delete_items)
delete_button.grid(row=0, column=1, padx=5)
delete_all_button = Button(button_frame, text="delete all items", command=delete_all_items)
delete_all_button.grid(row=0, column=2, padx=5)
cross_off_button = Button(button_frame, text="cross off items", command=cross_off_items)
cross_off_button.grid(row=1, column=0, padx=5)
uncross_off_button = Button(button_frame, text="uncross off items", command=uncross_off_items)
uncross_off_button.grid(row=1, column=1, padx=5)
delete_cross_off_button = Button(button_frame, text="delete_cross_off_button", command=delete_cross_off_items)
delete_cross_off_button.grid(row=1, column=2, padx=5)



#save all the notes to the database
def save_file():
    #checks for invalid charaters that can't be saved 
    for item in range(my_listbox.size()):
        for charater in my_listbox.get(item):
            for i in invalid:
                if charater == i:
                    messagebox.showerror("error", "can't save these charaters:   " + " ".join(invalid) + "\nplease delete them to save")
                    return
                     

    connection = sqlite3.connect("app_data_base.db")
    cursor = connection.cursor()

    #save all the items
    cursor.execute(f"DELETE FROM {username}_notes_items")
    for item in range(my_listbox.size()):
        cursor.execute(f"insert into {username}_notes_items values('{my_listbox.get(item)}')")
    
    #save all the crossed off items
    cursor.execute(f"DELETE FROM {username}_notes_cross_off_items")
    for index in range(my_listbox.size()):
        if my_listbox.itemcget(index, "fg") == crossed_off_colour:
            cursor.execute(f"insert into {username}_notes_cross_off_items values('{index}')")

    connection.commit()
    cursor.close()
    connection.close()

    #inform the user that the notes is saved
    messagebox.showinfo("Saved", "Your notes is successfully saved.")

#go to the homepage
def homepage():
    if exit_confirm() == True:
        subprocess.run(["python", "homepage.py"])

#go to the alarm page
def alarm():
    if exit_confirm() == True:
        subprocess.run(["python", "alarm.py"])

#go the calendar page
def calendar():
    if exit_confirm() == True:
        subprocess.run(["python", "calendar_page.py"])

#creating and displaying menu
main_menu = Menu(root)
root.config(menu=main_menu)

file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)

navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Alarm page", command=alarm)
navigate_menu.add_command(label="Calendar page", command=calendar)



#remind the user to save their notes when existing 
def exit_confirm():
    response = messagebox.askyesno("exit confirm", """Do you wish to exit? \nMake sure to save your notes in the file menu.""")
    
    if response == True:
         root.destroy()
         return True
root.protocol("WM_DELETE_WINDOW", exit_confirm)



root.mainloop()