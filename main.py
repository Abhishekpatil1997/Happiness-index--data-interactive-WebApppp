import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('data/happy.csv')
columns = df.columns.to_list()
st.title('In Search for Happiness:')

x_variable = st.selectbox("Select the data for the X-axis:", columns)

y_variable = st.selectbox("Select the data for the Y-axis:",columns)

x_title = x_variable.replace("_"," ").title()
y_title = y_variable.replace("_"," ").title()
st.title(f"{x_title} & {y_title}:")

figure = px.scatter(df,x=df[x_variable], y=df[y_variable], labels={"x": x_title, "y":y_title})
st.plotly_chart(figure)



