import pandas as pd

df = pd.read_csv('data/CleanedAirQuality.csv')


sensor_cols = ['PT08.S1(CO)', 'PT08.S3(NOx)',  'PT08.S4(NO2)', 'PT08.S2(NMHC)']
pollutant_cols = ['CO(GT)', 'NOx(GT)', 'NO2(GT)', 'NMHC(GT)']
weather_cols = ['T', 'RH', 'AH']