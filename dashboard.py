# Importing dependencies
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import altair as alt
import wordcloud
from wordcloud import WordCloud
import numpy as np
from scipy.signal import find_peaks
from scipy import signal

# Title
st.title("COVID-19 Data dashboard")

# Style
plt.style.use("dark_background")
st.set_option('deprecation.showPyplotGlobalUse', False)

# Getting data
@st.cache_data  
def get_data():

    # URL from where we get the data
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"

    # Load data
    data = pd.read_csv(url)
    data["date"] = pd.to_datetime(data["date"])
    
    #st.dataframe(data)

    return data

# Getting countries list
@st.cache_data
def get_countries(data):
    
    # Create countries list
    countries = list(sorted(data['location'].unique()))

    # Removing errors from countries list
    notCountries = ['High income', 'Low income', 'Lower middle income', 
                    'Upper middle income', 'World', 'Africa', 'Asia', 'Europe', 
                    'European Union', 'North America', 'Oceania', 'South Africa', 'South America']
    
    for i in notCountries:
        countries.remove(i)

    return countries

# Calling get_data function
data = get_data()
countries = get_countries(data)


st.subheader("A Few General Facts", anchor=None)

# Date info
a = data.date.value_counts().sort_index()
first_day = a.index[0]
last_day = a.index[-1]

col1, col2 = st.columns(2)
with col1:
    st.markdown('**Date**')
    st.write(f'The first recorded date is: {first_day}')
    st.write(f'The last recorded date is: {last_day}')
    st.write(f'Date span: {data.date.min(),data.date.max()}')
    st.markdown('**Locations**')
    st.write(f'Number of locations recorded: {data.location.nunique()}')

#with col2:
#  st.write(f'Locations: how many location has been implemented')


################# Data by country ##############################

st.subheader("Data by Country", anchor=None)
# Create a sidebar with a list of countries and a radio button to choose between new cases and new deaths
#countries = sorted(data['location'].unique())

# Streamlit sidebar
st.sidebar.image('https://institutducerveau-icm.org/wp-content/uploads/2020/10/coronavirus-covid-19-e1603461789898-830x483.jpg', width=300)


visualisation_type = {'Total confirmed cases of COVID-19 per 1,000,000 people': 'total_cases_per_million', 
                    'New confirmed cases of COVID-19 per 1,000,000 people': 'new_cases_per_million', 
                    'New confirmed cases of COVID-19 (7-day smoothed) per 1,000,000 people': 'new_cases_smoothed_per_million', 
                    'Total deaths attributed to COVID-19 per 1,000,000 people': 'total_deaths_per_million', 
                    'New deaths attributed to COVID-19 per 1,000,000 people': 'new_deaths_per_million', 
                    'New deaths attributed to COVID-19 (7-day smoothed) per 1,000,000 people': 'new_deaths_smoothed_per_million'}

# Selecting dashboard type
select_dashboard_type = st.sidebar.radio('Choose What type of visualisation you want for the dashboard :', visualisation_type.keys())   
selected_type = visualisation_type[select_dashboard_type]

###################### DATE ########################################
selected_dates = st.sidebar.date_input('Select dates:', [pd.to_datetime('2020-01-01'), pd.to_datetime('today')])

# Check if only one date was selected
if isinstance(selected_dates, tuple):
    start_date= selected_dates[0]
    try: 
        end_date = selected_dates[1]
    except:
        "Date selection error. Choose 2 dates."
        end_date = start_date
else:
    start_date, end_date = selected_dates, pd.to_datetime('today')


# Convert start_date and end_date to numpy.datetime64[ns]
start_date = np.datetime64(start_date)
end_date = np.datetime64(end_date)
st.write('Selected dates:', start_date, end_date)

###################################################################

# Selecting countries
selected_countries = st.sidebar.multiselect('Select countries:', countries, default=['United States', 'India', 'France'])
#country_data = data[data['location'].isin(selected_countries)]
#country_data = data[(data['location'].isin(selected_countries))][['location', 'date', selected_type]].dropna()

# Selecting countries
country_data = data.loc[(data['location'].isin(selected_countries)) & (data['date'] >= start_date) & (data['date'] <= end_date), ['location', 'date', selected_type]].dropna()



############################ PEAK DETECTION ##########################################################
def detect_peaks(x):

    peaks, peak_properties = signal.find_peaks(x, prominence=-0.5, distance=50)
    return peaks

######################################################################################################


def choose_name(select_type):
    if select_type == 'total_cases_per_million':
        return 'total cases per million'
    elif select_type == 'new_cases_per_million':
        return 'new cases per million'
    elif select_type == 'new_cases_smoothed_per_million':
        return 'new cases smoothed per million'
    elif select_type == 'total_deaths_per_million':
        return 'total deaths per million'
    elif select_type == 'new_deaths_per_million':
        return 'new deaths per million'
    elif select_type == 'new_deaths_smoothed_per_million':
        return 'new deaths smoothed per million'



# Create the chart
chart = alt.Chart(country_data).mark_line().encode(
    x='date:T',
    y=alt.Y( f'{selected_type}:Q', title = choose_name(selected_type)),
    color='location:N'
).properties(
    width=800,
    height=400,
    title=f'Daily {selected_type.capitalize()} for {", ".join(selected_countries)}'
)

# Display the chart
st.altair_chart(chart, use_container_width=True)



####################### PEAK DETECTION BUTTON ##################################################

new_cases = ['new_cases_per_million',
             'new_cases_smoothed_per_million',
             'new_deaths_per_million',
             'new_deaths_smoothed_per_million'

if selected_type in new_cases:
    if st.button('Detect Peaks'):
    # Filter data for first country in selected countries
        country_data_filtered = country_data[country_data['location'] == selected_countries[0]]
        
        # Get peak properties
        peaks = detect_peaks(country_data_filtered[selected_type].values)
        
        # Add peaks to chart
        peaks_chart = alt.Chart(country_data_filtered.iloc[peaks]).mark_circle(size=100, color='red').encode(
            x='date:T',
            y=alt.Y(f'{selected_type}:Q', title='New Cases'),
            tooltip=['location', 'date', selected_type]
        )
        
        # Display chart with peaks
        st.altair_chart(chart + peaks_chart, use_container_width=True)


###############################################################################################


