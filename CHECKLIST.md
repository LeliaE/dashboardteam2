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
- [x] The codemeta.json file is present and filled properly.

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
- [x] Dashboard displays graphics of Covid-19 cases or deaths vs time for several countries.
- [x] Data are normalized with respect to the number of inhabitants per country.
- [x] Raw number, cumulative number and the (rolling) average number of cases or deaths could be displayed.
- [x] The graph has proper axis names with “Date” for the x-axis and a name updated live for the y-axis (for instance “raw cases per million”, “average deaths per million”...) 
- [ ] Peak (wave) detection is implemented for cumulative number of cases or deaths.

### Interaction
- [x] User can select which countries to display in the same graphic (among a predefined list of countries).
- [x] User can select to display Covid-19 cases or deaths.
- [x] User can select to display the raw number, cumulative number or the 7-day rolling average.
- [x] User can select the time frame to display. Either with a double slider or with 2 date pickers.
- [ ] User can select to display or not the peak detection (for cumulative numbers only).
