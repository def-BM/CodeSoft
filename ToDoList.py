from tkinter import *
from tkinter import simpledialog, messagebox

# Initialization of window
root = Tk()
root.geometry("925x500+300+200")
root.title("To-Do List")
root.configure(bg='#00ffff')
root.resizable(False, False)

# Global list to store task
tasks=[]

# Function to add tasks to the list
def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, END)

#  Function to update tasks from lists
def update_task():
    selected_index = listbox.curselection()
    if selected_index:
        selected_task = listbox.get(selected_index[0])  
        updated_task = simpledialog.askstring("Update Task", f"Update the task '{selected_task[2:]}':")
        if updated_task:
            tasks[selected_index[0]] = updated_task  
            update_listbox()   


# Function to delete tasks from the list
def delete_task():
    selected_index = listbox.curselection()
    if selected_index:
        task_to_delete = listbox.get(selected_index)
        confirm_delete = messagebox.askyesno("Delete Task", f"Are you sure you want to delete the task '{task_to_delete[2:]}'?")
        if confirm_delete:
            del tasks[selected_index[0]]
            update_listbox()

# Function to update list
def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, f"\u2022 {task}")

frame = Frame(root,width=450,height=450)
frame.place(x=0,y=50)

# Header Frame
frame1 = Frame(root, width=925, height=50, bg='black')
frame1.place(x=0,y=0)

heading = Label(frame1, text="To-Do List", fg='white', bg='black', font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=400, y=5)

listbox = Listbox(frame, height=28, width=70)
listbox.pack(side=LEFT)

scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=RIGHT, fill=Y)
listbox.config(yscrollcommand=scrollbar.set)

label = Label(root, text="Enter your task", fg='black', bg='#00ffff', font=('Microsoft YaHei UI Light', 14))
label.place(x=500, y=60)

entry = Entry(root, width=50, bg='white')
entry.place(x=500, y=100)

add_button = Button(root, text="Add Task", width=40, bg='#ff00ff', activebackground='#ff00ff', command=add_task)
add_button.place(x=500, y=140)

update_button = Button(root, text="Update Task", width=40, bg='#ff00ff', activebackground='#ff00ff', command=update_task)
update_button.place(x=500, y=180)

delete_button = Button(root, text="Delete Task", width=40,bg='#ff00ff', activebackground='#ff00ff', command=delete_task)
delete_button.place(x=500, y=220)

root.mainloop()