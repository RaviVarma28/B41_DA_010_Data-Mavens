import streamlit as st

st.logo("static/Logo.png")

st.title(':material/check: Conclusion')
st.markdown("""This project has successfully demonstrated the use of Streamlit and Python for visualizing and analyzing air quality data. The UCI Machine Learning Repository’s dataset has provided valuable insights into the relationships between sensor responses and pollutant concentrations. Through interactive scatter plots and real-time filtering, users have been able to explore correlations and trends in air quality data.

### Key takeaways include:

- **Data Exploration**:   
            The interactive visualizations have highlighted the various correlations between sensors and pollutant concentrations. Notably, while one pollutant shows a negative correlation with its sensor, the other three exhibit positive correlations.
- **Data Preprocessing**:   
            The approach of replacing missing values with calculated medians has ensured that only valid data points were considered in the analysis.
- **User-Friendly Interface**:  
            The Streamlit dashboard offers an intuitive, engaging platform for exploring and interpreting the data.
This web application provides an effective way to monitor and analyze air quality, offering insights into pollutant behavior and sensor performance.""")

st.write("""
    ## RECOMMENDATIONS:
         
    Based on the findings of this project, the following actions could help improve air quality in urban environments:

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
