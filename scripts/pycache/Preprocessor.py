import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# Load the dataset
data = pd.read_csv(
    r'C:\Users\Welcome\Desktop\PROJECT\B41_DA_010_Data-Mavens\data\CleanedAirQuality.csv', 
    parse_dates=['Date'], index_col='Date'
)

sensor_cols = ['PT08.S1(CO)', 'PT08.S3(NOx)', 'PT08.S4(NO2)', 'PT08.S2(NMHC)']
pollutant_cols = ['CO(GT)', 'NOx(GT)', 'NO2(GT)', 'NMHC(GT)']
weather_cols = ['T', 'RH', 'AH']

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

    # Removing values equal to -200 in 'NMHC(GT)' column
    data = data[data['NMHC(GT)'] > -200]

    # Creating a function for identifying outliers and removing them
    def outliers(data, cols):
        for col in cols:
            q1 = np.quantile(data[col], 0.25)
            q3 = np.quantile(data[col], 0.75)
            iqr = q3 - q1
            lb = q1 - 1.5 * iqr
            ub = q3 + 1.5 * iqr
            data = data[(data[col] >= lb) & (data[col] <= ub)]
        return data

    # Creating a list of columns for checking outliers
    cols_outl = sensor_cols + pollutant_cols
    data_out = outliers(data, cols_outl)

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
    st.dataframe(summary_table.reset_index(drop=True), width=1000)

    # Plotting the daily pollution trends
    fig, ax = plt.subplots(figsize=(20, 8))
    for column in daily_pollution.columns:
        sns.lineplot(data=daily_pollution[column], label=column, ax=ax)
    ax.set_title('Daily Average Pollution Trends', fontsize=16)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Pollution Level (μg/m³)', fontsize=12)
    ax.grid(True)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    plt.xticks(rotation=45, ha='right')
    ax.legend(title='Pollutants', bbox_to_anchor=(1.01, 1), loc='upper left')
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
    st.subheader("Hourly Pollution Trends")
    st.dataframe(hourly_summary_table.reset_index(drop=True), width=500)

    # Plotting the hourly pollution trends
    fig, ax = plt.subplots(figsize=(20, 8))
    for column in hourly_pollution.columns:
        sns.lineplot(data=hourly_pollution[column], label=column, ax=ax)
    ax.set_title('Hourly Average Pollution Levels', fontsize=16)
    ax.set_xlabel('Hour of the Day', fontsize=12)
    ax.set_ylabel('Pollution Level (μg/m³)', fontsize=12)
    ax.grid(True)
    ax.legend(title='Pollutants')
    st.pyplot(fig)

    # Extracting the Month from the Date
    data_out['Month'] = data_out.index.month_name()  # Extract month name from Date

    # Ensure the months are in the correct order (January to December)
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    data_out['Month'] = pd.Categorical(data_out['Month'], categories=month_order, ordered=True)

    # Grouping by 'Month' and calculating the mean for each pollutant
    monthly_trends = data_out.groupby('Month')[pollutant_cols].mean()

    # Plotting monthly pollution trends
    fig, ax = plt.subplots(figsize=(15, 8))
    monthly_trends.plot(kind='line', marker='o', ax=ax)  # Added markers for better visibility
    ax.set_title('Monthly Pollution Trends', fontsize=14, fontweight='bold')
    ax.set_ylabel('Pollution Level (μg/m³)', fontsize=12)
    ax.set_xlabel('Month of the Year', fontsize=12)
    ax.legend(title='Pollutants', bbox_to_anchor=(1.01, 1), loc='upper left')
    ax.set_xticks(range(len(monthly_trends.index)))
    ax.set_xticklabels(monthly_trends.index, rotation=0)
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot(fig)
    # Scatter plots of sensor vs. pollutant
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(18, 12))
    axes = axes.flatten()
    sen_poll = {sensor_cols[x]: pollutant_cols[x] for x in range(len(sensor_cols))}
    for i, (sensor, pollutant) in enumerate(sen_poll.items()):
        sns.scatterplot(x=data_out[sensor], y=data_out[pollutant], alpha=0.7, s=50, ax=axes[i])
        axes[i].set_title(f'{sensor} vs. {pollutant}')
        axes[i].set_xlabel(sensor)
        axes[i].set_ylabel(pollutant)
    for i in range(len(sen_poll), len(axes)):
        axes[i].axis('off')
    plt.tight_layout()
    st.subheader("Sensors vs Pollutants Relationship")
    st.pyplot(fig)

    # Correlation Matrix of Pollutants vs Climate
    st.subheader("Correlation Heatmaps")

    # Prepare data
    weather_pollut = data_out[pollutant_cols + weather_cols]
    weather_pollut_corr = weather_pollut.corr()

    correlation_data = data_out[sensor_cols + pollutant_cols + weather_cols]
    correlation_matrix_full = correlation_data.corr()
    sensor_pollutant_corr = correlation_matrix_full.loc[sensor_cols, pollutant_cols]

    # Create columns for side-by-side heatmaps
    col1, col2 = st.columns(2)

    # Plot Pollutants vs. Climate
    with col1:
        st.subheader("Pollutants vs Climate")
        fig1, ax1 = plt.subplots(figsize=(8, 6))
        sns.heatmap(
            weather_pollut_corr.loc[weather_cols, pollutant_cols],
            cmap='coolwarm',
            annot=True,
            fmt=".2f",
            linewidths=0.5,
            cbar_kws={'label': 'Correlation Coefficient'},
            ax=ax1
        )
        ax1.set_title('Weather Variables vs Pollutants', fontsize=14, fontweight='bold')
        ax1.set_xlabel('Pollutants', fontsize=12)
        ax1.set_ylabel('Weather Variables', fontsize=12)
        plt.tight_layout()
        st.pyplot(fig1)

    # Plot Sensors vs. Pollutants
    with col2:
        st.subheader("Sensors vs Pollutants")
        fig2, ax2 = plt.subplots(figsize=(8, 6))
        sns.heatmap(
            sensor_pollutant_corr,
            cmap='coolwarm',
            annot=True,
            fmt=".2f",
            linewidths=0.5,
            cbar_kws={'label': 'Correlation Coefficient'},
            ax=ax2
        )
        ax2.set_title('Sensors vs Pollutants', fontsize=14, fontweight='bold')
        ax2.set_xlabel('Pollutants', fontsize=12)
        ax2.set_ylabel('Sensors', fontsize=12)
        plt.tight_layout()
        st.pyplot(fig2)


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