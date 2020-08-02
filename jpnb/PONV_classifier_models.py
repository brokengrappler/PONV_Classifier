from sklearn.metrics import confusion_matrix, f1_score, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler

# Oversample script
import Oversample
import xgboost as xgb
import pandas as pd
import numpy as np

# Try to turn this into a class
# Have a method to initialize train and val sets
# Also have attirbutes for scaled features

def std_scale(x_tr,x_va):
    scaler = StandardScaler()
    sc_xtr = scaler.fit_transform(x_tr)
    sc_xva = scaler.transform(x_va)
    return sc_xtr, sc_xva

def evaluate_models(model_sel, x, y):
    # Need to incorporate scaling
    '''
    Fit a series of classifier models and print metrics
    arg:
        model_sel: list from 1-5
        1: Logistic Regression
        2: Random Forest
        3: Naive Bayes
        4: SVM
        5: xgBoost
        6: KNN
    '''

    model_menu = {
        1: LogisticRegression(),
        2: RandomForestClassifier(),
        3: GaussianNB(),
        4: SVC(),
        5: xgb.XGBClassifier(objective="binary:logistic"),
        6: KNeighborsClassifier(10)
    }
    model_prob_results={}
    f1_score_list=[]
    rocauc_score_list=[]
    # Generate kfolds
    skf = StratifiedKFold(n_splits=6, shuffle=True, random_state=444)

    for selection in model_sel:
        for tr_idx, va_idx in skf.split(x, y):
            tr_x, tr_y = x.iloc[tr_idx], y.iloc[tr_idx]
            va_x, va_y = x.iloc[va_idx], y.iloc[va_idx]
            # Get oversample set
            trx_os, try_os = Oversample.return_oversample(2, tr_x, tr_y)
            #scale and transform
            sc_xtr, sc_xva = std_scale(trx_os, va_x)
            model = model_menu[selection]
            model.fit(sc_xtr, try_os)
            f1_score_list.append(f1_score(va_y, model.predict(sc_xva)))
            if selection == 4:
                pass
            else:
                predict_proba = model.predict_proba(sc_xva)[:,1]
                rocauc_score_list.append(roc_auc_score(va_y,predict_proba))
        val_summary = dict(zip(va_idx, predict_proba))
        model_prob_results[selection] = val_summary
        print(str(model_menu[selection]).split('(')[0])
        print('Avg. f1 score:', np.array(f1_score_list).mean())
        print('Avg. Roc/Auc score', np.array(rocauc_score_list).mean())
    return model_prob_results

if __name__ == '__main__':
    # This only provides results for the base case with apfel features only
    tv_x = pd.read_pickle('../pkl_files/tv_x.pkl')
    tv_y = pd.read_pickle('../pkl_files/tv_y.pkl')
    model_selection = [1, 3, 5, 6]
    apfel_feat = ['gender_code', 'non_smoker', 'previous_ponv', 'postoperative_opioids']
    apfel_x = tv_x[apfel_feat]
    evaluate_models(model_selection, apfel_x, tv_y)