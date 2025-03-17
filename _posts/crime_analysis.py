import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
crime_weather_df = pd.read_csv("crime_weather_data.csv")

# Convert 'date' to datetime
crime_weather_df['date'] = pd.to_datetime(crime_weather_df['date'])

# Aggregate daily crime counts
daily_crime_counts = crime_weather_df.groupby(crime_weather_df['date'].dt.date).size().reset_index(name='crime_count')


plt.figure(figsize=(12, 8))
sns.lineplot(x='date', y='crime_count', data=daily_crime_counts, marker='o')
plt.title("Daily Crime Counts Over Time in Chicago")
plt.xlabel("Date")
plt.ylabel("Number of Crimes")
plt.xticks(rotation=45)
plt.tight_layout()

# Add caption
plt.figtext(0.5, -0.1, 
    "The crime rates were higher on March 6th around midnight (03-06 00), possibly due to colder temperatures. "
    "As it continued to get colder, crime peaked around March 7th at midnight (03-07 00). "
    "Crime rates then decreased as it started to warm up.", 
    wrap=True, horizontalalignment='center', fontsize=10)

plt.savefig("assets/img/daily_crimes.png", bbox_inches='tight')


plt.show()

# # Plot daily crime counts
# plt.figure(figsize=(12, 8))
# sns.lineplot(x='date', y='crime_count', data=daily_crime_counts, marker='o')
# plt.title("Daily Crime Counts Over Time in Chicago")
# plt.xlabel("Date")
# plt.ylabel("Number of Crimes")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the merged crime and weather data
crime_weather_df = pd.read_csv("crime_weather_data.csv")

# Count crimes by type
crime_counts = crime_weather_df['primary_type'].value_counts().reset_index()
crime_counts.columns = ['crime_type', 'count']

# Load the merged crime and weather data
crime_weather_df = pd.read_csv("crime_weather_data.csv")

# Count crimes by type
crime_counts = crime_weather_df['primary_type'].value_counts().reset_index()
crime_counts.columns = ['crime_type', 'count']

plt.figure(figsize=(12, 8))
sns.barplot(x='count', y='crime_type', data=crime_counts, palette='viridis')

plt.title("Crime Type Counts in Chicago")
plt.xlabel("Number of Crimes")
plt.ylabel("Crime Type")
plt.tight_layout()

plt.savefig("assets/img/daily_crime_trend.png", bbox_inches='tight')


plt.show()