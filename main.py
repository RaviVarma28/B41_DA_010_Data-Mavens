import streamlit as st
import pandas as pd

st.title("Air Quality Index")
df = pd.read_csv('data/CleanedAirQuality.csv')

st.markdown('**Air Quality Dataset**, [*via kaggle*](https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set)')

st.text('Sample Dataset:')
st.dataframe(df.head())

st.sidebar.subheader("Select")
pollutant_cols = st.multiselect("Pollutants")