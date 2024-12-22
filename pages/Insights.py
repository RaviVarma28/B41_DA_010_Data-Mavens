import streamlit as st
import sys
sys.path.append('..\scripts')
import Preprocessor

st.logo("static/Logo.png")


st.title(':material/stacked_bar_chart: Insights Dashboard',help='This is for insights')

tabs = st.tabs(Preprocessor.pollutant_cols)

for i, tab in enumerate(tabs):

    with tab:

        col1,col2=st.columns(2)

        with col1:
            st.subheader(f'Scatter Plot for {Preprocessor.pollutant_cols[i]}',divider='rainbow',help='Scatter Plot shows the relation between two variables')
            Preprocessor.scatter(Preprocessor.pollutant_cols[i])

        with col2:
            st.subheader(f'Box Plot',divider='rainbow',help='BoxPlot is used for identifying the descriptive statistics and the outlirers in the data')
            Preprocessor.box(Preprocessor.pollutant_cols[i])

        st.markdown('## Summary:')

        if Preprocessor.pollutant_cols[i] == 'CO(GT)':
            st.write("""
- **Positive Correlatio**:The scatter plot's strong correlation suggests the sensor is performing well, with outliers requiring further investigation.    
- **Outliers**: Outliers in both plots could be related to sensor anomalies, calibration issues, or external environmental conditions affecting measurements. These outliers should be examined for possible sensor drift or cross-sensitivity.     
- **Trend**: The overall trends confirm that the PT08.S1(CO) sensor readings align with the CO(GT) ground truth for most cases, indicating reliable performance within normal operating conditions.
""")
        
        if Preprocessor.pollutant_cols[i] == 'NOx(GT)':
            st.write("""
- **Nonlinear Sensor Response**: The PT08.S3(NOx) sensor's behavior is complex, possibly saturating at high NOx(GT) concentrations or being influenced by other environmental factors. Cross-check the performance of PT08.S3(NOx) with other sensors measuring similar pollutants for validation.
- **Pollution Events**: The outliers in the visualizations point to rare but significant pollution episodes that may need further examination.
- **Skewed Pollution Levels**: The skew in NOx(GT) levels suggests that high concentrations are relatively rare but impactful.
""")
        
        if Preprocessor.pollutant_cols[i] == 'NO2(GT)':
            st.write("""
- **Stable Pollution Patterns**: NO2 exhibits a predictable and stable distribution, suggesting consistent sources and environmental conditions.
- **Minimal Extremes**: Few outliers indicate the absence of frequent extreme pollution events for NO2. We can use the centralized nature of NO2 data as a feature in predictive modeling, as its consistent behavior may improve model accuracy.
- **Reliable Sensor Performance**: If the scatter plot involves a sensor, its response likely aligns well with the ground truth data for NO2.
""")
        
        if Preprocessor.pollutant_cols[i] == 'NMHC(GT)':
            st.write("""
- **Positive Correlation**: The positive correlation in the scatter plot suggests that the sensor PT08.S2(NMHC) is a reliable indicator of NMHC(GT) levels. This can be useful for real-time monitoring and quick assessments of pollution levels using sensor data.
- **Distribution and Variability**: The box plot indicates the central tendency and spread of NMHC(GT) levels. The presence of outliers suggests occasional spikes in pollutant concentration, which could be due to specific events or conditions.
- **Data Anomalies**: Identifying outliers helps in understanding anomalies in the data, which could be caused by sensor malfunctions, specific environmental conditions, or other factors. Addressing these anomalies is crucial for accurate data analysis and decision-making.
""")