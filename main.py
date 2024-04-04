import streamlit as st
import numpy as np
import pandas as pd
import csv

st.title('Pokemon Data Vizualization Tool')
st.divider()

# Load the data
@st.cache
def load_data():
    data = pd.read_csv('pokemon.csv')
    return data

data = load_data()

# create a data frame with the pokemon data
df = pd.DataFrame(data)

# display the data
st.write(df)
