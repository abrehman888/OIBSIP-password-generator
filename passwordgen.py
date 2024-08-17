
import tkinter as tk
from tkinter import messagebox
import random
import string

# Create   Function to generate password

def generate_password():
    length = int(length_var.get())
    
    if length < 4:
        messagebox.showerror("Error", "Password  length should be at least 8 characters.")
        return
    
    char_set = ""
    if letters_var.get():
        char_set += string.ascii_letters  
    if numbers_var.get():
        char_set += string.digits
    if symbols_var.get():
        char_set += string.punctuation
    
    if exclude_var.get():
        char_set = ''.join([c for c in char_set if c not in exclude_var.get()])
    
    if not char_set:
        messagebox.showerror("Error", "No character types selected.")
        return
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Function to validate length input
def validate_length(input):
    if input.isdigit() or input == "":
        return True
    else:
        return False


app = tk.Tk()
app.title("Advanced Password Generator")
app.geometry("400x300")

# Password length Label
length_label = tk.Label(app, text="Password Length:")
length_label.pack()
length_var = tk.StringVar(value="12")
length_entry = tk.Entry(app, textvariable=length_var, validate="key")
length_entry['validatecommand'] = (length_entry.register(validate_length), '%P')
length_entry.pack()

# Character types
letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

letters_check = tk.Checkbutton(app, text="Include Letters", variable=letters_var)
letters_check.pack()

numbers_check = tk.Checkbutton(app, text="Include Numbers", variable=numbers_var)
numbers_check.pack()

symbols_check = tk.Checkbutton(app, text="Include Symbols", variable=symbols_var)
symbols_check.pack()

# Exclude specific characters during create password
exclude_label = tk.Label(app, text="Exclude Characters:")
exclude_label.pack()
exclude_var = tk.StringVar()
exclude_entry = tk.Entry(app, textvariable=exclude_var)
exclude_entry.pack()

# Generated password display
password_entry = tk.Entry(app, font=("Arial", 14), justify="center")
password_entry.pack(pady=10)

# Create   Buttons for generate password
generate_button = tk.Button(app, text="Generate Password", command=generate_password)
generate_button.pack(pady=5)

# Run the application
app.mainloop()

