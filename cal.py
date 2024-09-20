import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import pickle

# Function to calculate the BMI based on user input
def calculate_body_mass_index():
    try:
        # Fetch the weight and height values from input
        weight_value = float(weight_field.get())
        height_value = float(height_field.get())
        bmi_result = round(weight_value / (height_value ** 2), 2)
        
        # Display the calculated BMI
        bmi_output.config(text=f"{bmi_result}")

        # Determine the BMI classification
        if bmi_result < 18.5:
            classification = "Underweight"
        elif 18.5 <= bmi_result < 24.9:
            classification = "Healthy"
        elif 25 <= bmi_result < 29.9:
            classification = "Overweight"
        else:
            classification = "Obesity"
        
        # Update the category label with the classification result
        category_output.config(text=classification)

        # Store the user's BMI data
        store_bmi_record(name_input.get(), bmi_result)

    except ValueError:
        messagebox.showerror("Invalid Entry", "Please input valid numeric values for both weight and height.")

# Function to save the BMI data for each user into a file
def store_bmi_record(user_name, bmi_value):
    if user_name:
        # Check if the user already has BMI records
        if user_name in bmi_records:
            bmi_records[user_name].append(bmi_value)
        else:
            bmi_records[user_name] = [bmi_value]

        # Save the updated data into a pickle file
        with open('bmi_data_storage.pkl', 'wb') as file:
            pickle.dump(bmi_records, file)

# Function to plot and display the user's BMI history
def display_bmi_chart():
    user_name = name_input.get()
    if user_name in bmi_records:
        bmi_history = bmi_records[user_name]
        plt.plot(bmi_history, marker='o', linestyle='-', color='green', label=f"{user_name}'s BMI Trend")
        plt.title(f"BMI History for {user_name}")
        plt.xlabel("Entries")
        plt.ylabel("BMI Value")
        plt.legend()
        plt.grid(True)
        plt.show()
    else:
        messagebox.showinfo("No Data", f"No BMI records found for {user_name}.")

# Load existing BMI data from the file if available
try:
    with open('bmi_data_storage.pkl', 'rb') as file:
        bmi_records = pickle.load(file)
except FileNotFoundError:
    bmi_records = {}

# Setup the main application window
window = tk.Tk()
window.title("BMI Tracker Application")
window.geometry("400x300")

# Create input fields and labels
tk.Label(window, text="Name:").grid(row=0, column=0)
name_input = tk.Entry(window)
name_input.grid(row=0, column=1)

tk.Label(window, text="Weight (kg):").grid(row=1, column=0)
weight_field = tk.Entry(window)
weight_field.grid(row=1, column=1)

tk.Label(window, text="Height (m):").grid(row=2, column=0)
height_field = tk.Entry(window)
height_field.grid(row=2, column=1)

# Display the BMI result and category
tk.Label(window, text="Your BMI:").grid(row=3, column=0)
bmi_output = tk.Label(window, text="")
bmi_output.grid(row=3, column=1)

tk.Label(window, text="Category:").grid(row=4, column=0)
category_output = tk.Label(window, text="")
category_output.grid(row=4, column=1)

# Buttons to calculate BMI and view history
calculate_btn = tk.Button(window, text="Compute BMI", command=calculate_body_mass_index)
calculate_btn.grid(row=5, column=0, pady=10)

history_btn = tk.Button(window, text="Show BMI History", command=display_bmi_chart)
history_btn.grid(row=5, column=1)

# Run the main application loop
window.mainloop()
