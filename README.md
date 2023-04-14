# DASHBOARDTEAM2 : Open Source Project

[![SWH](https://archive.softwareheritage.org/badge/swh:1:dir:830bc682c58fc7d5158d6cd0153bcfaad4ef5b4c/)](https://archive.softwareheritage.org/swh:1:dir:830bc682c58fc7d5158d6cd0153bcfaad4ef5b4c;origin=https://github.com/LeliaE/dashboardteam2;visit=swh:1:snp:22e01c878777317a9c17341f1e92cec7de72bb45;anchor=swh:1:rev:90c84fd309cd250d5547a303e9b8049b275c544c)


Team Members:
Lelia Erscoi, Irina Delamare and Sakshi Sharma

### Project Description:
The 3 of us form team 2 and we are working on creatting an interactive dashboard of covid19 casualties using streamlit for our OpenSource course.

You can check our dashboard with this [link](https://leliae-dashboardteam2-dashboard-6cmp3i.streamlit.app/).

*WE NEED A SUMMARY*


# Data
The COVID-19 dataset comes from the Our World in Data team from Johns Hopkins University. The data can be found at [owid/covid-19-data](https://github.com/owid/covid-19-data/tree/master/public/data).

###O verview:
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

