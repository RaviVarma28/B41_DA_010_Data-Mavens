import streamlit as st



pg = st.navigation([
    st.Page('pages/main.py', title='Home', icon=":material/home:"),
    st.Page("pages/Insights.py", title="Insights", icon=":material/stacked_bar_chart:"),
    st.Page('pages/Visualizations.py', title="Visualization", icon=":material/data_exploration:"),
    st.Page('pages/Conclusion.py', title='Conclusion', icon=':material/check:'),
    st.Page('pages/About.py', title='About', icon=':material/quiz:')
])
st.sidebar.image('static/Logo.jpg')
pg.run()