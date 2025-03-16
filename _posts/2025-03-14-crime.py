import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from config import API_KEY

crime_url = "https://data.cityofchicago.org/resource/ijzp-q8t2.csv"
crime_df = pd.read_csv(crime_url)


crime_df = crime_df[['primary_type', 'date', 'latitude', 'longitude']]
crime_df['date'] = pd.to_datetime(crime_df['date'])

city = "Chicago,US"  

weather_data_list = []

for index, row in crime_df.iterrows():
    crime_datetime = row['date']
    
    #API Call for current weather
    weather_url = (
        f"http://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={API_KEY}&units=metric"
    )

    response = requests.get(weather_url)

    if response.status_code == 200:
        weather_data = response.json()
        
        # Extract weather details
        temp = weather_data['main']['temp']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        weather_data_list.append({
            "temperature": temp,
            "humidity": humidity,
            "wind_speed": wind_speed
        })
    else:
        print(f"Failed to fetch weather data at index {index}: {response.status_code} - {response.text}")
        weather_data_list.append({"temperature": None, "humidity": None, "wind_speed": None})

# Merge weather data into crime DataFrame
weather_df = pd.DataFrame(weather_data_list)
crime_df = pd.concat([crime_df.reset_index(drop=True), weather_df], axis=1)

# Save to CSV
crime_df.to_csv("crime_weather_data.csv", index=False)
print("Data fetching and merging complete! Data saved to 'crime_weather_data.csv'.")