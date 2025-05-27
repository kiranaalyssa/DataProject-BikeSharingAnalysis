# IDCamp 2024 - Bike Sharing Analysis 🚴‍♀️
## **Business Understanding**
As the need for eco-friendly and efficient transportation increases, bike-sharing systems have become a modern solution. These systems automate the entire process — from membership to renting and returning bikes. Users can easily rent a bike from one location and return it to another. Today, there are over 500 bike-sharing programs around the world, with more than 500,000 bikes in use.

Bike-sharing systems not only help reduce traffic and pollution but also generate valuable data. Unlike other public transportation systems, they record details such as trip duration, start location, and end location. This turns the system into a virtual sensor network that tracks how people move around the city.

By analyzing this data, the government and service providers can gain useful insights to improve infrastructure, support better decision-making, and solve traffic and environmental problems more effectively.

## **Project Scope**
This project aims to analyze bike sharing data to uncover insights about user behavior and system usage patterns. By processing and visualizing the data, the project helps provide a better understanding of how bike sharing systems operate and their impact on urban mobility.

The project involves the following steps:
* Data wrangling to collect, assess, and clean the bike sharing dataset from Kaggle.
* Exploratory Data Analysis (EDA) to identify trends, patterns, and important factors in the data.
* Development of an interactive dashboard using Python’s Streamlit.

## Preparation 
### Data Source: https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset

### Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data_bike-sharing
cd proyek_analisis_data_bike-sharing
pipenv install
pipenv shell
jupyter-notebook
```
### Run steamlit app
```
streamlit run dashboard.py
```

## Conclusion
Based on the dashboard built with Streamlit, here are some key insights:

1. In 2012, the number of bike-sharing users increased significantly compared to 2011. This can be seen from the higher number of registered users compared to casual users.
2. The highest bike-sharing usage in 2011 happened in June (month 6), while in 2012 it peaked in September (month 9).
3. Bike usage is much higher on working days than on holidays.
4. Registered users use bikes more often on working days compared to casual users.
5. Fall is the season with the highest number of bike-sharing users, followed by summer.
6. In clear weather, both casual and registered users tend to use bike-sharing more.
7. When the wind speed is low (between 0.05–0.18), more people still use bikes, compared to when the wind speed is higher.

Overall, the visualizations in this dashboard show user behavior and patterns for both 2011 and 2012.

## Recommended Action Items
* **Increase Support for Registered Users.** Since registered users dominate weekday usage, consider offering loyalty programs, discounts, or better bike availability during peak commuting hours to improve user retention.
* **Promote Bike Sharing on Weekends.** Casual user numbers are lower on weekends. Launch marketing campaigns, weekend passes, or events to encourage more weekend usage.
* **Seasonal Maintenance Planning.** Fall has the highest bike usage, followed by summer. Ensure more maintenance staff and available bikes during these seasons to meet demand.
* **Time-Based Demand Adjustment.** Since peak months are different between 2011 and 2012 (June vs. September), regularly monitor usage trends to adjust operational resources based on real-time and seasonal patterns.
* **Encourage Registration for Casual Users.** Highlight the benefits of registering (cheaper prices or priority access) to convert casual users into registered users, especially those who frequently use bikes during good weather.
