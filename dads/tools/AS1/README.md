# 2023-2024 Global Air Quality: PM2.5

![image](https://imgur.com/9Smq6ou.jpg)


## Project Description
This project aims to analyze global air quality using PM2.5 data from [World Air Quality Data 2024 (Updated)](https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated), which includes data from 8,469 stations in 65 countries, with PM2.5 being the main parameter used for analysis. The project showcases an overall picture of PM2.5 pollution levels from the years 2023-2024 on a geographic map with Scatter Plots on Mapbox, which helps in exploring differences in PM2.5 pollution levels in different areas.


## Data and Data Source
[World Air Quality Data 2024 (Updated)](https://www.kaggle.com/datasets/kanchana1990/world-air-quality-data-2024-updated) has been collected from 8,469 locations across 65 countries, with data sourced from 105 governmental and research organizations through [OpenAQ](https://public.opendatasoft.com/explore/dataset/openaq/export/?disjunctive.city&disjunctive.location&disjunctive.measurements_parameter&sort=measurements_lastupdated&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJsaW5lIiwiZnVuYyI6IkFWRyIsInlBeGlzIjoibWVhc3VyZW1lbnRzX3ZhbHVlIiwic2NpZW50aWZpY0Rpc3BsYXkiOnRydWUsImNvbG9yIjoicmFuZ2UtY3VzdG9tIn1dLCJ4QXhpcyI6Im1lYXN1cmVtZW50c19sYXN0dXBkYXRlZCIsIm1heHBvaW50cyI6IiIsInRpbWVzY2FsZSI6ImRheSIsInNvcnQiOiIiLCJzZXJpZXNCcmVha2Rvd24iOiJtZWFzdXJlbWVudHNfcGFyYW1ldGVyIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJvcGVuYXEiLCJvcHRpb25zIjp7ImRpc2p1bmN0aXZlLmNpdHkiOnRydWUsImRpc2p1bmN0aXZlLmxvY2F0aW9uIjp0cnVlLCJkaXNqdW5jdGl2ZS5tZWFzdXJlbWVudHNfcGFyYW1ldGVyIjp0cnVlLCJzb3J0IjoibWVhc3VyZW1lbnRzX2xhc3R1cGRhdGVkIn19fV0sImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9&location=2,2.98693,49.21875&basemap=jawg.light) 
Each data entry contains key air quality parameters such as PM2.5, NO2, SO2, CO, and O3, spanning from 2015 to March 2024, along with geographic coordinates. This dataset serves as a valuable resource for understanding the current status and trends of global air quality.

PM2.5 consists of fine particulate matter that is small, lightweight, and poses significant health risks. Due to their small size, PM2.5 particles remain airborne for longer periods, increasing the likelihood of inhalation. Exposure to PM2.5 has been linked to respiratory diseases such as asthma, bronchitis, and other lung conditions, as well as cardiovascular diseases. According to research published in the American Medical Association Journal, prolonged exposure to PM2.5 contributes to plaque formation in arteries, leading to inflammation, arterial stiffening, and increased risks of heart disease and stroke. Given these severe health impacts, this study primarily focuses on PM2.5 pollution.
     

## Distribution of PM2.5 Pollution Levels - Visualize with Scatter Plots on Mapbox

A scatter plot visualization on Mapbox is used to represent PM2.5 pollution levels across different regions. By leveraging geographic coordinates, the scatter plots display air quality monitoring locations, where the color of each point corresponds to the level of PM2.5 pollution at that location. This visualization provides an annual overview of PM2.5 pollution trends, making it easier to understand air quality conditions across regions.

The severity of PM2.5 pollution is categorized according to the National Ambient Air Quality Standards for Particle Pollution, using the following color-coded levels:

* Green: Low
* Yellow: Moderate
* Orange: Unhealthy for Sensitive Groups
* Red: Unhealthy
* Purple: Very Unhealthy

This interactive PM2.5 pollution map can aid decision-making in research and environmental policy. Areas classified as "Very Unhealthy" can be further examined to identify pollution sources and mitigation strategies. For example, regions near airports or industrial zones may require stricter pollution control measures to minimize health risks for nearby populations.


## Observation
The PM2.5 pollution map reveals that "Unhealthy" PM2.5 levels are widely distributed across Europe and various cities in Mexico (located in the lower part of North America). Furthermore, a high concentration of "Very Unhealthy" PM2.5 levels is observed in northern Thailand, near the Myanmar border.

Data from 2023–2024 indicates that most air quality measurements were collected from North America and Europe, where "Low" and "Moderate" PM2.5 levels are predominant.
