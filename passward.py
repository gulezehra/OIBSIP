import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Function to create a password based on user specifications
def create_password():
    try:
        # Get the desired length and options from user input
        length = int(length_field.get())
        use_uppercase = uppercase_check.get()
        use_digits = digits_check.get()
        use_special_chars = special_check.get()

        # Define the character pool
        char_pool = string.ascii_lowercase
        if use_uppercase:
            char_pool += string.ascii_uppercase
        if use_digits:
            char_pool += string.digits
        if use_special_chars:
            char_pool += string.punctuation

        # Ensure that at least one character type is selected
        if not char_pool:
            messagebox.showerror("Selection Error", "At least one type of characters must be selected.")
            return

        # Generate the password
        generated_password = ''.join(random.choice(char_pool) for _ in range(length))
        result_label.config(text=generated_password)
        pyperclip.copy(generated_password)  # Copy the generated password to clipboard

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number for password length.")

# Create the main application window
window = tk.Tk()
window.title("Password Maker")
window.geometry("400x300")

# Entry for password length
tk.Label(window, text="Desired Length:").pack(pady=5)
length_field = tk.Entry(window)
length_field.pack(pady=5)

# Checkboxes for character types
uppercase_check = tk.BooleanVar()
digits_check = tk.BooleanVar()
special_check = tk.BooleanVar()

tk.Checkbutton(window, text="Add Uppercase Letters", variable=uppercase_check).pack(pady=5)
tk.Checkbutton(window, text="Add Numbers", variable=digits_check).pack(pady=5)
tk.Checkbutton(window, text="Add Special Characters", variable=special_check).pack(pady=5)

# Button to trigger password generation
generate_button = tk.Button(window, text="Generate", command=create_password)
generate_button.pack(pady=20)

# Label to show the generated password
tk.Label(window, text="Your Password:").pack(pady=5)
result_label = tk.Label(window, text="")
result_label.pack(pady=5)

# Start the application
window.mainloop()
