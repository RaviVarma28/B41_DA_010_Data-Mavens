import streamlit as st
import pandas as pd
import sys
sys.path.append('scripts')
import Preprocessor
import numpy as np

st.logo("static/Logo.jpg")



col1, col2= st.columns([1,8])

with col1:
    st.image("static/Logo.jpg", width=120)

with col2:
    st.markdown("# Air Quality Index")
    st.markdown('**Air Quality Dataset**, [*via kaggle*](https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set)')


st.subheader('Data Preview:')
st.write(Preprocessor.df.head(), width=1000)

st.subheader("Data Summary:")
st.write(Preprocessor.df.head())

# st.subheader("Highest recorded Pollution level")
pollutant = st.selectbox("**Select the Pollutant**",Preprocessor.pollutant_cols)
if pollutant:
    peak = Preprocessor.df[pollutant].max()
    least = np.sort(Preprocessor.df[pollutant].unique())[1]
    peak_date = Preprocessor.df[Preprocessor.df[pollutant]==peak]['Date'].iloc[0]
    least_date = Preprocessor.df[Preprocessor.df[pollutant]==least]['Date'].iloc[0]
    st.metric(label = 'Highest recorded Pollution level',value=f'{peak} mg/m³ at {peak_date}')
    st.metric(label = 'Lowest recorded Pollution level',value=f'{least} mg/m³ at {least_date}')
    

 