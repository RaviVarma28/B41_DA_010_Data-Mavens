# AIR QUALITY INDEX (AQI) 📊

<img src="https://github.com/user-attachments/assets/68a1759a-6a62-4d36-943b-57dc4b213039" width="500"/>

## **About**
The **Air Quality Index (AQI) Dashboard** is an innovative project designed to provide real-time monitoring and analysis of air quality in various regions. By leveraging environmental data, the dashboard enables users to track key pollutants like PM2.5, PM10, NO2, SO2, CO, and O3. Its intuitive design, powered by **Python, Streamlit**, and cutting-edge **data visualization tools**, transforms complex datasets into actionable insights.

Whether you're an individual concerned about health risks or a policymaker looking for environmental insights, this project equips you with the tools to make informed decisions. With a focus on simplicity and accessibility, the **AQI Dashboard** bridges the gap between raw data and meaningful environmental awareness.

## 🎯**Aim**
The aim of this project is to develop an interactive and user-friendly **Air Quality Index (AQI) Dashboard** that provides real-time insights into air quality metrics. By leveraging Python and Streamlit, the project seeks to analyze and visualize air quality data, empowering users to track pollution levels, understand trends, and assess their impact on health. This initiative promotes awareness and informed decision-making for healthier living and sustainable communities.

## 📋**Objectives of the Project:**
**1**. **Understanding AQI Metrics:**

- Learn about key pollutants (e.g., PM2.5, PM10, NO2, SO2, CO, O3) and their permissible levels.
- Understand how AQI is categorized into health impact levels.

**2**. **Data Collection and Preprocessing:**

- Work with real-time or historical air quality datasets from sources like government APIs or publicly available datasets.
- Clean and preprocess data to handle missing values, inconsistencies, and outliers.


**3**. **Visualization:**

- Use libraries like **Matplotlib and Seaborn**, to create graphs that depict trends in air quality over time.
- To Experience a sleek, modern dashboard that transforms complex air quality data into actionable insights, helping you make informed decisions for a healthier lifestyle.

**4**. **Insights and Analysis:**

- Analyze trends in air quality, identifying patterns, seasonal variations, and hotspots for pollution.
- Explore **correlations between pollutants and air quality.**

## 🛠**Tools and Libraries Used:**
**1. Data Handling**: Pandas, NumPy

**2. Visualization**: Matplotlib, Seaborn

**3. Web App Framework**: Streamlit (for creating interactive and real-time dashboards)

## 💻**Project Type** 
Data Analysis using Python Libraries

## 🌐**Deployed App**
**AIR QUALITY INDEX(AQI)**: (LINK)

## **Directory Structure**📁➡️📄
**AIR QUALITY INDEX DASHBOARD**📊
- ├─ assets/
- │ ├─ ├─ EV Maker by Place.csv/
- │ ├─ datasets/
- │ ├─ ├─ ev_cat_01-24.csv/
- │ ├─ ├─ ev_sales_by_makers_and_cat_15-24.csv/
- │ ├─ ├─ OperationalPC.csv/
- │ ├─ ├─ Vehicle Class - All.csv/
- ├─ images/
- │ ├─ analysis.ico/
- │ ├─ Indian EV Market Logo.svg/
- ├─ preprocessor.py/
- ├─ charts.py/
- ├─ main.py/
- ├─ Indian_States.geojson/
- ├─ requirements.txt/
- ├─ README.md/

## **Walkthrough of the project**▶️
Understand the project in Short: (LINK)

## **Data Scrapping**💾🧹
**1. Data Cleaning:**
This code cleans and preprocesses air quality data by removing unnecessary columns, converting specific columns to appropriate numeric formats, handling missing values, and ensuring correct date and time formats. The cleaned data is then saved to a new CSV file, CleanedAirQuality.csv.

![DATA CLEANING](https://github.com/user-attachments/assets/5c635e55-5cc0-444b-bdc8-128da8ea52fe)


**2. Visualization of all Polutants:**
This code visualizes the distribution of four specified pollutants (CO(GT), NMHC(GT), NOx(GT), and NO2(GT)) by plotting histograms for each, filtered to exclude values below -200(*to remove the outliers*). The *Histograms* are displayed in a 2x2 grid with labeled axes and titles for each pollutant.

![Visualization of all pollutants (code)](https://github.com/user-attachments/assets/ce16a01e-ef24-41fb-8486-fa211d1b6a56)


**3. Hourly , Daily & Monthly Trends of Peak Pollution Periods:**
This code processes air quality data by extracting and calculating daily, hourly, and monthly pollution trends for multiple pollutants, while also computing the average pollution levels. It then visualizes these trends using line and bar plots in a 2x2 grid to showcase the patterns of pollution over time.

![H,D,Y Trends (code)](https://github.com/user-attachments/assets/57f2814d-737e-4e1e-9421-8012fc7335ce)

## **Data Visualization**📈
<img src="https://github.com/user-attachments/assets/369f157f-754f-42d4-b6e0-a6151439b5b0" width="603"/>

<img src="https://github.com/user-attachments/assets/791467c3-d8f8-415c-a098-bf300dbe948f" width="603"/>

<img src="https://github.com/user-attachments/assets/552349c7-7d44-4324-89ca-d7669ad1140d" width="603"/>

<img src="https://github.com/user-attachments/assets/b8722f14-92d4-4fa3-b1b4-a567c08e1ff0" width="603"/>

## **Why This Dashboard Stands Out 🌟**
**1) Real-Time Monitoring:** Stay updated with the latest air quality data from your region or anywhere in the world.

**2) Interactive Visualizations:** Dynamic graphs and charts help you uncover trends and patterns effortlessly.

**3) Health Insights:** Understand what AQI levels mean for your health and take informed actions.

**4) Customizable Views:** Filter data by pollutant type, time frame, or location for a tailored experience.

## **Challenges Faced**❗⚠️
**1) Data Cleaning and Preprocessing:**
Raw air quality data frequently contained errors like missing values, outliers, or incorrect readings due to sensor malfunctions. Cleaning and preprocessing the data, such as handling missing values, removing unnecessary columns, and converting timestamps to a consistent format, required careful attention to ensure data accuracy and reliability.

**2) User Interface and Experience:**
Creating an intuitive and responsive dashboard using Streamlit posed challenges, especially in terms of user interaction. Ensuring that the users could easily explore real-time AQI data, filter by location or time, and understand complex pollution metrics required designing an engaging yet simple user interface.

**3) Data Inconsistencies Across Sources:**
Different sources for air quality data may report different pollutants, use varying units of measurement, or have different methods of calculation. For instance, one source might report PM2.5 levels in micrograms per cubic meter (µg/m³), while another might use parts per million (ppm). Normalizing data to a common format across multiple data sources was necessary for consistent AQI calculation.

**4) Ensuring Scalability:**
As the project grew and more regions were added, the system had to scale efficiently to handle large volumes of real-time data. Ensuring that the infrastructure could handle increasing amounts of data without degradation in performance was a challenge. This required optimizing database queries, managing memory usage, and utilizing cloud services for scaling when necessary.

**5) Interactivity and User Engagement:**
Providing interactive elements such as filters, search options, or time-series analysis tools was essential for the usability of the dashboard. Ensuring that these interactive features worked smoothly with real-time data and did not affect performance (especially in terms of data processing or network latency) was an ongoing challenge.

These challenges were mitigated through careful data management, using Python’s robust libraries for data processing and visualization, and by designing the dashboard to be flexible and responsive to real-time data changes. Each of these challenges required creative solutions, robust error handling, and continuous optimization to ensure the AQI dashboard functioned efficiently and provided accurate, real-time insights.

## **Conclusion**✅🔚

The **Air Quality Index (AQI) Dashboard project** successfully addressed several challenges related to *data collection, processing, and visualization*. By integrating data from multiple sources and cleaning it for accuracy, the project provided users with a reliable tool for monitoring air quality in real time. The visualization of pollution trends across different time frames (hourly, daily, and monthly) helped reveal important patterns and insights into air quality levels, empowering users to make informed decisions about their health and environment.

Despite challenges such as data inconsistencies, missing values, and real-time synchronization, the project highlighted the importance of accurate data handling and intuitive visualization in environmental science. Through careful design, data processing techniques, and the use of Python libraries like Pandas, Matplotlib, and Streamlit, the dashboard was able to provide clear, actionable insights into air quality trends. Moving forward, the project can be expanded by adding more real-time data sources, improving the dashboard’s scalability, and integrating predictive models for more advanced air quality forecasting.

This project not only enhances your Python programming and data science skills but also contributes to raising awareness about environmental sustainability. This project is perfect for anyone passionate about using technology to drive environmental awareness and create healthier communities. 🌍✨

## **Team Members**👤🤝👥
[@RaviVarma28] 

Handling the development of the interactive user interface using *Streamlit*, ensuring the *dashboard* was responsive and *user-friendly* across devices.

[@neetukm]

Performed the *Exploratory Data Analyis* for the *AQI project*. Analyzing and understanding the underlying structure of the *Air Quality Data*.

[@PrinceSrivastava182]

Handling *Data Cleaning and Data Preprocessing* , and Created *visualizations charts* to display pollution trends, working with libraries like *Matplotlib and Seaborn*.