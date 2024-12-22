import streamlit as st
import sys
sys.path.append('..\scripts')
import Preprocessor

st.logo("static/Logo.jpg")


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
        st.write(f'{Preprocessor.pollutant_cols[i]}')