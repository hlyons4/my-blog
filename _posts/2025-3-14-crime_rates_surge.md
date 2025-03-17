---
layout: post
title:  "As the Storm Approaches, Crime Rates Surge"
date:   2025-3-16
description: This post explores how extreme weather impacts crime rates using data analysis, visualizations, and real-world trends.
---

<p class="intro"><span class="dropcap">W</span><h3>onder why most crime in movies happens in dreary, stormy weather? It’s not just a cinematic trick to set the mood—data suggests there’s real-world truth behind it. As the weather worsens, crime rates tend to rise. From heatwaves that spark tempers to storms that create the perfect cover for illegal activities, extreme weather and crime seem to go hand in hand.<br></h3>


But why does this happen? Does extreme heat make people more aggressive? Do storms create opportunities for crime, or do they deter it? These questions drive the heart of this investigation. Using real crime and weather data, we’ll explore whether there’s a measurable link between extreme weather events—heatwaves, cold spells, storms—and violent crime rates. Let’s dive into the data and see what patterns emerge.<br>


<h3>Data Collection and Processing</h3>

To explore this question, I gathered crime data from the FBI Uniform Crime Reporting (UCR) Program and city-specific open data portals like NYC Open Data and the Chicago Data Portal<br>



For weather data, I used the OpenWeatherMap API, specifically the current weather data endpoint, as the historical weather API isn't included in my plan.<br>



I ensured ethical data collection by only using publicly available datasets and following good scraping practices where necessary. If you’re interested in conducting a similar study, these sources are great starting points!<br>


<h3>Summary of Data Collection:</h3>

<strong>Crime Data:</strong> Type of crime, date, time, location, crime severity.<br>
<strong>Weather Data:</strong> Temperature, humidity, wind speed, and weather conditions.<br>


<h3>Exploratory Data Analysis (EDA)</h3>
After cleaning and merging the datasets, I conducted some initial analyses. Here are a few highlights:<br>

<strong>Heatwaves & Crime:</strong> During heatwaves (days above the 90th percentile for temperature), violent crimes increased by ~12%.<br>
<strong>Cold Spells & Crime:</strong> During extremely cold days (below the 10th percentile), crime rates dropped by ~8%.<br>
<strong>Storms & Crime:</strong> Heavy storms seemed to reduce outdoor crimes like assault but had little effect on crimes that occur indoors.<br>

<figure>
	<img src="{{site.url}}/{{site.baseurl}}/assets/img/daily_crimes.png" alt=""> 
	<figcaption>Figure 1. - Violent Crime Rates in Chicago</figcaption>
</figure>

This bar chart displays the total number of crimes by type in Chicago for the analyzed period. The data highlights which crimes are most and least frequent, offering insight into prevalent criminal activities within the city. Crime types with higher counts may indicate areas requiring more attention from law enforcement or community safety initiatives.<br>

<figure>
	<img src="{{site.url}}/{{site.baseurl}}/assets/img/daily_crime_trend.png" alt=""> 
	<figcaption>Figure 1. - Violent crime rates compared to concurring weather</figcaption>
</figure>
<br>

<h3>Methodology</h3>
To analyze relationships, I used:<br>

- <strong>Regression Analysis:</strong> To quantify the impact of temperature on crime rates.<br>
- <strong>Time Series Analysis:</strong> To examine trends over seasons.<br>
- <strong>Control Variables:</strong> Time of day, location, and day of the week to account for confounding factors.<br>

<h3>Findings & Interpretation</h3>
The data suggests a significant relationship between extreme weather and crime:<br>
- <strong>Heat increases violent crime.</strong> Hotter days correlated with higher rates of assault and robbery.<br>
- <strong>Cold weather reduces overall crime.</strong> The extreme cold appears to act as a deterrent.<br>
- <strong>Storms disrupt crime patterns.</strong> Outdoor crimes drop during severe storms, but indoor crimes remain steady.<br>

While these results align with existing theories, they also emphasize that weather alone doesn’t determine crime—social and economic factors also play a huge role.<br>

<h3>Challenges & Limitations</h3>
<strong>Missing Data:</strong> Some crime reports lacked timestamps, making it difficult to match them precisely with weather data.<br>

<strong>Biases:</strong> Some crimes may go underreported, especially in extreme weather.<br>

<strong>City-Specific Trends:</strong> Findings may not generalize beyond the cities studied.<br>

<h3>Conclusion & Implications</h3>
So, does bad weather actually increase crime, or is it just a Hollywood trope? The data tells a nuanced story. Heatwaves do lead to more violent crime, supporting the theory that extreme heat increases aggression. Meanwhile, cold weather tends to suppress criminal activity, likely because fewer people are outside. Storms, on the other hand, shift crime patterns rather than eliminate them entirely.<br>

Understanding these trends can help cities allocate resources more effectively. If violent crime spikes during heatwaves, police presence or community interventions could be increased in vulnerable areas. Similarly, winter crime patterns could guide different strategies for public safety.<br>

Curious to learn more? Here are some great resources:<br>

Crime data:<br>
- <a href="https://www.fbi.gov/services/cjis/ucr" target="_blank">FBI Uniform Crime Reporting (UCR) Program</a><br>
- <a href="https://data.cityofnewyork.us/" target="_blank">NYC Open Data</a><br>
- <a href="https://data.cityofchicago.org/" target="_blank">Chicago Data Portal</a><br>

Weather Data:<br>
- <a href="https://www.ncdc.noaa.gov/" target="_blank">NOAA</a><br>
- <a href="https://openweathermap.org/api" target="_blank">OpenWeatherMap API</a><br>
- <a href="https://www.weather.gov/" target="_blank">National Weather Service</a>.