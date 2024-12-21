import streamlit as st
import sys
sys.path.append('..\scripts')
import Preprocessor

st.logo("static/Logo.jpg")


st.title(':material/stacked_bar_chart: Insights Dashboard')


tab1, tab2, tab3, tab4 = st.tabs(Preprocessor.pollutant_cols)

with tab1:
    st.write("Scatter Plot between True Hourly Pollutant and Sensor")
    Preprocessor.scatter(Preprocessor.pollutant_cols[0])

with tab2:
    st.write("Scatter Plot between True Hourly Pollutant and Sensor")
    Preprocessor.scatter(Preprocessor.pollutant_cols[1])

with tab3:
    st.write("Scatter Plot between True Hourly Pollutant and Sensor")
    Preprocessor.scatter(Preprocessor.pollutant_cols[2])

with tab4:
    st.write("Scatter Plot between True Hourly Pollutant and Sensor")
    Preprocessor.scatter(Preprocessor.pollutant_cols[3])