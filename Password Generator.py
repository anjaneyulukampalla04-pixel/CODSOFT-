import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    entry_password.config(state='normal')
    entry_password.delete(0, tk.END)
    try:
        length = int(entry_length.get())
        if length <= 0:
            entry_password.insert(0, "Length must be > 0")
            entry_password.config(state='readonly')
            return
    except ValueError:
        entry_password.insert(0, "Enter a valid number")
        entry_password.config(state='readonly')
        return

    chars = ""
    if var_upper.get():
        chars += string.ascii_uppercase
    if var_lower.get():
        chars += string.ascii_lowercase
    if var_digits.get():
        chars += string.digits
    if var_special.get():
        chars += string.punctuation
    if not chars:
        entry_password.insert(0, "Select at least one set")
        entry_password.config(state='readonly')
        return

    password = "".join(random.choice(chars) for _ in range(length))
    entry_password.insert(0, password)
    entry_password.config(state='readonly')

def copy_to_clipboard():
    password = entry_password.get()
    if password and "must be" not in password and "number" not in password and "Select" not in password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied!", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("520x240")
root.resizable(False, False)

font_label = ("Arial", 12)
font_entry = ("Arial", 12)

# Row 1: Password Length
tk.Label(root, text="Password Length:", font=font_label, anchor='e', width=18).grid(row=0, column=0, padx=(28,5), pady=12, sticky='e')
entry_length = tk.Entry(root, width=8, font=font_entry)
entry_length.grid(row=0, column=1, padx=5, pady=12, sticky='w')

# Row 2 & 3: Character Options
var_upper = tk.BooleanVar(value=True)
var_lower = tk.BooleanVar(value=True)
var_digits = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=var_upper, font=font_label).grid(row=1, column=0, sticky="e", padx=(28,5), pady=3)
tk.Checkbutton(root, text="Lowercase (a-z)", variable=var_lower, font=font_label).grid(row=1, column=1, sticky="w", padx=5, pady=3)
tk.Checkbutton(root, text="Numbers (0-9)", variable=var_digits, font=font_label).grid(row=2, column=0, sticky="e", padx=(28,5), pady=3)
tk.Checkbutton(root, text="Special (!@#...)", variable=var_special, font=font_label).grid(row=2, column=1, sticky="w", padx=5, pady=3)

# Row 4: Generate Button
tk.Button(root, text="Generate Password", command=generate_password, font=font_label, width=17, bg="#44c767").grid(row=3, column=0, columnspan=2, pady=14)

# Row 5: Password Display
tk.Label(root, text="Generated Password:", font=font_label, anchor='e', width=18).grid(row=4, column=0, padx=(28,5), pady=(5,7), sticky='e')
entry_password = tk.Entry(root, width=38, font=font_entry, justify="left", bd=2, relief="sunken", state='readonly')
entry_password.grid(row=4, column=1, padx=5, pady=(5,7), sticky='w')

# Row 6: Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font=font_label, width=17).grid(row=5, column=0, columnspan=2, pady=6)

root.grid_columnconfigure(0, weight=0)
root.grid_columnconfigure(1, weight=1)

root.mainloop()