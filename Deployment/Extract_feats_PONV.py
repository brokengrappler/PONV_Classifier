import pandas as pd
import numpy as np

def select_surgery_features(analysis_df):
    proc_feat = analysis_df.iloc[:, np.r_[55, 58:83]].groupby('ponv').sum().T
    proc_feat['subtotal_surg'] = proc_feat[True]+proc_feat[False]
    proc_feat['ponv_rate'] = proc_feat[True]/proc_feat['subtotal_surg']
    # Filter surgeries with less than 20 samples in data set
    surg_ponv_summary = proc_feat[proc_feat['subtotal_surg']>20]
    surg_ponv_summary = surg_ponv_summary.sort_values(by='ponv_rate', ascending=False).reset_index()
    # Selected Surgery Features based on surgeries with > 30% PONV outcome
    surg_filter = list(surg_ponv_summary['index'][:19])
    return surg_filter

def extract_features(master_df, input_df):
    '''
    Filters features from master list for input into logistic regression model
    :param master_df:
        df containing all features
    :param analysis_df:
        subset of inputs (train, val, or test)
    :return:
        filtered input features
    '''
    # Apfel Features
    basic_feat = ['gender_code', 'non_smoker', 'previous_ponv', 'postoperative_opioids']
    age = ['age']
    chemo = ['previous_chemotherapy','how_many_months_ago_chemotherapy',
             'post_chemotherapy_nausea', 'post_chemotherapy_vomiting']
    # Took out emetogenics due to potential leakage

    dosage = ['fentanil_mcg', 'sufentanil_mcg', 'tramadol_dose_pacu',
              'ketamine_dose', 'intraoperative_morphine_dose']
    surgeries = select_surgery_features(master_df)
    master_feature_list = basic_feat+surgeries+dosage+chemo+age
    # get drug interaction feature engineering
    fe_drugs = total_drug_interaction(input_df)
    return pd.concat([input_df[master_feature_list], fe_drugs], axis=1)

def total_drug_interaction(analysis_df):
    '''
    Engineers feature of total volume of drugs given to patient
    :param analysis_df:
        input feature subset (train, val, or test)
    :return:
        Panda Series of total drugs given to each patient
    '''
    emetogenics = ['intraoperative_ondansetron_dose', 'dexamethasone_dose', 'intraoperative_dimenidrate_dose',
                   'metoclopramide_dose', 'droperidol_dose']
    total_drugs = pd.concat([analysis_df[emetogenics], analysis_df[['tramadol_dose_pacu', 'ketamine_dose',
                                      'intraoperative_morphine_dose','fentanil_mcg', 'sufentanil_mcg']]], axis=1)
    total_drugs['tot_drugs'] = total_drugs[['tramadol_dose_pacu', 'ketamine_dose',
                                      'intraoperative_morphine_dose']].sum(axis=1) + \
                            total_drugs[['intraoperative_ondansetron_dose', 'dexamethasone_dose',
                                          'intraoperative_dimenidrate_dose',
                                          'metoclopramide_dose', 'droperidol_dose']].sum(axis=1) + \
                            total_drugs[['fentanil_mcg', 'sufentanil_mcg']].sum(axis=1) / 1000
    return total_drugs['tot_drugs']
