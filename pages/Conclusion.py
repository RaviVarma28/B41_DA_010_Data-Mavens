import streamlit as st

st.logo("static/Logo.jpg")

st.title(':material/check: Conclusion')
st.markdown("""
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
    
    Expand air quality monitoring networks and use real-time data to trigger alerts and inform mitigation strategies dynamically."""
         
)
