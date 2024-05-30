from tkinter import *
import subprocess

root = Tk()
root.title("practice")
root.geometry("600x600")



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

#user entry
my_entry = Entry(root)
my_entry.pack(pady=20)

#Add item to listbox
list_items = ["One", "Second", "Third", "sleep", "work out", "eat", "wake up", "eat breakfast", "walk the dog", 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17]
for item in list_items:
    my_listbox.insert("end", item)



#button frame
button_frame = Frame(root)
button_frame.pack(pady=10)

#button functions
def add_items():
    my_listbox.insert(END, my_entry.get())
    my_entry.delete(0, END)

def delete_items():
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)

def delete_all_items():
    my_listbox.delete(0, END)

def cross_off_items():
    for item in my_listbox.curselection():
        my_listbox.itemconfig(item, fg="#808080")
    my_listbox.selection_clear(0, END)

def uncross_off_items():
    for item in my_listbox.curselection():
        my_listbox.itemconfig(item, fg="")
    my_listbox.selection_clear(0, END)

def delete_cross_off_items():

    for item in range(my_listbox.size()-1, -1, -1):
        if my_listbox.itemcget(item, "fg") == "#808080":
            my_listbox.delete(item)
    """ 
    #another way to do it
    count = 0
    while count < my_listbox.size():
        print(count)
        if my_listbox.itemcget(count, 'fg')=="#808080":
            my_listbox.delete(count)
        else:
            count += 1
    """

#buttons
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



#menus bar
main_menu = Menu(root)
root.config(menu=main_menu)

#functions
def save_file():
    pass

def exit():
    root.destroy()

def homepage():
    root.destroy()
    subprocess.run(["python", "homepage.py"])

def alarm():
    root.destroy()
    subprocess.run(["python", "alarm.py"])

def calender():
    root.destroy()
    subprocess.run(["python", "calender.py"])

#Create a menu items
file_menu = Menu(main_menu)
main_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Exit", command=exit)

navigate_menu = Menu(main_menu)
main_menu.add_cascade(label="Navigate", menu=navigate_menu)
navigate_menu.add_command(label="Back to Homepage", command=homepage)
navigate_menu.add_command(label="Alarm page", command=alarm)
navigate_menu.add_command(label="Calender page", command=calender)


root.mainloop()