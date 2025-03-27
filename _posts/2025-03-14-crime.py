import time
import requests
import pandas as pd
from datetime import datetime, timedelta
from config import API_KEY

# Load crime data from Chicago
crime_url = "https://data.cityofchicago.org/resource/ijzp-q8t2.csv"
crime_df = pd.read_csv(crime_url)

crime_df = crime_df.drop_duplicates()

# Filter relevant columns
crime_df = crime_df[['primary_type', 'date', 'latitude', 'longitude']]
crime_df['date'] = pd.to_datetime(crime_df['date'])


print(crime_df['date'].head()) 
# weather_df = pd.read_csv(r"C:\Users\hanna\Downloads\Boston.csv")
# weather_df.rename(columns={'datetime': 'date'}, inplace=True)
# weather_df['date'] = pd.to_datetime(weather_df['date'])  # Convert to datetime


# # Fill missing latitude and longitude values with Boston's coordinates (or other valid coordinates if applicable)
# crime_df['latitude'].fillna(42.3601, inplace=True)  # Boston latitude
# crime_df['longitude'].fillna(-71.0589, inplace=True)  # Boston longitude

# # Fill missing values in numeric columns with the column mean
# weather_df['tempmax'].fillna(weather_df['tempmax'].mean(), inplace=True)
# weather_df['tempmin'].fillna(weather_df['tempmin'].mean(), inplace=True)
# weather_df['humidity'].fillna(weather_df['humidity'].mean(), inplace=True)

# # You can loop through all numeric columns if you have many
# numeric_cols = weather_df.select_dtypes(include=['number']).columns
# weather_df[numeric_cols] = weather_df[numeric_cols].fillna(weather_df[numeric_cols].mean())


# # # Or fill missing values with a default value (if applicable)
# # weather_df['preciptype'].fillna('Unknown', inplace=True)
# # weather_df['stations'].fillna('Unknown', inplace=True)
# # Ensure both 'date' columns are in datetime format
# # Convert the 'date' columns to datetime objects to ensure consistency in format
# crime_df['date'] = pd.to_datetime(crime_df['date'])
# weather_df['date'] = pd.to_datetime(weather_df['date'])

# # Check if there are any NaN values in the 'date' columns before merging
# print(crime_df['date'].isnull().sum())  # Should print 0 if no NaNs in 'date'
# print(weather_df['date'].isnull().sum())  # Should print 0 if no NaNs in 'date'

# # Ensure there are no NaNs in the 'date' column before merging
# if crime_df['date'].isnull().sum() > 0 or weather_df['date'].isnull().sum() > 0:
#     print("There are NaN values in the 'date' column. Handle them before proceeding.")
#     # Handle missing dates if necessary (e.g., by removing rows with NaNs or filling them)
#     crime_df.dropna(subset=['date'], inplace=True)
#     weather_df.dropna(subset=['date'], inplace=True)

# # Perform the merge
# merged_df = pd.merge(crime_df, weather_df, how='left', on='date')

# # Check if there are NaN values after merging
# print(merged_df.isnull().sum())

# # Optionally, you can fill NaNs in the merged dataframe if needed
# # For example, filling NaN values in numeric columns with the mean
# # merged_df.fillna(merged_df.mean(numeric_only=True), inplace=True)

# # # Check the result
# # print(merged_df.head())

# # Convert 'date' in both dataframes to only the date part (no time)
# crime_df['date'] = pd.to_datetime(crime_df['date']).dt.date
# weather_df['date'] = pd.to_datetime(weather_df['date']).dt.date
# # Check the unique dates in both dataframes
# # print("Unique dates in crime_df:", crime_df['date'].unique())
# # print("Unique dates in weather_df:", weather_df['date'].unique())
# print(weather_df['date'].unique())  # Displays all unique dates in the 'date' column


# # Perform an inner join if you only want matching dates
# merged_df = pd.merge(crime_df, weather_df, how='inner', on='date')
# # Fill missing weather data (e.g., forward fill)
# merged_df.fillna(method='ffill', inplace=True)
# # print(merged_df.head())

# # Check if there are any matching dates between the two dataframes
# matching_dates = pd.merge(crime_df[['date']], weather_df[['date']], how='inner', on='date')










# # Check the first few rows of each dataframe
# print(crime_df.head())  # Check crime data
# print(weather_df.head())  # Check weather data

# # Check for missing values in the crime data
# print(crime_df.isnull().sum())

# # Check for missing values in the weather data
# print(weather_df.isnull().sum())


# # merged_df = pd.merge(crime_df, weather_df, how='left', on='date')
# # merged_df.to_csv("merged_crime_weather_data.csv", index=False)


















# city = "Boston"
# start_date = datetime(2024, 12, 1)
# end_date = datetime(2024, 12, 14)

# # Prepare the URL for the Visual Crossing API
# weather_url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}?unitGroup=us&key={API_KEY}&contentType=json"

# # Initialize an empty list to store the weather data
# weather_data_list = []

# # Loop through the date range and fetch data for each day
# current_date = start_date
# while current_date <= end_date:
#     # Format the date to the required format (YYYY-MM-DD)
#     date_str = current_date.strftime('%Y-%m-%d')

#     # Make the request to the API for daily data
#     response = requests.get(weather_url + f"&startDate={date_str}&endDate={date_str}")

#     # Check if the response is successful
#     if response.status_code == 200:
#         weather_data = response.json()

#         # Extract necessary weather data from the response
#         if 'days' in weather_data:
#             day_data = weather_data['days'][0]
#             date = day_data['datetime']
#             temp = day_data['temp']
#             humidity = day_data['humidity']
#             wind_speed = day_data['windspeed']
#             precipitation = day_data['precip']
#             cloud_cover = day_data['cloudcover']

#             # Append the data to the list
#             weather_data_list.append({
#                 "date": date,
#                 "temperature": temp,
#                 "humidity": humidity,
#                 "windspeed": wind_speed,
#                 "precipitation": precipitation,
#                 "cloudcover": cloud_cover
#             })
#         else:
#             print(f"No data for {date_str}")
#     else:
#         print(f"Failed to fetch data for {date_str}, Status Code: {response.status_code}")
    
#     # Move to the next day
#     current_date += timedelta(days=1)

# # Create a DataFrame from the weather data
# weather_df = pd.DataFrame(weather_data_list)
# print(weather_df.columns)


# # Merge crime data with the weather data based on the 'date' column
# merged_df = pd.merge(crime_df, weather_df, how='left', left_on='date', right_on='date')

# # Save the merged data to a CSV file
# merged_df.to_csv("merged_crime_weather_data.csv", index=False)

# print("Data merging completed and saved to merged_crime_weather_data.csv")