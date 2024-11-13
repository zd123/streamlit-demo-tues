import streamlit as st
import pandas as pd

st.markdown("# Hello World")

df = pd.read_csv('data/titanic.csv')
st.dataframe(df)

st.bar_chart(df['age'])


button_response = st.button("Click me")

if button_response:
    st.write('YOU CLICKED ME')
