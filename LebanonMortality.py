import pandas as pd
import plotly.express as px
import streamlit as st

lebanon_mortality_2 = 'https://raw.githubusercontent.com/KinanMorad/MortalityInLebanon/main/lebanon_mortality_2.csv'
df = pd.read_csv(lebanon_mortality_2)

st.title("Lebanon Mortality Over Years")

# Selection for plot type
plot_type = st.selectbox('Select a Plot Type', ['Bar', 'Scatter', 'Pie', 'Histogram', 'Area', 'Line'])

# Year Range Slider
year_range = st.slider('Select a Year Range', int(df['Year'].min()), int(df['Year'].max()), (int(df['Year'].min()), int(df['Year'].max())))

# Deaths Range Slider
deaths_range = st.slider('Select a Death Range', int(df['Deaths'].min()), int(df['Deaths'].max()), (int(df['Deaths'].min()), int(df['Deaths'].max())))

# Drop-Down List for year
selected_year_dropdown = st.selectbox('Select a Year (Drop-down)', [None] + sorted(df['Year'].unique()))


# Description
st.write("This app provides an interactive visualization of mortality data in Lebanon over various years. You can select different visualization types and filter the data according to your interests.")

st.write("""
### Description
This interactive dashboard visualizes the mortality data in Lebanon across various years. It showcases the annual death count, allowing users to identify trends, anomalies, or significant events that might have influenced mortality rates. 

Users can select a year or range of years using multiple methods such as drop-downs, radio buttons, or input fields. There's also a feature to filter the data based on a specific range of death counts, enabling focused analysis on years with particular mortality rates.

Choose your visualization type and apply filters to dive deep into the data.
""")




# Filter data based on selected year and deaths range
if selected_year_dropdown:
    df_filtered = df[(df['Year'] == selected_year_dropdown) & (df['Deaths'] >= deaths_range[0]) & (df['Deaths'] <= deaths_range[1])]
else:
    df_filtered = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1]) & (df['Deaths'] >= deaths_range[0]) & (df['Deaths'] <= deaths_range[1])]

# Visualization
if plot_type == 'Bar':
    st.header('Bar Plot')
    fig = px.bar(df_filtered, x='Year', y='Deaths', title='Lebanon Mortality')
    st.plotly_chart(fig)
elif plot_type == 'Scatter':
    st.header('Scatter Plot')
    fig = px.scatter(df_filtered, x='Year', y='Deaths', title='Lebanon Mortality')
    st.plotly_chart(fig)
elif plot_type == 'Pie':
    st.header('Pie Chart')
    fig = px.pie(df_filtered, names='Year', values='Deaths', title='Lebanon Mortality')
    st.plotly_chart(fig)
elif plot_type == 'Histogram':
    st.header('Histogram')
    fig = px.histogram(df_filtered, x='Deaths', title='Distribution of Deaths in Lebanon')
    st.plotly_chart(fig)
elif plot_type == 'Area':
    st.header('Area Chart')
    fig = px.area(df_filtered, x='Year', y='Deaths', title='Lebanon Mortality Over Time (Area Chart)')
    st.plotly_chart(fig)
elif plot_type == 'Line':
    st.header('Line Chart')
    fig = px.line(df_filtered, x='Year', y='Deaths', title='Lebanon Mortality Over Time (Line Chart)')
    st.plotly_chart(fig)
