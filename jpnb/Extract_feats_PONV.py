import pandas as pd
import numpy as np

def select_surgery_features(analysis_df):
    proc_feat = analysis_df.iloc[:, np.r_[55, 60:83]].groupby('ponv').sum().T
    proc_feat['subtotal_surg'] = proc_feat[True]+proc_feat[False]
    proc_feat['ponv_rate'] = proc_feat[True]/proc_feat['subtotal_surg']
    # Filter surgeries with less than 20 samples in data set
    surg_ponv_summary = proc_feat[proc_feat['subtotal_surg']>20]
    surg_ponv_summary = surg_ponv_summary.sort_values(by='ponv_rate', ascending=False).reset_index()
    # Selected Surgery Features based on surgeries with > 30% PONV outcome
    surg_filter = list(surg_ponv_summary['index'][:18])
    return surg_filter

def extract_features(master_df, analysis_df):
    '''
    Filters features from master list for input into logistic regression model
    :param analysis_df:
        master list of input features
    :return:
        filtered input features
    '''
    # Apfel Features
    basic_feat = ['gender_code', 'non_smoker', 'previous_ponv', 'postoperative_opioids']
    age= ['age']
    chemo = ['previous_chemotherapy','how_many_months_ago_chemotherapy',
             'post_chemotherapy_nausea', 'post_chemotherapy_vomiting']
    emetogenics = ['intraoperative_ondansetron_dose', 'dexamethasone_dose', 'intraoperative_dimenidrate_dose',
                   'metoclopramide_dose', 'droperidol_dose']
    dosage = ['fentanil_mcg', 'sufentanil_mcg', 'tramadol_dose_pacu',
              'ketamine_dose', 'intraoperative_morphine_dose']
    surgeries = select_surgery_features(master_df)
    master_feature_list = basic_feat+surgeries+dosage+chemo+age+emetogenics
    return analysis_df[master_feature_list]

def total_drug_interaction(master_df, analysis_df):
    input_plus_FE = extract_features(master_df, analysis_df)
    input_plus_FE['tot_drugs'] = input_plus_FE[['tramadol_dose_pacu', 'ketamine_dose',
                                      'intraoperative_morphine_dose']].sum(axis=1) + \
                            input_plus_FE[['intraoperative_ondansetron_dose', 'dexamethasone_dose',
                                          'intraoperative_dimenidrate_dose',
                                          'metoclopramide_dose', 'droperidol_dose']].sum(axis=1) + \
                            input_plus_FE[['fentanil_mcg', 'sufentanil_mcg']].sum(axis=1) * 1000
    return input_plus_FE
