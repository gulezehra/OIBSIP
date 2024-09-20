import tkinter as tk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
import io

# Function to retrieve weather information
def get_weather():
    city_name = location_entry.get()
    if not city_name:
        messagebox.showerror("Input Error", "Please provide a location.")
        return
    
    api_key = 'd8bee240b05b69a37468739ef7c1532a'  # Replace with your OpenWeatherMap API key
    endpoint = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(endpoint)
        weather_data = response.json()
        
        if weather_data.get("cod") != 200:
            messagebox.showerror("Error", weather_data.get("message", "Unable to retrieve weather data"))
            return

        weather_info = {
            'city': weather_data['name'],
            'description': weather_data['weather'][0]['description'].capitalize(),
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
            'icon': weather_data['weather'][0]['icon']
        }

        # Update the interface with the fetched data
        display_weather_info(weather_info)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to update the interface with weather data
def display_weather_info(info):
    city_label.config(text=f"City: {info['city']}")
    description_label.config(text=f"Description: {info['description']}")
    temperature_label.config(text=f"Temperature: {info['temperature']} °C")
    humidity_label.config(text=f"Humidity: {info['humidity']}%")
    wind_speed_label.config(text=f"Wind Speed: {info['wind_speed']} m/s")
    
    # Fetch and show the weather icon
    icon_url = f"http://openweathermap.org/img/wn/{info['icon']}@2x.png"
    icon_response = requests.get(icon_url)
    icon_img = Image.open(io.BytesIO(icon_response.content))
    icon_photo = ImageTk.PhotoImage(icon_img)
    
    icon_label.config(image=icon_photo)
    icon_label.image = icon_photo

# Setting up the GUI window
app = tk.Tk()
app.title("Weather Application")
app.geometry("400x400")

# Entry for location input
tk.Label(app, text="Location:").pack(pady=5)
location_entry = tk.Entry(app)
location_entry.pack(pady=5)

# Button to fetch weather data
fetch_button = tk.Button(app, text="Fetch Weather", command=get_weather)
fetch_button.pack(pady=10)

# Labels for displaying weather details
city_label = tk.Label(app, text="")
city_label.pack(pady=5)

description_label = tk.Label(app, text="")
description_label.pack(pady=5)

temperature_label = tk.Label(app, text="")
temperature_label.pack(pady=5)

humidity_label = tk.Label(app, text="")
humidity_label.pack(pady=5)

wind_speed_label = tk.Label(app, text="")
wind_speed_label.pack(pady=5)

# Label for showing the weather icon
icon_label = tk.Label(app)
icon_label.pack(pady=10)

# Start the Tkinter event loop
app.mainloop()
