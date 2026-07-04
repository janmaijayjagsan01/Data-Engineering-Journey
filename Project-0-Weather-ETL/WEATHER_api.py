import csv
import requests
from datetime import datetime

API_KEY = "open_weather_api_key"
CITIES = ["Lucknow", "Mumbai", "Delhi", "Bangalore", "Chennai"]

# =================== EXTRACT ===================
def extract(city):
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print(f"EXTRACTED: {city} ka data aaya!")
        return response.json()
    else:
        print(f"ERROR: {city} — {response.status_code}")
        return None

# =================== TRANSFORM ===================
def transform(raw_data, city):
    if raw_data is None:
        return None
    return {
        "city": city,
        "temp_celsius": round(raw_data["main"]["temp"], 2),
        "humidity": raw_data["main"]["humidity"],
        "weather": raw_data["weather"][0]["description"],
        "status": "Hot" if raw_data["main"]["temp"] > 30 else "Pleasant",
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

# =================== LOAD ===================
def load(all_data):
    with open("weather_data_api.csv", "w", newline="") as file:
        fieldnames = ["city", "temp_celsius", "humidity", "weather", "status", "timestamp"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_data:
            if row:
                writer.writerow(row)
    print("LOAD: weather_data.csv ban gayi!")

# =================== PIPELINE ===================
all_weather = []
for city in CITIES:
    raw = extract(city)
    processed = transform(raw, city)
    all_weather.append(processed)

load(all_weather)
print("PIPELINE COMPLETE!")
