import streamlit as st
st.write("COVID-19 data")

import pandas as pd
data = pd.read_csv("Covid Data.csv")
data.head()

import matplotlib.pyplot as plt
st.dataframe(data.head())


col1, col2 = st.columns(2)
col1.write('# Correlation')
with col1:
    fig, ax = plt.subplots()
    plt.plot(data.corr())
    st.pyplot(fig)



plt.show()