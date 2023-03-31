# DASHBOARDTEAM2 : Open Source Project
Team Members:
Lelia Erscoi, Irina Delamare and Sakshi Sharma

###Project Description:
The 3 of us form team 2 and we are working on creatting an interactive dashboard of covid19 casualties using streamlit for our OpenSource course.

You can check our dashboard with this [link](https://leliae-dashboardteam2-dashboard-6cmp3i.streamlit.app/).

*WE NEED A SUMMARY*


# Data
The COVID-19 dataset comes from the Our World in Data team from Johns Hopkins University. The data can be found at [owid/covid-19-data](https://github.com/owid/covid-19-data/tree/master/public/data).

###Overview:
# Run dashboard localy
:exclamation: If you havent installed the dependency, go to (add link via summary)

In the terminal, navigate to the project. Here, the project is stored in the folder Documents, inside the folder git. 
```bash
USER:~$ cd Documents/git/dashboardteam2/
```
Then, you need to activate your virtual environment:
```bash
USER:~/Documents/git/dashboardteam2$ source env/bin/activate
```
Then run the dashboard
```bash
USER:~/Documents/git/dashboardteam2$ streamlit run dashboard.py
```
In case of issues, you might need to reinstall dependencies in your virtual environment with the command:
```python -m pip install -r requirements.txt``` 

# Install Dependencies
First, you will need to **Install dependencies you need for your project:**
We are using Streamlit, a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps. 

You need to install the required dependencies in a dedicated Python virtual environment on your machine. For that, nothing more simple, just follow the instruction bellow.
To understand a bit what we are doing, we are using the file requirements.txt to store all the dependencies we wish our environment runs on. This is done to ensure that you will be able to run our dashboard even if we stop updating it.

So, you just need to create and enter your virtual environment :
## FOR LINUX AND MACos USERS
- Open a terminal and go to the directory of your project repository.
- Inside your project repository, create a virtual environment with the Python venv module:
``` python -m venv env ```
- Now activate your virtual environment:
```source env/bin/activate```
(the command is different on Windows)
- Install dependencies in your virtual environment (activated) with the command:
```python -m pip install -r requirements.txt```

## FOR WINDOWS USERS
*to add* 





# CHECKLIST

Here you will find the interactive checklist of all the stuff we implemented:

### Metadata
- [x] The README.md file is present at the root of the GitHub repo and is in Markdown format.
- [x] The README.md file states where the data come from (with a link to the original repo).
- [ ] The README.md file contains guidelines to explicitly install all required dependencies for the project in a virtual environment.
- [x] The README.md file contains instructions on how to run the dashboard locally.
- [x] The README.md file contains a link to Streamlit Cloud.
- [ ] The README.md file contains a Software Heritage button with an active link
- [x] The LICENSE (or LICENSE.txt) file contains a valid open-source license.
- [x] The requirements.txt (for pip) file to install all required dependencies.
- [x] The AUTHORS file contains the list of authors.
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
