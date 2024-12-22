import streamlit as st
import sys
sys.path.append('..\scripts')
import Preprocessor

st.logo("static/Logo.png")

st.title(":material/data_exploration: Visualization Dashboard")

st.subheader("Correlation Matrix of Sensors and Pollutants",
             divider='rainbow',
             help="""Correlation tells you the type of relationship between two variables in a numerical form.  
                - Heatmaps is visualization of it""")

col1, col2 = st.columns(2)
   
with col2:
    st.dataframe(Preprocessor.correlation_matrix(), width=1000)
     
with col1:
    Preprocessor.corr()

tab1,tab2,tab3 = st.tabs(["**Trends**",'**Bar Chart**','**Histograms**'])

with tab1:

    col3,col4 = st.columns([1,1.5])
    st.subheader("Line Plots",divider='rainbow',help='Shows trend over time')
    with col3:
        pollutant_for_line = Preprocessor.multiselect("Select Pollutant(s) for line plot:", Preprocessor.pollutant_cols)

    if pollutant_for_line:
        col5, col6 = st.columns(2)  

        with col5:
            st.subheader("Hourly Average Pollution over a Year")
            Preprocessor.hourly(pollutant_for_line)

        with col6:
            
            st.subheader("Monthly Average Pollution over a Year")
            Preprocessor.monthly(pollutant_for_line)
        

        col7, col8 = st.columns([1,7])
        
        with col7:
            month = st.radio('# Months',['March','April'])
        with col8:
            st.subheader("Daily Average Pollution over a Year per Month")
            Preprocessor.daily(pollutant_for_line,month)

        

    else:
        st.write('No Pollutant is selected for Visualization')

with tab2:

    st.subheader("Bar Charts",divider='rainbow',)
    col9,col10 = st.columns([1,1.5])
    with col9:
        pollutant_for_bar = Preprocessor.multiselect("Select Pollutant(s) for Bar chart:", Preprocessor.pollutant_cols)

    col7, col8 = st.columns(2)

    if pollutant_for_bar:
        

        with col7:
            st.subheader("Pollution on Weekdays and Weekends")
            Preprocessor.bar(pollutant_for_bar)

        with col8:
            st.subheader("Average populatant concentration over a Year")
            Preprocessor.avg_bar(pollutant_for_bar)

    else:
        st.write("No Pollutants selected for Visualization")

with tab3:
    
    st.subheader("Histograms",divider='rainbow',)
    pollutant = Preprocessor.selectbox("Pollutant:",Preprocessor.pollutant_cols)

    if pollutant:
        Preprocessor.histogram(pollutant)
