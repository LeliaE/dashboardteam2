import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import altair as alt
import wordcloud
from wordcloud import WordCloud

st.set_option('deprecation.showPyplotGlobalUse', False)

# Title
st.title("COVID-19 Data")

# Style
plt.style.use("dark_background")

# Getting data
@st.cache_data  
def get_data():
    url = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"
    data = pd.read_csv(url)
    return data

data = get_data()
st.dataframe(data)
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

with col2:
    st.write(f'Locations:')
    wordcloud = WordCloud().generate(' '.join(data.location.unique()))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot()


dependent_var = ['total_deaths', 'total_deaths_per_million', 'total_cases_per_million', \
                 'icu_patients_per_million','people_vaccinated_per_hundred',  \
                'total_vaccinations','hosp_patients_per_million']

independent_var = ['gdp_per_capita','population','stringency_index','population', 
                    'population_density', 'median_age', 'aged_65_older',
                    'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
                    'cardiovasc_death_rate', 'diabetes_prevalence', 
                    'female_smokers','male_smokers', 'handwashing_facilities', 
                    'hospital_beds_per_thousand','life_expectancy','continent', 'location']

# Creating selectbox for x, y and color label and setting default value
#x_column = st.sidebar.selectbox('Select X axis', independent_var)
#y_column = st.sidebar.selectbox('Select Y axis', dependent_var)

#Create the scatterplot using altair
#scatterplot = alt.Chart(data).mark_circle().encode(
#    x=x_column,
#    y=y_column
#).interactive()

# Display the scatterplot
#st.altair_chart(scatterplot, use_container_width=True)


################# Data by country ##############################

st.subheader("Data by Country", anchor=None)
# Create a sidebar with a list of countries and a radio button to choose between new cases and new deaths
countries = sorted(data['location'].unique())
selected_countries = st.sidebar.multiselect('Select countries:', countries, default=['United States', 'India'])
new_cases_or_deaths = st.sidebar.radio('Choose between new cases or new deaths:', ['new_cases', 'new_deaths'])

# Filter the data for the selected country and the chosen variable
country_data = data[data['location'].isin(selected_countries)][['location', 'date', new_cases_or_deaths]].dropna()

# Create the chart
chart = alt.Chart(country_data).mark_line().encode(
    x='date:T',
    y=alt.Y(f'{new_cases_or_deaths}:Q', title='New Cases' if new_cases_or_deaths == 'new_cases' else 'New Deaths'),
    color='location:N'
).properties(
    width=800,
    height=400,
    title=f'Daily {new_cases_or_deaths.capitalize()} for {", ".join(selected_countries)}'
)

# Display the chart
st.altair_chart(chart, use_container_width=True)



# Correlation
col1, col2 = st.columns(2)
col1.write('## Correlation')
with col1:
    fig, ax = plt.subplots()
    sns.heatmap(data.corr())
    st.pyplot(fig)

col2.write('                                                                                                                         \
            Many factors are at play when looking at COVID-19 outcomes. Age has been identified as a significant risk factor,\
            with older adults more likely to require hospitalization and experience more severe illness. Similarly, underlying health \
            conditions such as diabetes, obesity, and cardiovascular disease have been associated with worse outcomes. Other factors,  \
            such as sex and pregnancy, may also play a role in disease severity and require special consideration in clinical management.  \
            The presence of pneumonia, intubation, and ICU admission are all markers of more severe disease and can indicate a higher risk of mortality.')


