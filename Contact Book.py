from tkinter import *
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required.")
        return
    
    contacts.append([name, phone, email, address])
    update_list()
    clear_entries()

def update_contact():
    search = name_entry.get()
    for contact in contacts:
        if contact[0] == search:
            contact[1] = phone_entry.get()
            contact[2] = email_entry.get()
            contact[3] = address_entry.get()
            update_list()
            clear_entries()
            return
    messagebox.showerror("Error", "Contact not found.")

def delete_contact():
    search = search_entry.get()
    for contact in contacts:
        if contact[0].lower() == search.lower() or contact[1] == search:
            contacts.remove(contact)
            update_list()
            search_entry.delete(0, END)
            return
    messagebox.showerror("Error", "Matching contact not found for deletion.")

def search_contact():
    search = search_entry.get()
    contact_listbox.delete(0, END)
    for contact in contacts:
        if search.lower() in contact[0].lower() or search in contact[1]:
            contact_listbox.insert(END, f"{contact[0]} | {contact[1]} | {contact[2]} | {contact[3]}")

def update_list():
    contact_listbox.delete(0, END)
    for contact in contacts:
        contact_listbox.insert(END, f"{contact[0]} | {contact[1]} | {contact[2]} | {contact[3]}")

def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

root = Tk()
root.title("Contact Book")
root.geometry("750x450")
root.configure(bg="#e8f0ff")

Label(root, text=" Contact Book", font=("Arial", 22, "bold"), bg="#e8f0ff").pack()

frame = Frame(root, bg="#e8f0ff")
frame.pack(pady=10)

Label(frame, text="Name:", bg="#e8f0ff").grid(row=0, column=0, sticky="w")
name_entry = Entry(frame, width=30)
name_entry.grid(row=0, column=1, padx=10)

Label(frame, text="Phone:", bg="#e8f0ff").grid(row=1, column=0, sticky="w")
phone_entry = Entry(frame, width=30)
phone_entry.grid(row=1, column=1, padx=10)

Label(frame, text="Email:", bg="#e8f0ff").grid(row=2, column=0, sticky="w")
email_entry = Entry(frame, width=30)
email_entry.grid(row=2, column=1, padx=10)

Label(frame, text="Address:", bg="#e8f0ff").grid(row=3, column=0, sticky="w")
address_entry = Entry(frame, width=30)
address_entry.grid(row=3, column=1, padx=10)

#  Update Button Row (Delete is set besdie Search option...) : 

add_btn = Button(frame, text="Add Contact", command=add_contact, width=12)
add_btn.grid(row=4, column=0, pady=10)

update_btn = Button(frame, text="Update", command=update_contact, width=12)
update_btn.grid(row=4, column=1)

search_entry = Entry(frame, width=20)
search_entry.grid(row=4, column=2, padx=10)

search_btn = Button(frame, text="Search", command=search_contact, width=10)
search_btn.grid(row=4, column=3)

delete_btn = Button(frame, text="Delete", command=delete_contact, width=10)
delete_btn.grid(row=4, column=4, padx=10)

# Contact List Display :

contact_listbox = Listbox(root, width=100, height=12)
contact_listbox.pack(pady=10)

root.mainloop()
