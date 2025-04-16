import pandas as pd
import zipfile
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import BytesIO
import streamlit as st
import numpy as np

#data
dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
np.random.seed(42)

crime_types = {
    'ASSAULT': 'outdoor',
    'ROBBERY': 'outdoor',
    'BURGLARY': 'indoor',
    'NARCOTICS': 'indoor',
    'BATTERY': 'indoor',
    'OTHER OFFENSE': 'mixed'
}

data = []

for date in dates:
    month = date.month
    is_summer = month in [6, 7, 8]
    is_winter = month in [12, 1, 2]
    is_storm = np.random.rand() < 0.1


    temp = np.random.normal(loc=90, scale=5) if is_summer else np.random.normal(loc=30, scale=8) if is_winter else np.random.normal(loc=60, scale=10)
    humidity = np.clip(np.random.normal(70 if is_summer else 60, 10), 20, 100)
    wind = np.clip(np.random.normal(10 if is_storm else 5, 2), 0, 30)

    for crime, location_type in crime_types.items():
        base = 5  

        if crime in ['ASSAULT', 'ROBBERY'] and temp > 85:
            count = np.random.poisson(base + 6)
        elif temp < 35:
            count = np.random.poisson(base - 3)
        else:
            count = np.random.poisson(base)

        
        if is_storm and location_type == 'outdoor':
            count = int(count * 0.3)  

        data.append({
            'date': date,
            'crime_type': crime,
            'location_type': location_type,
            'count': count,
            'temperature': round(temp, 1),
            'humidity': round(humidity, 1),
            'wind_speed': round(wind, 1),
            'storm': int(is_storm)
        })

crime_weather_df = pd.DataFrame(data)


#needed for specific eda graphs
assault_df = crime_weather_df[crime_weather_df["crime_type"] == "ASSAULT"]
daily_assault = assault_df.groupby("temperature")["count"].mean().reset_index()
outdoor_df = crime_weather_df[crime_weather_df["location_type"] == "outdoor"]
storm_crime = outdoor_df.groupby("storm")["count"].sum().reset_index()
storm_crime["storm"] = storm_crime["storm"].map({0: "No Storm", 1: "Storm"})


#streamlit app code
st.title('My Crime Weather App')


tab1, tab2, tab3, tab4 = st.tabs(['Overall','By Crime', 'Average Daily Assault', 'Crime Frequency Heatmap'])

#crime totals by weather type with color as location
with tab1:
    st.write("Total outdoor vs indoor crimes by storm status")
    #quick insights
    st.metric("Total Crimes", value=crime_weather_df['count'].sum())
    st.metric("Avg Temp (°F)", value=round(crime_weather_df['temperature'].mean(), 1))
    st.metric("Storm Days", value=crime_weather_df['storm'].sum())
    #code
    group_loc_storm = crime_weather_df.groupby(['storm', 'location_type'])['count'].sum().reset_index()
    group_loc_storm['storm'] = group_loc_storm['storm'].map({0: 'No Storm', 1: 'Storm'})

    loc_fig = plt.figure(figsize=(10, 6))
    sns.barplot(data=group_loc_storm, x='storm', y='count', hue='location_type')
    plt.title('Total Crime Counts by Location Type During Storms')
    plt.xlabel('Weather Condition')
    plt.ylabel('Total Crime Count')
    plt.legend(title='Location Type')
    #save figure for blog
    loc_fig.savefig("location_vs_storm.png")
    st.pyplot(loc_fig)
    
    #created a drop down menu for crime type
with tab2:
    st.write("Select a crime type to see how its frequency changes with temperature")
    
    unique_crimes = crime_weather_df['crime_type'].unique().tolist()
    noi = st.selectbox("Choose a crime type", unique_crimes)
    plot_crime = st.checkbox('Plot the selected crime type')

    fig = plt.figure(figsize=(15, 8))

    if plot_crime:
        filtered = crime_weather_df[crime_weather_df['crime_type'] == noi]
        sns.lineplot(data=filtered, x='temperature', y='count', label=noi)
        plt.title(f'{noi} Counts at Various Temperatures')
        plt.xlabel('Temperature (°F)')
        plt.ylabel('Crime Count')
        plt.grid(True)
        plt.tight_layout()
        #save figure for blog
        # fig.savefig(f"{noi.lower()}_temp_trend.png")
        st.pyplot(fig)

with tab3:
    pig = plt.figure(figsize=(15, 8))
    sns.scatterplot(data=daily_assault, x="temperature", y="count")
    plt.title("Average Assault Count vs Temperature")
    plt.xlabel("Temperature (°F)")
    plt.ylabel("Average Daily Assault Count")
    plt.grid(True)
    plt.tight_layout()
    #save figure for blog
    pig.savefig("assault_vs_temp.png")
    st.pyplot(pig)
    
with tab4:
    daily_total = crime_weather_df.groupby('date')['count'].sum().reset_index()
    daily_total['month'] = daily_total['date'].dt.month
    daily_total['day'] = daily_total['date'].dt.day

    heat_data = daily_total.pivot_table(index='month', columns='day', values='count', aggfunc='mean')

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.heatmap(heat_data, cmap="YlOrRd", ax=ax)
    plt.title("Crime Frequency Heatmap (Month x Day)")
    #save figure for blog
    fig.savefig("crime_heatmap_calendar.png")
    st.pyplot(fig)

#note: check which packages are not on base python-listed in the requirements file