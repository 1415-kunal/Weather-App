# # Import requests library (server se data lene ke liye)
# import requests

# # Weather fetch karne ka function
# def get_weather(city):
#     # API key (OpenWeatherMap se milegi)
#     api_key = "1564f4a5cbe16902df02835c376ea4df"  # <- yaha apna API key daalna

#     # URL jaha request bhejni hai (city + API key ke sath)
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#     # Server ko request bhejna
#     response = requests.get(url)

#     # Response ko JSON (dictionary jaisa format) me convert karna
#     data = response.json()

#     # Agar request successful hui (cod == 200 ka matlab success)
#     if data["cod"] == 200:
#         # JSON se useful data nikalna
#         temp = data["main"]["temp"]              # Temperature
#         weather = data["weather"][0]["description"]  # Weather condition
#         humidity = data["main"]["humidity"]      # Humidity %
#         wind = data["wind"]["speed"]             # Wind speed

#         # Result print karna
#         print(f"\nWeather in {city}:")
#         print(f"🌡 Temperature: {temp}°C")
#         print(f"☁ Condition: {weather}")
#         print(f"💧 Humidity: {humidity}%")
#         print(f"🌬 Wind Speed: {wind} m/s")
#     else:
#         # Agar galat city name dala ya API fail ho gayi
#         print("City not found!")

# # ------------ Main Program ------------

# # User se city input lena
# city = input("Enter city name: ")

# # Function call karke weather dikhana
# get_weather(city)







# import requests

# def get_weather(city):
#     # Tera API key
#     api_key = "1564f4a5cbe16902df02835c376ea4df"
    
#     # API URL
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#     # Request bhejna
#     response = requests.get(url)
#     data = response.json()

#     # Debugging: dekh server kya bhej raha hai
#     print("DEBUG RESPONSE:", data)

#     # Agar city sahi mili
#     if data["cod"] == 200:
#         temp = data["main"]["temp"]
#         weather = data["weather"][0]["description"]
#         humidity = data["main"]["humidity"]
#         wind = data["wind"]["speed"]

#         print(f"\nWeather in {city}:")
#         print(f"🌡 Temperature: {temp}°C")
#         print(f"☁ Condition: {weather}")
#         print(f"💧 Humidity: {humidity}%")
#         print(f"🌬 Wind Speed: {wind} m/s")
#     else:
#         print("City not found!")

# # ------------ Main Program ------------
# city = input("Enter city name: ")
# get_weather(city)







# # Import requests library (server se data lene ke liye)
# import requests

# # Function jo weather + air quality dono fetch karega
# def get_weather_and_air(city):
#     # Apna API key (OpenWeatherMap se liya hua)
#     api_key = "1564f4a5cbe16902df02835c376ea4df"
    
#     # ---------- STEP 1: WEATHER DATA ----------
#     # Weather ke liye URL (city name + API key)
#     url_weather = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
#     # API call (server ko request bhejna)
#     response_weather = requests.get(url_weather)
    
#     # Response ko JSON (Python dictionary) me convert karna
#     data_weather = response_weather.json()

#     # Agar city sahi hai (status code == 200)
#     if data_weather["cod"] == 200:
#         # Weather data nikalna JSON se
#         temp = data_weather["main"]["temp"]                 # Temperature
#         weather = data_weather["weather"][0]["description"] # Condition (cloudy, sunny)
#         humidity = data_weather["main"]["humidity"]         # Humidity %
#         wind = data_weather["wind"]["speed"]                # Wind speed

#         # City ka latitude & longitude nikalna (AQI ke liye zaruri hai)
#         lat = data_weather["coord"]["lat"]
#         lon = data_weather["coord"]["lon"]

#         # ---------- STEP 2: AIR QUALITY DATA ----------
#         # Air Pollution API (lat + lon + API key)
#         url_aqi = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"
        
#         # AQI API call
#         response_aqi = requests.get(url_aqi)
        
#         # AQI ka JSON response
#         data_aqi = response_aqi.json()

#         # AQI value nikalna (1–5)
#         aqi_value = data_aqi["list"][0]["main"]["aqi"]

#         # AQI ko human-readable banane ke liye mapping
#         aqi_status = {
#             1: "Good 🙂",
#             2: "Fair 😐",
#             3: "Moderate 😷",
#             4: "Poor 🤢",
#             5: "Very Poor ☠️"
#         }[aqi_value]

#         # ---------- FINAL OUTPUT ----------
#         print(f"\nWeather in {city}:")
#         print(f"🌡 Temperature: {temp}°C")
#         print(f"☁ Condition: {weather}")
#         print(f"💧 Humidity: {humidity}%")
#         print(f"🌬 Wind Speed: {wind} m/s")
#         print(f"🌍 Air Quality Index: {aqi_value} ({aqi_status})")
    
#     else:
#         # Agar galat city name dala ya API fail ho gayi
#         print("City not found!")

# # ------------ MAIN PROGRAM START ------------
# # User se city ka naam input lena
# city = input("Enter city name: ")

# # Function call karke data fetch aur print karna
# get_weather_and_air(city)







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

