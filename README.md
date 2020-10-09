# PONV_Classifier  

## Multi-variable Logistic Regression Model to Estimate Probability of Post Operative Nausea and Vomiting (PONV)

Final product: 

https://ponv-app.herokuapp.com

## Description 
Logistic Regression model that outputs the probability a patient may experience PONV based on the following features:

1. Gender (0: Male; 1: Female)
2. Non_Smoker (bool)
3. previous_ponv (bool)
4. postoperative_opioids (bool)
5. Age (int range 18-100)
6. Type of Surgery (str)
7. fentanil_mcg (float)
8. sufentanil_mcg (float)
9. tramadol_dose_pacu (float)
10. ketamine_dose (float)
11. morphine_dose (float)
12. previous_chemotherapy (float)
13. how_many_months_ago_chemotherapy (int)
14. post_chemotherapy_nausea (bool)
15. post_chemotherapy_vomiting (bool)

## File Contents

#### Files For StreamLit App  
- **ST_PONV_app:** App built in streamlit that takes feature inputs and output PONV probability as output. Requires pickled scaler and final logistic models be in the same directory (ponv_scaler.p and lr_final_model.p). These files are created in the iter2_logreg.ipynb notebook
- **iter2_logreg.ipynb:** Notebook where test data is input into final model, along with results metrics. Dependencies include the following python scripts:  
	- **Extract_feats_PONV.py:** Extract selected features from the master dataframe 
	- **baseline_apfel.py:** Outputs probability of PONV based on patient Apfel score
	- **Oversample.py:** Oversample minority outcomes 

## Dependencies  
pandas==1.0.5
imbalanced_learn==0.7.0
numpy==1.18.5
imblearn==0.0
scikit_learn==0.23.2
streamlit==0.67.1
xgboost==1.2.0

#### Files for ETL, EDA, feature engineering, and validation
Files to The following files will not run unless I activate my EC2.
- **Project-3-Cleaning.ipynb:** Script to clean raw data to load into postgres SQL database on AWS EC2 instance. Includes creating three new tables to be loaded on postgres for converting strings to categorical ordinal data.
- **P3_EDA.ipynb:** EDA, feature selection, and feature engineering notebook. 
- **log_reg_tuning:** Script to oversample and run stratified K-fold cross validation on various models. 

## Data Source

Guimaraes, Gabriel (2018), “PONV risk factors in onchological surgery”, Mendeley Data, v1
http://dx.doi.org/10.17632/gsnj8vmgm2.1
Abstract: https://www.mendeley.com/catalogue/45dc09ac-2137-3b81-a018-bd9a27912659/

Institutions
Universidade de Sao Paulo, Universidade de Sao Paulo Instituto do Cancer do Estado de Sao Paulo

Published: 2018-03-27

Description
Preoperative, intraoperative and postoperative data to select the best predictors for postoperative nausea and vomiting in onchologic patients.

