import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
df = pd.read_csv('data/CleanedAirQuality.csv')

df['Date'] = pd.to_datetime(df['Date']).dt.date
df['Time'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.time


sensor_cols = ['PT08.S1(CO)', 'PT08.S3(NOx)',  'PT08.S4(NO2)', 'PT08.S2(NMHC)']
pollutant_cols = ['CO(GT)', 'NOx(GT)', 'NO2(GT)', 'NMHC(GT)']
weather_cols = ['T', 'RH', 'AH']

def scatter(pollutant):
    
    # Select corresponding sensor (Elements in lists are already in place)
    num = pollutant_cols.index(pollutant)
    sensor = sensor_cols[num]

    # Filter data
    temp_df = df[(df[pollutant] > -200) & (df[sensor] > -200)].copy()
    temp_df = temp_df[[sensor, pollutant]].dropna()  # Drop rows with NaN

    # Create Plotly scatter plot
    fig = px.scatter(
        temp_df,
        x=sensor,
        y=pollutant,
        title=f"{sensor} vs. {pollutant}",
        labels={sensor: f"{sensor} Reading", pollutant: f"{pollutant} Level"},
        opacity=0.6,
    )
    st.plotly_chart(fig)


def correlation_matrix():
    
    correlation_data = df.drop(columns=['Time','Date']) # Drop the object type columns

    # Filtering the data, so that only numbers above -200 remain
    # In the data provided, it is stated that missing values are given a default value of -200
    correlation_data = correlation_data[(correlation_data[correlation_data.columns]>-200).all(axis=1)]
    correlation_matrix = correlation_data.corr()

    # Taking sensor_cols as rows
    sensor_pollutant_corr = correlation_matrix.loc[sensor_cols, pollutant_cols]
    return sensor_pollutant_corr

def corr():
    
    # heatmap in plotly
    fig = px.imshow(correlation_matrix(),
                    text_auto='.2f',
                    labels=dict(x='Pollutants',y='Sensors',color='Correlation'),
                    color_continuous_scale='sunset',
                    title="Heatmap across Sensors and Pollutants")
    st.plotly_chart(fig)

# Code used previously for multiselect
####################################################################################
# def multiselect(title, options_list):
#     selected = st.multiselect(title, options_list, key=title+'_key')
#     select_all = st.checkbox("Select all", value = False, key = title+'_checkbox')
#     # if selected = None: return False
#     if select_all:
#       selected_options = options_list
#     else:
#       selected_options = selected
#     return selected_options
#####################################################################################


def multiselect(title, options_list):
    
    # creating a popover
    with st.popover(title):
        
        # creating a select all option
        select_all = st.checkbox("Select all", value=False, key=title+'_checkbox')

        selected_options = []

        for option in options_list:
            # Options can only be selected if select all is unchecked
            if not select_all:
                if st.checkbox(option, value=False, key=f'{title}_{option}'):
                    selected_options.append(option)

        if select_all:
            selected_options = options_list

    return selected_options

def selectbox(title,pollutant):
    selected = st.selectbox(title,pollutant,key=title+'_Selected')
    return selected

def hourly(pollutants):
    
    # Removing -200 value will be done for every similar function
    # As not entire is empty
    temp_df=df[(df[pollutants]>-200).all(axis=1)]
    temp_df['Hour'] = temp_df['Time'].apply(lambda x: x.hour) # extracting Hour value

    # Hourly pollution trends
    hourly_pollution = temp_df.groupby('Hour')[pollutants].mean()
    st.line_chart(hourly_pollution, x_label='Hour', y_label='Pollutant Concentration')

def daily(pollutants):

    # bye bye -200 values
    temp_df=df[(df[pollutants]>-200).all(axis=1)]
    temp_df['Date']=pd.to_datetime(temp_df['Date'])
    
    temp_df['Day'] = temp_df['Date'].dt.day_name() # Creating a new column for Name of the Day
    
    # Daily Poollution Trend
    daily_pollution = temp_df.groupby('Day')[pollutants].mean()

    # rearraging the index into proper order
    daily_pollution = daily_pollution.reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
    fig = px.line(
        daily_pollution,
        labels={'value':'Pollutant Concentration','variable':'Pollutants'}
    )
    st.plotly_chart(fig)

def monthly(pollutants):
    
    # -200 values whoosh..
    temp_df=df[(df[pollutants]>-200).all(axis=1)]
    temp_df['Date']=pd.to_datetime(temp_df['Date'])
    
    temp_df['Month'] = temp_df['Date'].dt.month_name() # Extracting months from the given data
    
    # Daily Poollution Trend
    monthly_pollution = temp_df.groupby('Month')[pollutants].mean()
    monthly_pollution = monthly_pollution.reindex(['March','April','May'])
    fig = px.line(
        monthly_pollution,
        labels={'value':'Pollutant Concentration','variable':'Pollutants'}
    )
    st.plotly_chart(fig)

def bar(pollutants):
    
    # If all -200 values are gone totally, we may miss some values, That's the thought
    temp_df=df[(df[pollutants]>-200).all(axis=1)]

    # Assigning day type depending no the date
    temp_df['Day Type']=pd.to_datetime(temp_df['Date']).dt.dayofweek.apply(lambda x:"Weekend" if x>4 else "Weekday")

    # bar chart for Pollution on Weekdays and Weekends
    fig = px.bar(
        temp_df.groupby("Day Type")[pollutants].mean(),
        title="Pollution on Weekdays and Weekends",
        labels={'value':'Pollutant Concentration','variable':'Pollutants'},
        barmode='group'
    )
    st.plotly_chart(fig)

def avg_bar(pollutants):
    
    # Don't know if it will change if we remove everything at once
    temp_df=df[(df[pollutants]>-200).all(axis=1)]
    fig = px.bar(
        temp_df[pollutants].mean(),
        title="Pollution on Weekdays and Weekends",
        labels={'value':'Average Pollutant Concentration','index':'Pollutants'},
        barmode='group'
    )
    st.plotly_chart(fig)

def histogram(pollutant):
    
    temp_df = df[df[pollutant]>-200]
    fig = px.histogram(
        temp_df[pollutant],
        title=f'Histogram for {pollutant}',
        labels={'count':'Frequency','value':f'{pollutant}'}
    )
    st.plotly_chart(fig)