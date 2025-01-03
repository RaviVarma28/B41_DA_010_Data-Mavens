import streamlit as st

st.set_page_config(layout="wide")

pg = st.navigation([
    st.Page('pages/main.py', title='Home', icon=":material/home:"),
    st.Page("pages/Insights.py", title="Insights", icon=":material/stacked_bar_chart:"),
    st.Page('pages/Visualizations.py', title="Visualization", icon=":material/data_exploration:"),
    st.Page('pages/Conclusion.py', title='Conclusion', icon=':material/check:'),
    st.Page('pages/About.py', title='About', icon=':material/quiz:')
])

pg.run()
st.sidebar.image("static/Logo.png")
