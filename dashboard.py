import streamlit as st
st.write("# COVID-19 data")

import pandas as pd
data = pd.read_csv("Covid Data.csv")
data.head()

import matplotlib.pyplot as plt
st.dataframe(data.head())

import seaborn as sns
plt.style.use("dark_background")
col1, col2 = st.columns(2)
col1.write('## Correlation')
with col1:
    fig, ax = plt.subplots()
    sns.heatmap(data.corr())
    st.pyplot(fig)

col2.write('Many factors are at play when looking at COVID-19 outcomes. Age has been identified as a significant risk factor,\
            with older adults more likely to require hospitalization and experience more severe illness. Similarly, underlying health \
            conditions such as diabetes, obesity, and cardiovascular disease have been associated with worse outcomes. Other factors, s \
            uch as sex and pregnancy, may also play a role in disease severity and require special consideration in clinical management.  \
            The presence of pneumonia, intubation, and ICU admission are all markers of more severe disease and can indicate a higher risk of mortality.')

col1, col2 = st.columns(2)

col1.write('Older people are more likely to end up in ICU because of COVID-19 due to their weakened immune systems and higher likelihood \
           of having pre-existing health conditions. As people age, their immune systems become less efficient in fighting off infections, \
           making them more vulnerable to severe illness from COVID-19. Additionally, older adults are more likely to have underlying health \
           conditions such as cardiovascular disease, diabetes, and chronic respiratory diseases that can make COVID-19 more severe. \
           These factors increase the likelihood of hospitalization and ICU admission for older adults with COVID-19.')

col2.write('## Correlation')
with col2:
    fig, ax = plt.subplots()
    sns.histplot(data=data, x="AGE", color="skyblue", label="ICU", kde=True)
    sns.histplot(data=data, x="AGE", color="red", label="ICU", kde=True)

    plt.legend() 
    plt.show()
    st.pyplot(fig)
