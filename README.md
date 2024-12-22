# AIR QUALITY INDEX (AQI) 📊

<img src="https://github.com/user-attachments/assets/68a1759a-6a62-4d36-943b-57dc4b213039" width="500"/>

## 🎯**Aim**
 The goal is to learn data handling, visualization, and dashboard development using Python.

The aim of this project is to develop an interactive and user-friendly Dashboard that provides insights into air quality metrics. By leveraging Python and Streamlit, the project provides tools to analyze pollutant concentrations and sensor data collected over a year in an Italian city.
  
The goal is to analyze and visualize air quality data, empowering users to track pollution levels, understand trends, and assess their impact on health. This initiative promotes awareness and informed decision-making for healthier living and sustainable communities.

## 📋**Objectives of the Project:**
**1**. **Understanding AQI Metrics:**

- Explore relationships between sensor responses and pollutant concentrations.
- Create an interactive, user-friendly interface for data visualization.

**2**. **Data Collection and Preprocessing:**

- Work with historical air quality datasets from sources like government APIs or publicly available datasets.
- Clean and preprocess data to handle missing values, inconsistencies, and outliers.


**3**. **Visualization:**

- Use libraries like **Matplotlib and plotly**, to create graphs that depict trends in air quality over time.
- To Experience a sleek, modern dashboard that transforms complex air quality data into actionable insights, helping you make informed decisions for a healthier lifestyle.

**4**. **Insights and Analysis:**

- Analyze trends in air quality, identifying patterns, seasonal variations, and hotspots for pollution.
- Explore **correlations between pollutants and air quality.**


## 🛠**Tools and Dataset Used:**
**1.Dataset Used**: [Air Quality Dataset](https://www.kaggle.com/datasets/fedesoriano/air-quality-data-set)

**2. Data Handling**: Pandas, NumPy

**3. Visualization**: Matplotlib, Seaborn , Plotly

**4. Web App Framework**: Streamlit (for creating interactive and real-time dashboards)

## 💻**Project Type** 
Data Analysis using Python Libraries

## 🌐**Deployed App**
**AIR QUALITY INDEX(AQI)**: [AQI Dashboard](https://b41-da-010-data-mavens.streamlit.app)

## **Directory Structure**📁➡️📄
**AIR QUALITY INDEX DASHBOARD**📊  

├─ data/  
│   ├─ AirQuality.csv  
│   ├─ CleanedAirQuality.csv  
├─ notebook/  
│   ├─ Data_Visualization.ipynb  
│   ├─ Data_Cleaning.ipynb  
│   ├─ EDA_Correlations.ipynb  
│   ├─ EDA.ipynb  
│   ├─ Insights_and_Recommendations.ipynb  
├─ pages/  
│   ├─ About.py  
│   ├─ Conclusion.py  
│   ├─ Insights.py  
│   ├─ Visualizations.py  
│   ├─ main.py  
├─ scripts/  
│   ├─ .gitignore  
│   ├─ Preprocessor.py  
├─ static/  
│   ├─ Logo.jpg  
├─ .gitignore  
├─ README.md  
├─ app.py  
├─ requirements.txt 
  
## **Walkthrough of the project**▶️
Understand the project in Short: (LINK)


## **Data Analysis**📑💻

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
**1) Interactive Visualizations:** Dynamic graphs and charts help you uncover trends and patterns effortlessly.

**2) Health Insights:** Understand what AQI levels mean for your health and take informed actions.

**3) Customizable Views:** Filter data by pollutant type, time frame, or location for a tailored experience.

## **Challenges Faced**❗⚠️
**1) Data Cleaning and Preprocessing:**
Raw air quality data frequently contained errors like missing values, outliers, or incorrect readings due to sensor malfunctions. Cleaning and preprocessing the data, such as handling missing values, removing unnecessary columns, and converting timestamps to a consistent format, required careful attention to ensure data accuracy and reliability.

**2) User Interface and Experience:**
Creating an intuitive and responsive dashboard using Streamlit posed challenges, especially in terms of user interaction. Ensuring that the users could easily explore AQI data, filter by location or time, and understand complex pollution metrics required designing an engaging yet simple user interface.

**3) Data Inconsistencies Across Sources:**
Different sources for air quality data may report different pollutants, use varying units of measurement, or have different methods of calculation. For instance, one source might report NOx levels in micrograms per cubic meter (µg/m³), while another might use parts per million (ppm). Normalizing data to a common format across multiple data sources was necessary for consistent AQI calculation.

**4) Interactivity and User Engagement:**
Providing interactive elements such as filters, search options, or time-series analysis tools was essential for the usability of the dashboard. Ensuring that these interactive features worked smoothly with the data and did not affect performance was a challenge.

These challenges were mitigated through careful data management, using Python’s robust libraries for data processing and visualization, and by designing the dashboard to be flexible and responsive to real-time filtering. Each of these challenges required creative solutions, robust error handling, and continuous optimization to ensure the AQI dashboard functioned efficiently.

## **Conclusion**✅🔚

The Air Quality Monitoring and Analysis project successfully showcased the use of Python and Streamlit for building an intuitive dashboard. Key achievements include:

- Developing insights into pollutant trends and sensor responses through interactive visualizations.
- Tackling real-world challenges like missing data by removing erroneous entries entirely.
- Gaining valuable experience in preprocessing, data analysis, and web app development.  
While this project is a learning exercise with no future development planned, it demonstrates the potential of data visualization tools for environmental analysis and awareness. 🌍✨

## **Team Members**👤🤝👥
**[ Ravi Kiran Venkata Sai Varma Gedela](https://github.com/RaviVarma28)** 

Handling the development of the interactive user interface using *Streamlit*, ensuring the *dashboard* was responsive and *user-friendly* across devices.

**[Neetu Kumari](https://github.com/neetukm)**

Performed the *Exploratory Data Analyis* for the *AQI project*. Analyzing and understanding the underlying structure of the *Air Quality Data*.

**[Prince Srivastava](https://github.com/PrinceSrivastava182)**

Handling *Data Cleaning and Data Preprocessing* , and Created *visualizations charts* to display pollution trends, working with libraries like *Matplotlib and Seaborn*.
