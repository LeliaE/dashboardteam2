"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
import numpy as np


data = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

""" location = data[location]
date = data[date]
total_death = data[total_death]
"""
data 
"""print("Shape of cdata:", data.shape)"""



""" st.line_chart(data, x = date, y = total_death )"""