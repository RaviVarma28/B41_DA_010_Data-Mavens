import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the dataset
data = pd.read_csv('CleanedAirQuality.csv', parse_dates=['Date'], index_col='Date')

# Set up the page title and layout
st.set_page_config(page_title="Insights Dashboard", layout="wide")
st.title("Pollution Insights and Recommendations")

# Sidebar for navigation
st.sidebar.header("Navigation")
section = st.sidebar.selectbox(
    "Choose a section:",
    ("Summary Charts", "Insights & Recommendations")
)

if section == "Summary Charts":
    st.header("Summary Charts")

    # Peak Pollution Periods
    st.subheader("Peak Pollution Periods")

    pollutants = ['CO(GT)', 'NMHC(GT)', 'C6H6(GT)', 'NOx(GT)', 'NO2(GT)']
    daily_pollution = data[pollutants].resample('D').mean()

    # Finding the worst pollution days for each pollutant
    worst_days = daily_pollution.idxmax()
    worst_levels = daily_pollution.max()

    # Creating a summary table
    summary_table = pd.DataFrame({
        'Pollutant': pollutants,
        'Worst Day & Time': worst_days.values,
        'Max Level': worst_levels.values
    })

    # Display the summary table in Streamlit
    st.subheader("Worst Pollution Days")
    st.dataframe(summary_table.reset_index(drop=True),width=1000)

    # Plotting the daily pollution trends
    fig, ax = plt.subplots(figsize=(20, 8))
    for column in daily_pollution.columns:
        sns.lineplot(data=daily_pollution[column], label=column, ax=ax)

    # Customizing the chart
    ax.set_title('Daily Average Pollution Trends', fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Pollution Level (μg/m³)', fontsize=12)
    ax.grid(True)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45, ha='right')
    ax.legend(title='Pollutants', bbox_to_anchor=(1.01, 1), loc='upper left')

    # Display the plot in Streamlit
    st.pyplot(fig)

    # Hourly pollution trends
    hourly_pollution = data[pollutants].groupby(data.index.hour).mean()

    # Finding the worst hourly trends for each pollutant
    hour_levels = hourly_pollution.max()

    # Creating a summary table for hourly trends
    hourly_summary_table = pd.DataFrame({
        'Pollutant': pollutants,
        'Max Level': hour_levels.values
    })

    # Display the summary table for hourly trends
    st.subheader("Hourly Pollution Trends")
    st.dataframe(hourly_summary_table.reset_index(drop=True),width=500)

    # Plotting the hourly pollution trends
    fig, ax = plt.subplots(figsize=(20, 8))
    for column in hourly_pollution.columns:
        sns.lineplot(data=hourly_pollution[column], label=column, ax=ax)

    ax.set_title('Hourly Average Pollution Levels', fontsize=16)
    ax.set_xlabel('Hour of the Day', fontsize=12)
    ax.set_ylabel('Pollution Level (μg/m³)', fontsize=12)
    ax.grid(True)
    ax.legend(title='Pollutants')

    # Display the plot in Streamlit
    st.pyplot(fig)

    
    # Scatter plots of sensor vs. pollutant
    sensor_cols = ['PT08.S1(CO)', 'PT08.S3(NOx)',  'PT08.S4(NO2)', 'PT08.S5(O3)', 'PT08.S2(NMHC)']
    pollutant_cols = ['CO(GT)', 'NOx(GT)', 'NO2(GT)', 'C6H6(GT)', 'NMHC(GT)']

    # Create a 2x3 grid of subplots
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(18, 12))
    axes = axes.flatten()  # Flatten the 2D array of axes to make it easier to iterate over

    # Hide the sixth subplot (the last empty one)
    axes[5].axis('off')

    # Create the sensor-pollutant mapping
    sen_poll = {sensor_cols[x]: pollutant_cols[x] for x in range(len(sensor_cols))}

    # Loop through the dictionary and plot each sensor vs pollutant on the appropriate subplot
    for i, (sensor, pollutant) in enumerate(sen_poll.items()):
        ax = axes[i]  # Get the appropriate subplot (flattened)
        sns.scatterplot(x=data[sensor], y=data[pollutant], alpha=0.5, ax=ax)
        ax.set_title(f'{sensor} vs. {pollutant}')
        ax.grid(True)

    # Adjust the layout to avoid overlapping
    plt.tight_layout()
    st.subheader("Sensors VS Pollutants Relationship")
    # Display the grid of scatter plots in Streamlit
    st.pyplot(fig)

    # Correlation matrix
    correlation_data = data.drop(columns=['Time'])
    correlation_matrix = correlation_data.corr()
    sensor_pollutant_corr = correlation_matrix.loc[sensor_cols, pollutant_cols]

    # Display the correlation matrix in Streamlit
    st.subheader("Correlation Matrix of Sensors and Pollutants")
    st.dataframe(sensor_pollutant_corr, width=1000)

elif section == "Insights & Recommendations":
    st.header("Insights & Recommendations")
        # Display the insights
    st.write("""
    ### INSIGHTS:

    1. **Peak Pollution Periods:**
        - **Worst Pollution Days:** 
          By analyzing the "Worst Pollution Days" table, we can see the specific dates when each pollutant reached its highest levels. These dates may correspond to specific events or periods of the year, such as holidays, traffic congestions, or industrial emissions. 
          For example, if `NO2(GT)` and `CO(GT)` levels spike during peak hours, this suggests that vehicle emissions could be a major factor contributing to poor air quality.

    2. **Daily Average Pollution Trends:**
        - **Pollution Trends:** 
          The daily average pollution trends help us identify seasonal variations in air quality. Pollutants such as `CO(GT)` and `NOx(GT)` are more likely to peak during periods of heavy traffic, while others like `NMHC(GT)` may correlate more closely with industrial emissions. This information is valuable for understanding how pollution levels fluctuate over time and tailoring interventions accordingly.

    3. **Hourly Pollution Trends:**
        - **Hourly Peaks:** 
          Pollution spikes in the early morning and late evening hours, when traffic congestion is at its highest. For example, pollution from `CO(GT)` and `NOx(GT)` might peak during rush hours. Targeting interventions during these specific times can help reduce exposure to harmful pollutants.
        - **Worst Hours for Each Pollutant:** 
          By identifying the specific hours when each pollutant is at its peak, we can make targeted recommendations, such as traffic restrictions or public health warnings for vulnerable populations.

    4. **Sensor-Pollutant Correlation:**
        - **Sensor Accuracy and Pollutant Relation:** 
          Correlation analysis between sensors and pollutants reveals the accuracy of the sensor measurements. High correlation indicates that the sensor is reliably tracking the pollutants, while a low correlation might signal the need for sensor recalibration. For instance, if `PT08.S1(CO)` has a strong correlation with `CO(GT)`, it confirms that this sensor is accurately detecting carbon monoxide levels.
        - **Sensor Calibration:** 
          Sensors that show weak correlations should be calibrated or adjusted to improve their accuracy in pollutant detection.

    5. **Correlation Insights:**
        - **Pollutant Interrelationships:** 
          Some pollutants, such as `NOx(GT)` and `NO2(GT)`, may be produced by similar sources like combustion engines, and their high correlation suggests that strategies to reduce one will likely reduce the other as well.
        - **Air Quality Index (AQI) Relevance:** 
          The correlation between sensors and pollutants provides valuable insights into how reliable the AQI is for forecasting air quality. If multiple pollutants show high correlation with sensors, it suggests the AQI is accurate and can be used effectively in real-time monitoring.""")

    st.write("""
    ### RECOMMENDATIONS:

    **1. Implement Traffic Restrictions:**
    
    Enforce traffic limitations during peak pollution hours, such as early morning and evening rush periods, to reduce vehicular emissions.

    **2. Promote Public Transportation:**
    
    Enhance public transportation systems and incentivize their use to decrease the number of private vehicles on the road.

    **3. Increase Green Spaces:**
    
    Develop more parks, green belts, and urban forests to naturally absorb pollutants and improve air quality.

    **4. Enforce Industrial Emission Controls:**
    
    Strengthen regulations for industrial emissions, especially during periods identified as high-pollution days.

    **5. Launch Public Awareness Campaigns:**
    
    Educate communities about pollution peaks and suggest protective measures to minimize exposure during high-risk times.

    **6. Encourage Flexible Work Hours:**
    
    Promote staggered or remote work options to distribute traffic evenly and avoid rush-hour congestion.

    **7. Establish Low Emission Zones (LEZs):**
    
    Restrict or levy fees on high-emission vehicles in designated areas with heavy pollution to encourage cleaner alternatives.

    **8. Adopt Smart Urban Planning:**
    
    Design city layouts that separate residential areas from industrial zones and high-traffic corridors to reduce direct pollutant exposure.

    **9. Incentivize Renewable Energy Adoption:**
    
    Encourage businesses and households to shift to renewable energy sources like solar and wind to cut down on emissions from fossil fuels.

    **10. Strengthen Monitoring and Data Utilization:**
    
    Expand air quality monitoring networks and use real-time data to trigger alerts and inform mitigation strategies dynamically.
    """)