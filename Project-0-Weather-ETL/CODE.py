# EXTRACT SECTION
import csv
def extract():
    # normally yahan api ya database hota hai but hum abi raw data ko use kar rahe hai
    raw_data = [
        {"city": "paris", "temp_kelvin":294.15, "humidity": 80},
        {"city": "mumbai", "temp_kelvin":301.2, "humidity": 90},
        {"city": "lucknow", "temp_kelvin":308 ,"humidity": 70},
        {"city": "jaipur", "temp_kelvin":308.15, "humidity": 60},
        {"city": "rachi", "temp_kelvin":303.15, "humidity": 75},
        {"city": "kashmir", "temp_kelvin":288.15, "humidity": 85},
        {"city": "ladhak", "temp_kelvin":283.15, "humidity": 90},
        {"city": "sikkim", "temp_kelvin":285.15, "humidity": 88},
    ]
    print("EXTRACTED DATA:", raw_data)
    return raw_data



#transform section 

def transform(raw_data):
    cleaned =[]
    for row in raw_data:
        cleaned.append({
            "city": row["city"].title(),
            "temp_celsius": round(row["temp_kelvin"] - 273.15, 2),
            "humidity": row["humidity"],
            "status":"Hot" if row["temp_kelvin"] > 303 else "Cold"
        })
    print("TRANSFORMED DATA:", cleaned)
    return cleaned



#load section
def load(cleaned_data):
    with open("weather_data.csv","w", newline="")as file:
        writer = csv.DictWriter(file,fieldnames=["city","temp_celsius","humidity","status"])
        writer.writeheader()
        writer.writerows(cleaned_data)
    print("DATA LOADED INTO CSV FILE: wheather_data.csv")
    
   
   
   
   
   
    
    ###pipeline run
raw = extract()
process_data = transform(raw)
load(process_data)