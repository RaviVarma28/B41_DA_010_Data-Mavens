import streamlit as st
import sys
sys.path.append('..\scripts')
import Preprocessor

st.logo("static/Logo.jpg")

col1, col2 = st.columns([1,3])


with col2:
    st.markdown('# Insights')

pollutant = st.selectbox("Select the Pollutant(s):", Preprocessor.pollutant_cols)