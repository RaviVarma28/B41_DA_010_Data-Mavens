import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sys
sys.path.append('..\scripts')
import Preprocessor

st.logo("static/Logo.jpg")

col1, col2 = st.columns([1,3])

# with col1:
    # st.image('../')
with col2:
    st.markdown("# Visualizations:")

pollutant = st.multiselect("Select the Pollutant(s):", Preprocessor.pollutant_cols)


if pollutant:
    st.subheader("Trend")
    st.metric(label = 'Bullshit', value = f"{int(Preprocessor.df[pollutant].mean().iloc[0])}")

else:
    st.write('No Pollutant is selected for Visualization')

tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")
