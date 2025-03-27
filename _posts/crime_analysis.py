import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#merged_crime_weather_data.csv

# Load data
crime_weather_df = pd.read_csv("merged_crime_weather_data.csv")
print(crime_weather_df.head())

# heatmap_data = crime_weather_df.groupby(['hour', 'temperature']).size().unstack(fill_value=0)

# plt.figure(figsize=(12, 8))
# sns.heatmap(heatmap_data, cmap='coolwarm', annot=True, fmt='d', linewidths=0.5)
# plt.title("Heatmap of Crime Counts vs. Temperature by Hour of the Day")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Hour of the Day")
# plt.tight_layout()
# plt.savefig("assets/img/crime_temp_heatmap.jpg", format='jpg', bbox_inches='tight')
# plt.show()



# #temperature & crime correlation
# plt.figure(figsize=(12, 8))
# sns.scatterplot(x='temperature', y='primary_type', data=crime_weather_df, hue='primary_type', palette='viridis')
# plt.title("Crime Counts vs. Temperature")
# plt.xlabel("Temperature (°C)")
# plt.ylabel("Crime Type")
# plt.legend(title="Crime Type", bbox_to_anchor=(1.05, 1), loc='upper left')
# plt.tight_layout()
# plt.savefig("assets/img/crime_vs_temperature.jpg", format='jpg', bbox_inches='tight')
# plt.show()

# # Plot Crime Type Counts
# crime_counts = crime_weather_df['primary_type'].value_counts().reset_index()
# crime_counts.columns = ['crime_type', 'count']
# plt.figure(figsize=(12, 8))
# sns.barplot(x='count', y='crime_type', data=crime_counts, palette='viridis')
# plt.title("Crime Type Counts in Chicago")
# plt.xlabel("Number of Crimes")
# plt.ylabel("Crime Type")
# plt.tight_layout()
# plt.figtext(0.5, -0.1, 
#     "This bar chart displays the total number of crimes by type in Chicago for the analyzed period. The data highlights which crimes are most and least frequent, offering insight into prevalent criminal activities within the city. Crime types with higher counts may indicate areas requiring more attention from law enforcement or community safety initiatives.",
#     wrap=True, horizontalalignment='center', fontsize=10)
# plt.savefig("assets/img/daily_crime_trend.jpg", format='jpg', bbox_inches='tight')

# plt.show()