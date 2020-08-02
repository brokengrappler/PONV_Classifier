from sklearn.metrics import f1_score, roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
import Oversample
import pickle

import pandas as pd
import numpy as np

def std_scale(x_tr,x_va):
    '''
    Standard scaler
    :param x_tr:
        training features
    :param x_va:
        validation features
    :return:
        scaled train and validation features
    '''
    scaler = StandardScaler()
    sc_xtr = scaler.fit_transform(x_tr)
    sc_xva = scaler.transform(x_va)
    return sc_xtr, sc_xva

def ponv_log_reg(x,y):
    '''
    Fit logistic regression model using stratified k-fold and prints metrics
    :param x:
        train and validation features
    :param y:
        train and validation targets
    :return:
        Logistic regression model
    '''
    f1_score_list = []
    rocauc_score_list = []
    # Generate kfolds
    skf = StratifiedKFold(n_splits=10, shuffle=True, random_state=444)
    lr = LogisticRegression(C=100, fit_intercept=False, solver='liblinear', tol=1e-6, max_iter=1000)

    for tr_idx, va_idx in skf.split(x, y):
        tr_x, tr_y = x.iloc[tr_idx], y.iloc[tr_idx]
        va_x, va_y = x.iloc[va_idx], y.iloc[va_idx]
        # Get oversample set
        trx_os, try_os = Oversample.return_oversample(2, tr_x, tr_y)
        # scale and transform
        sc_xtr, sc_xva = std_scale(trx_os, va_x)
        lr.fit(sc_xtr, try_os)
        f1_score_list.append(f1_score(va_y, lr.predict(sc_xva)))
        predict_proba = lr.predict_proba(sc_xva)[:, 1]
        rocauc_score_list.append(roc_auc_score(va_y, predict_proba))
    print('Avg. f1 score:', np.array(f1_score_list).mean())
    print('Avg. Roc/Auc score', np.array(rocauc_score_list).mean())

    return lr

if __name__ == '__main__':
    agg_df_x = pd.read_pickle('../pkl_files/agg_df_x.pkl')
    tv_y = pd.read_pickle('../pkl_files/tv_y.pkl')
    ponv_log_reg(agg_df_x, tv_y)
