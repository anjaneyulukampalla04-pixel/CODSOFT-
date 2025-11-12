from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("To-Do List App")
root.geometry("450x550")
root.config(bg="#E8F0FE")

tasks = []

# FILE HANDLING : 
 
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for task in file:
                tasks.append(task.strip())
        update_listbox()
    except:
        pass

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

#  FUNCTIONS : 

def update_listbox():
    listbox.delete(0, END)
    for task in tasks:
        listbox.insert(END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        entry.delete(0, END)
        update_listbox()
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task = listbox.get(ACTIVE)
        tasks.remove(selected_task)
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete.")

def clear_all():
    if messagebox.askyesno("Confirm", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_listbox()
        save_tasks()

def mark_completed():
    try:
        index = listbox.curselection()[0]
        task = tasks[index]
        if "✔" not in task:
            tasks[index] = task + " ✔"
            update_listbox()
            save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to mark completed.")

def edit_task():
    try:
        index = listbox.curselection()[0]
        new_task = entry.get()
        if new_task != "":
            tasks[index] = new_task
            entry.delete(0, END)
            update_listbox()
            save_tasks()
        else:
            messagebox.showwarning("Warning", "Enter new task in the input box.")
    except:
        messagebox.showwarning("Warning", "Select a task to edit.")

def search_task():
    search = entry.get().lower()
    listbox.delete(0, END)
    for task in tasks:
        if search in task.lower():
            listbox.insert(END, task)

# UI DESIGN : 

title = Label(root, text=" To-Do List", font=("Helvetica", 20, "bold"), bg="#E8F0FE", fg="#2C3E50")
title.pack(pady=10)

frame = Frame(root, bg="#E8F0FE")
frame.pack(pady=10)

entry = Entry(frame, width=30, font=("Arial", 14))
entry.pack(side=LEFT, padx=5)

Button(frame, text="Add", width=6, command=add_task).pack(side=LEFT)

listbox = Listbox(root, width=50, height=15, font=("Arial", 12), selectbackground="#A3C4F3")
listbox.pack(pady=10)

button_frame = Frame(root, bg="#E8F0FE")
button_frame.pack(pady=10)

Button(button_frame, text="Delete", width=10, command=delete_task).grid(row=0, column=0, padx=5)
Button(button_frame, text="Edit", width=10, command=edit_task).grid(row=0, column=1, padx=5)
Button(button_frame, text="Mark Done", width=10, command=mark_completed).grid(row=0, column=2, padx=5)

Button(button_frame, text="Clear All", width=10, command=clear_all).grid(row=1, column=0, padx=5, pady=5)
Button(button_frame, text="Search", width=10, command=search_task).grid(row=1, column=1, padx=5, pady=5)
Button(button_frame, text="Show All", width=10, command=update_listbox).grid(row=1, column=2, padx=5, pady=5)

load_tasks()
root.mainloop()
