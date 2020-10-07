


def apfel_prob(test_df, test_y):
    '''
    Outputs probability of PONV based on Apfel score
    :param test_df:
        Input dataframe that includes patientid and apfel features
    :param test_y:
        Actual PONV outcome
    :return:
        Dataframe with soft and hard outcomes
    '''
    apfel_output = test_df[['patientid', 'apfel']]
    apfel_output['apfel_prob'] = apfel_output['apfel'].map({0: .1, 1: .2, 2: .4, 3: .6, 4: .8})
    apfel_output['apfel_pred'] = apfel_output['apfel_prob'].apply(lambda x: True if x > 0.5 else False)
    apfel_output['actual'] = test_y
    return apfel_output