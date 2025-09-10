

# ======WINDOW BASED======#
import requests
import tkinter as tk
from tkinter import font

# ---------- FUNCTION TO FETCH WEATHER & AIR QUALITY ----------
def get_weather_and_air():
    city = city_entry.get()
    api_key = "1564f4a5cbe16902df02835c376ea4df"
    
    # Weather API
    url_weather = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response_weather = requests.get(url_weather)
    data_weather = response_weather.json()
    
    if data_weather["cod"] == 200:
        temp = data_weather["main"]["temp"]
        weather = data_weather["weather"][0]["description"].title()
        humidity = data_weather["main"]["humidity"]
        wind = data_weather["wind"]["speed"]
        lat = data_weather["coord"]["lat"]
        lon = data_weather["coord"]["lon"]
        
        # Air Quality API
        url_aqi = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
        response_aqi = requests.get(url_aqi)
        data_aqi = response_aqi.json()
        aqi_value = data_aqi["list"][0]["main"]["aqi"]
        aqi_status = {
            1: "Good 🙂",
            2: "Fair 😐",
            3: "Moderate 😷",
            4: "Poor 🤢",
            5: "Very Poor ☠️"
        }[aqi_value]
        
        # Weather emoji mapping
        weather_icons = {
            "Clear Sky": "☀️",
            "Few Clouds": "🌤️",
            "Scattered Clouds": "☁️",
            "Broken Clouds": "☁️",
            "Shower Rain": "🌧️",
            "Rain": "🌦️",
            "Thunderstorm": "⛈️",
            "Snow": "❄️",
            "Mist": "🌫️",
            "Overcast Clouds": "☁️"
        }
        icon = weather_icons.get(weather, "🌍")
        
        # Display nicely formatted result
        result_text = (
            f"📍 City: {city.title()}\n\n"
            f"🌡 Temperature:  {temp}°C\n"
            f"☁ Condition:    {weather} {icon}\n"
            f"💧 Humidity:     {humidity}%\n"
            f"🌬 Wind Speed:  {wind} m/s\n"
            f"🌍 Air Quality: {aqi_value} ({aqi_status})"
        )
        
        result_label.config(text=result_text, fg="#212121")
    else:
        result_label.config(text="❌ City not found!", fg="red")

# ---------- GUI SETUP ----------
root = tk.Tk()
root.title("Weather & AQI App 🌤️")
root.geometry("420x450")
root.config(bg="#DFF6FF")  # Light background

# Fonts
title_font = font.Font(family="Comic Sans MS", size=18, weight="bold")
label_font = font.Font(family="Arial", size=12)
result_font = font.Font(family="Courier New", size=12, weight="bold")

# Title
title_label = tk.Label(root, text="🌤️ Weather & Air Quality Checker 🌍", font=title_font, bg="#DFF6FF", fg="#0D47A1")
title_label.pack(pady=15)

# City input
city_entry = tk.Entry(root, font=label_font, width=28, relief="solid", bd=2, justify="center")
city_entry.pack(pady=10)
city_entry.insert(0, "Enter city name")

# Fetch button
fetch_button = tk.Button(root, text="🔍 Get Weather", font=label_font, command=get_weather_and_air, bg="#0288D1", fg="white", activebackground="#01579B", relief="raised", bd=3)
fetch_button.pack(pady=12)

# Result label
result_label = tk.Label(root, text="", font=result_font, bg="#FFFFFF", justify="left", anchor="w", width=40, height=12, relief="groove", bd=2)
result_label.pack(pady=15)

root.mainloop()


