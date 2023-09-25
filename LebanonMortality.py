import pandas as pd
import plotly.express as px
import streamlit as st

lebanon_mortality_2 = "lebanon_mortality_2.csv"
df = pd.read_csv(lebanon_mortality_2)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
st.title("Lebanon Mortality Over Years")

# Adding a select box to choose the plot type
plot_type = st.selectbox('Select a Plot Type', ['Bar', 'Scatter', 'Pie', 'Histogram', 'Area'])

# Adding a slider to filter the year
year_range = st.slider('Select a Year Range', int(df['Year'].min()), int(df['Year'].max()), (int(df['Year'].min()), int(df['Year'].max())))

# Filtering the DataFrame based on the selected year range
df_filtered = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]

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
