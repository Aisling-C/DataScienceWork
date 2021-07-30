CapstoneTwo_DiabetesPrevalence
==============================

July 2021 

Springboard School of Data

**Author**: Aisling Casey

**Mentor**: Tommy Blanchard 

**Overview**: This project uses demographic data from the US Census to predict changes in diabetes prevalence values at the US county level.  

**Start Here**: To get oriented with the project, first review the project proposal and other reports.

View the Tabelau dashboard of the project [here.](https://public.tableau.com/app/profile/aisling.casey/viz/Diabetes_Prevalence/USDiabetesPrevelance2004-2017)

Project Organization
------------
    ├── README.md         	<- The top-level README for this project.
    │
    ├── reports             	<- Readable Reports (Start Here)
    │   ├── ProjectProposal 	<- Initial project proposal
    │   ├── FinalPresentation	<- Final Presentation on results
    │   ├── FinalReport    		<- Final report, problem identification through results & next steps
    │   └── ModelMetrics   		<- Final model report
    │
    ├── data		  	<- Note: Not available on github
    │   ├── external       		<- Data from external sources- namely, a US counties geography file
    │   ├── interim       		<- Intermediate data that has been transformed.
    │   ├── processed     		<- The final, canonical data sets for modeling.
    │   └── raw            		<- The original, immutable data dump from Census API calls and manual csv file downloads
    │
    ├── models          		
    │   ├── All Models  		<- All models experimented with
    │   └── best_model_LSTM_4           <- Final, best performing LSTM network model in hdf5 file
    │
    ├── notebooks          		<- Jupyter Notebooks containing all code
    │   ├── 1. Data Wrangling  		<- US Census API Calls, saving data to local drive
    │   ├── 2. Data Cleaning		<- Merging data tables
    │   ├── 3. Exploratory Data Analysis <- Exploring relationship between variables
    │   └── 4. Modeling       		<- Model creation & evaluation
    │
    ├── references             		<- External Documentation
    │   └── census_api-guide       	<- How to make calls to the US Census API
    │
    ├── src                		<- Source code for use in this project.
    │   │
    │   ├── data           	 	<- Scripts to download data
    │   │   ├── ACS_API			<- Downlading Demographic Data (ACS) from Census API
    │   │   ├── ACS_variable_list	<- List of ACS variable names and shorthands
    │   │   └── PEP_API			<- Downloading PEP Population Data from Census API
    │   │
    │   ├── code_flow       		<- Scripts for reducing boilerplate 
    │   │   └── CreateJupyterNotebookHeadings.py
    │   │
    │   └── models         		<- Script to prepare data for modeling
    │       └── LSTM_Model		<- Functions for reshaping data, test/train splits for LSTM Model
    │
    ├── requirements1                	<- Packages to run notebooks 1-3. Python 3.9.5
    └── requirements2                	<- Packages to run notebook 4. Python 3.6.13. 
					   	Needed to downgrade Python and a few other
					   	libraries to play nice with tensorflow 1.14.0

	
--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
