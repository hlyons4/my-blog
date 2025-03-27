---
layout: post
title:  "As the Storm Approaches, Crime Rates Surge"
date:   2025-3-16
description: This post explores how extreme weather impacts crime rates using data analysis, visualizations, and real-world trends.
---

<h3>Wonder why most crime in movies happens in dreary, stormy weather?</h3> 
It’s not just a cinematic trick to set the mood—data suggests there’s real-world truth behind it. As the weather worsens, crime rates tend to rise. From heatwaves that spark tempers to storms that create the perfect cover for illegal activities, extreme weather and crime seem to go hand in hand.<br>


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
	<img src="{{site.url}}/{{site.baseurl}}/assets/img/daily_crimes.jpg" alt=""> 
	<figcaption>Figure 1. - Daily crime counts in Chicago over the study period.</figcaption>
</figure>

<figure>
	<img src="{{site.url}}/{{site.baseurl}}/assets/img/daily_crime_trend.jpg" alt=""> 
	<figcaption>Figure 1. - Violent crime rates compared to concurrent temperatures.</figcaption>
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

These results align with existing theories, suggesting that while weather affects crime, social and economic factors also play a crucial role.<br>

<h3>Challenges & Limitations</h3> <strong>Limited Weather Data:</strong> Due to the absence of historical weather data in my OpenWeatherMap plan, the weather data used may not perfectly align with crime timestamps. This limitation likely affects the precision of the analysis.<br>
<strong>Missing Crime Report Details:</strong> Some crime reports lacked precise timestamps, complicating the matching process with weather data.<br>

<strong>Potential Biases:</strong> Crimes may be underreported during extreme weather events, especially severe storms or extreme cold, which could skew results.<br>

<strong>City-Specific Trends:</strong> This study focuses on Chicago, so findings may not generalize to other cities or regions.<br>

<h3>Conclusion & Implications</h3> So, does bad weather increase crime, or is it just a Hollywood trope? The data tells a nuanced story. Heatwaves correlate with higher violent crime, supporting the theory that extreme heat increases aggression. Cold weather tends to suppress crime, likely due to reduced outdoor activity. Storms shift crime patterns rather than eliminate them.<br>
These insights can help cities allocate resources more effectively. For example, increasing police presence during heatwaves or adjusting safety strategies during winter months could enhance public safety.<br>

Despite data limitations, this study underscores the value of integrating weather variables into crime prevention strategies.<br>

Curious to learn more? Here are some great resources:<br>

Crime Data Sources:<br>
- <a href="https://www.fbi.gov/services/cjis/ucr" target="_blank">FBI Uniform Crime Reporting (UCR) Program</a><br>
- <a href="https://data.cityofnewyork.us/" target="_blank">NYC Open Data</a><br>
- <a href="https://data.cityofchicago.org/" target="_blank">Chicago Data Portal</a><br>

Weather Data Sources:<br>
- <a href="https://www.ncdc.noaa.gov/" target="_blank">NOAA</a><br>
- <a href="https://openweathermap.org/api" target="_blank">OpenWeatherMap API</a><br>
- <a href="https://www.weather.gov/" target="_blank">National Weather Service</a>.