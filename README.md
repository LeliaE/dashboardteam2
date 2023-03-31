# DASHBOARDTEAM2 : Open Source Project
Team Members:
Lelia Erscoi, Irina Delamare and Sakshi Sharma

###Project Description:
The 3 of us are team 2 and we are working on creatting an interactive dashboard of covid cases.

### Data
The COVID-19 dataset comes from the Our World in Data team from Johns Hopkins University. The data can be found at https://github.com/owid/covid-19-data/tree/master/public/data.

###Overview:
First, you will need to **Install dependencies you need for your project:**
We are using Streamlit, a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. 

You need to install the required dependencies in a dedicated Python virtual environment on your machine. For that, nothing more simple, just follow the instruction bellow.
To understand a bit what we are doing, we are using the file requirements.txt to store all the dependencies we wish our environment runs on. This is done to ensure that you will be able to run our dashboard even if we stop updating it.

So, you just need to create and enter your virtual environment :
- Open a terminal and go to the directory of your project repository.
- Inside your project repository, create a virtual environment with the Python venv module:
``` python -m venv env ```
- Now activate your virtual environment:
```source env/bin/activate```
(the command is different on Windows)
- Install dependencies in your virtual environment (activated) with the command:
```python -m pip install -r requirements.txt```




# CHECKLIST

Here you will find the interactive checklist of all the stuff we implemented:

### Metadata
- [x] The README.md file is present at the root of the GitHub repo and is in Markdown format.
- [ ] The README.md file states where the data come from (with a link to the original repo).
- [ ] The README.md file contains guidelines to explicitly install all required dependencies for the project in a virtual environment.
- [ ] The README.md file contains instructions on how to run the dashboard locally.
- [ ] The README.md file contains a link to Streamlit Cloud.
- [ ] The README.md file contains a Software Heritage button with an active link
- [ ] The LICENSE (or LICENSE.txt) file contains a valid open-source license.
- [ ] The requirements.txt (for pip) or environment.yml (for conda) file to install all required dependencies.
- [ ] The AUTHORS file contains the list of authors.
- [ ] The codemeta.json file is present and filled properly.

### Organization
- [ ] Issues are created to list expected features and report bugs.
- [ ] Issues are discussed.
- [ ] Commits address implementation of one feature or fix of one bug at a time.
- [ ] Commits are (roughly) evenly distributed among project participants.
- [ ] New features are implemented in branches and merged through pull requests.

### Data
- [x] Data file is not stored in the repo and is read on the fly with Pandas.
- [x] A caching mechanism is implemented to prevent downloading the file each time the user interacts with the dashboard.

### Visualization
- [ ] Dashboard displays graphics of Covid-19 cases or deaths vs time for several countries.
- [ ] Data are normalized with respect to the number of inhabitants per country.
- [ ] Raw number, cumulative number and the (rolling) average number of cases or deaths could be displayed.
- [ ] The graph has proper axis names with “Date” for the x-axis and a name updated live for the y-axis (for instance “raw cases per million”, “average deaths per million”...) 
- [ ] Peak (wave) detection is implemented for cumulative number of cases or deaths.

### Interaction
- [ ] User can select which countries to display in the same graphic (among a predefined list of countries).
- [ ] User can select to display Covid-19 cases or deaths.
- [ ] User can select to display the raw number, cumulative number or the 7-day rolling average.
- [ ] User can select the time frame to display. Either with a double slider or with 2 date pickers.
- [ ] User can select to display or not the peak detection (for cumulative numbers only).
