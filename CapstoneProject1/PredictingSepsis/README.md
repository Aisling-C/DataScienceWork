CapstoneOne_PredictingSepsis
==============================

This project classifies if an ICU patient will develop Sepsis or not. 
Data from PhysioNet Computing in Cardiolgy Challenge 2019: https://physionet.org/content/challenge-2019/1.0.0/

Project Organization
------------
    ├── README.md         	<- The top-level README for developers using this project.
    ├── data		  	<- Note: Not available on github
    │   ├── interim       	<- Intermediate data that has been transformed.
    │   ├── processed     	<- The final, canonical data sets for modeling.
    │   └── raw            	<- The original, immutable data dump.
    │
    ├── models         
    │   └── finalized_sepsis_model  <- Final Model for predicting Sepsis
    │
    ├── notebooks          	<- Jupyter Notebooks containing all code
    │   ├── 1. DataWrangling  	<- Data loading, cleaning
    │   ├── 2. EDA            	<- Exploratory data analysis
    │   ├── 3. Preprocessing  	<- Preprocessing
    │   ├── 4.1 Modeling  	<- Model creation & metrics - version 1
    │   └── 4.2 Modeling       	<- Model creation & metrics - version 2
    │
    ├── reports             			<- Readable Reports
    │   ├── CapstoneOne_FinalSlides_Sepsis      <- Final Presentation on results
    │   ├── Final Report    			<- Final report, problem identification through results & next steps
    │   ├── Model Metrics   			<- Final model report
    │   ├── PandasProfiling 			<- Pandas profiling report on raw data
    │   └── ProjectProposal 			<- Initial project proposal
    │
    ├── src                			<- Source code for use in this project.
    │   │
    │   ├── data        
    │   ├── _patient_Classification_.py    	<- Get patient level classification rather than hourly 
    │   ├── CreateJupyterNotebookHeadings.py    <- Create custom Jupyter Notebook Headings
    │   ├── Custom_Func.py                      <- Determine percentage of positive & negative instances in a data set
    │   ├── Elapsed_Time.py                     <- Determine time elapsed from start to end of a code block
    │   ├── PlotFeatureImportance.py            <- Code to plot feature importance of tree based models
    │   ├── plotPrecisionRecall_.py             <- Code to plot precision & recall curves for test & train data
    │   └── time_elapsed.py                     <- Determine time elapsed from start to end of a code block
 

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
