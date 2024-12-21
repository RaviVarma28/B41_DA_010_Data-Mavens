import streamlit as st

st.logo("static/Logo.jpg")

st.title(':material/quiz: About')

subject = """
## Air Quality Monitoring and Analysis Using Streamlit
### Overview
This project focuses on monitoring, analyzing, and visualizing air quality data using Python and Streamlit. The aim is to provide an interactive and intuitive web application for exploring pollutant concentrations and sensor data from a real-world deployment in an Italian city.

### Dataset Context
The dataset used in this project originates from the UCI Machine Learning Repository and contains the responses of a gas multisensor device deployed at road level in a significantly polluted area. Data were recorded hourly from March 2004 to February 2005, representing one of the longest freely available recordings of air quality chemical sensor responses. The ground truth values were obtained from a certified analyzer and include hourly averages for:

- Carbon Monoxide (CO)
- Non-Methanic Hydrocarbons
- Total Nitrogen Oxides (NOx)
- Nitrogen Dioxide (NO2)

The dataset also includes responses from 5 metal oxide chemical sensors embedded in the multisensor device. Missing values are denoted by -200.

### Key Features
1. Interactive Visualizations:

    - Scatter plots for analyzing relationships between pollutant concentrations and sensor responses.
    - Real-time filtering to focus on specific data subsets.


2. Data Preprocessing:

    - Replacement of missing values (-200) improve data usability.
    - Filtering to ensure only valid sensor responses and pollutant concentrations are used in visualizations.
3. Dataset Highlights:

    - Includes 9357 instances of hourly-averaged data spanning a year.
    - Captures real-world challenges such as sensor drift and cross-sensitivity.
4. Streamlit-Powered Dashboard:

    - An intuitive web-based interface for exploring data trends and relationships.
    - Automatic axis assignment and interactive features for detailed analysis.
### Methodology
1. Data Cleaning:

    - Erroneous values (-200) are replaced with calculated medians to address missing data.
    - Filters ensure only valid entries are considered for analysis and visualization.
2. Interactive Visualization:

    - Scatter plots are generated to reveal patterns and correlations.
    - Dynamic tooltips provide additional context for each data point.
3. Coding Implementation:

    - Pandas is used for data cleaning and manipulation.
    - Streamlit serves as the front-end framework for interactive dashboards.
### Project Objectives
- Explore sensor responses and their correlation with pollutant concentrations.
- Handle real-world data challenges, including missing values and sensor drift.
- Create a user-friendly interface for visualizing air quality data.
- Future Enhancements
- Add time-series visualizations to observe trends over the recorded year.
- Extend analysis to cover the effects of sensor drift and cross-sensitivity.
- Integrate predictive models for estimating pollutant levels based on sensor data."""

st.markdown(subject)