CapstoneOne_PredictingSepsis
==============================

Springboard School of Data - June 2021

**Author**: Aisling Casey

**Mentor**: Tommy Blanchard 

**Overview**:  This project classifies if an ICU patient will develop Sepsis or not. 
Data from PhysioNet Computing in Cardiolgy Challenge 2019: https://physionet.org/content/challenge-2019/1.0.0/

**Start Here**: To get oriented with the project, first review the project proposal and other reports [here.](https://github.com/Aisling-C/Springboard/tree/main/CapstoneProject1/PredictingSepsis/reports)


Project Organization
------------
    ├── README.md         	<- The top-level README for developers using this project.
    ├── data		  	<- Note: Not available on github
    │   ├── interim       	<- Intermediate data that has been transformed.
    │   ├── processed     	<- The final, canonical data sets for modeling.
    │   └── raw            	<- The original, immutable data dump.
    │
    ├── notebooks          	<- Jupyter Notebooks containing all code
    │   ├── 1. DataWrangling  	<- Data loading, cleaning
    │   ├── 2. EDA            	<- Exploratory data analysis
    │   ├── 3. Preprocessing  	<- Preprocessing
    │   ├── 4.1 Modeling  	<- Model creation & metrics - version 1
    │   └── 4.2 Modeling       	<- Model creation & metrics - version 2
    │
    ├── reports             			<- Readable Reports
    │   ├── 1. ProjectProposal 			<- Initial project proposal
    │   ├── 2. FinalSlides_Sepsis      		<- Final Presentation on results
    │   ├── 3. Final Report    			<- Final report, problem identification through results & next steps
    │   ├── 4. Model Metrics   			<- Final model report
    │   └── PandasProfiling 			<- Pandas profiling report on raw data
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
    │
    └── requirements.txt  			<- External library requirements; Python  3.9.5
 

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
