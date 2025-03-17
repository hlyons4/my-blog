import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
crime_weather_df = pd.read_csv("crime_weather_data.csv")
crime_weather_df['date'] = pd.to_datetime(crime_weather_df['date'])

# Plot Daily Crime Counts Over Time
daily_crime_counts = crime_weather_df.groupby(crime_weather_df['date'].dt.date).size().reset_index(name='crime_count')
plt.figure(figsize=(12, 8))
sns.lineplot(x='date', y='crime_count', data=daily_crime_counts, marker='o')
plt.title("Daily Crime Counts Over Time in Chicago")
plt.xlabel("Date")
plt.ylabel("Number of Crimes")
plt.xticks(rotation=45)
plt.tight_layout()
plt.figtext(0.5, -0.1, 
    "Crime rates were higher on March 6th around midnight (03-06 00), likely due to colder temperatures. "
    "As temperatures dropped further, crime peaked around March 7th at midnight (03-07 00). "
    "Crime rates decreased as temperatures warmed up.",
    wrap=True, horizontalalignment='center', fontsize=10)
plt.savefig("assets/img/daily_crimes.jpg", format='jpg', bbox_inches='tight')
plt.show()

# Plot Crime Type Counts
crime_counts = crime_weather_df['primary_type'].value_counts().reset_index()
crime_counts.columns = ['crime_type', 'count']
plt.figure(figsize=(12, 8))
sns.barplot(x='count', y='crime_type', data=crime_counts, palette='viridis')
plt.title("Crime Type Counts in Chicago")
plt.xlabel("Number of Crimes")
plt.ylabel("Crime Type")
plt.tight_layout()
plt.figtext(0.5, -0.1, 
    "This bar chart displays the total number of crimes by type in Chicago for the analyzed period. The data highlights which crimes are most and least frequent, offering insight into prevalent criminal activities within the city. Crime types with higher counts may indicate areas requiring more attention from law enforcement or community safety initiatives.",
    wrap=True, horizontalalignment='center', fontsize=10)
plt.savefig("assets/img/daily_crime_trend.jpg", format='jpg', bbox_inches='tight')

plt.show()