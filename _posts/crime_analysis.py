import pandas as pd

#load the merged crime and weather data
crime_df = pd.read_csv("crime_weather_data.csv")

#check the data structure
print(crime_df.head())
#print(crime_df['primary_type'].unique())

#filter for violent crimes 
violent_crimes = ['ASSAULT', 'BATTERY', 'CRIMINAL SEXUAL ASSAULT', 'HOMICIDE', 
'KIDNAPPING', 'SEX OFFENSE', 'ROBBERY', 'WEAPONS VIOLATION', 
'ARSON', 'INTIMIDATION']

violent_crime_data = crime_df[crime_df['primary_type'].isin(violent_crimes)]

#drop rows with missing values in key columns
crime_weather_df = crime_df.dropna(subset=['temperature'])

import seaborn as sns
import matplotlib.pyplot as plt


sns.set(style="whitegrid")

#create regression plot
plt.figure(figsize=(10, 6))
sns.regplot(x='temperature', y='primary_type', data=crime_weather_df, 
            scatter_kws={'alpha':0.5}, line_kws={'color': 'red'})

plt.title("Relationship Between Temperature and Violent Crime Rates")
plt.xlabel("Temperature (°C)")
plt.ylabel("Number of Violent Crimes")
plt.tight_layout()
plt.savefig("crime_plot.png")  #save the figure
plt.show()
