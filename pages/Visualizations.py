import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('..\scripts')
import Preprocessor

st.logo("static/Logo.jpg")

st.title(":material/data_exploration: Visualization Dashboard")

st.subheader("Correlation Matrix of Sensors and Pollutants")
col3, col4 = st.columns(2)
   
with col4:
    st.dataframe(Preprocessor.correlation_matrix(), width=1000)
     
with col3:
    Preprocessor.corr()

tab1,tab2,tab3 = st.tabs(["**Trends**",'**Bar Chart**','**Histograms**'])

with tab1:
    st.subheader("Line Plots")
    pollutant_for_line = Preprocessor.multiselect("Select Pollutant(s) for line plot:", Preprocessor.pollutant_cols)

    if pollutant_for_line:

        col5, col6 = st.columns(2)

        with col5:
            st.subheader("Hourly Average Pollution over a Year")
            Preprocessor.hourly(pollutant_for_line)

        with col6:
            st.subheader("Daily Average Pollution over a Year")
            Preprocessor.daily(pollutant_for_line)

        with col5:
            st.subheader("Monthly Average Pollution over a Year")
            Preprocessor.monthly(pollutant_for_line)
        

    else:
        st.write('No Pollutant is selected for Visualization')

with tab2:

    st.subheader("Bar Charts")
    pollutant_for_bar = Preprocessor.multiselect("Select Pollutant(s) for Bar chart:", Preprocessor.pollutant_cols)

    col7, col8 = st.columns(2)

    if pollutant_for_bar:

        with col7:
            Preprocessor.bar(pollutant_for_bar)

        with col8:
            Preprocessor.avg_bar(pollutant_for_bar)

    else:
        st.write("No Pollutants selected for Visualization")

with tab3:
    
    st.subheader("Histograms")
    pollutant = Preprocessor.selectbox("Pollutant:",Preprocessor.pollutant_cols)

    if pollutant:
        Preprocessor.histogram(pollutant)
