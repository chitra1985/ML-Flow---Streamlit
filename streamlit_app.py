import streamlit as st
import pandas as pd

st.title('This is Machine Learning App')

st.write('This app is Machine Learning app to predict stock price')

with st.expander('Dataset'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://github.com/chitra1985/ML-Flow---Streamlit/blob/master/FAANG%20.csv')
