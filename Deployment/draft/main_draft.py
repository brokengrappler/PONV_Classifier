from flask import Flask, request, render_template
from make_prediction import ponv_prediction
import pandas as pd
import numpy as np

# create a flask object
app = Flask(__name__)

# creates an association between the / page and the entry_page function (defaults to GET)
@app.route('/')
def entry_page():
    return render_template('index.html')

# creates an association between the /predict_recipe page and the render_message function
# (includes POST requests which allow users to enter in data via form)
@app.route('/predict_recipe/', methods=['GET', 'POST'])
def render_message():
    # user-entered ingredients
    bool_val = ["Gender", "Non_Smoker", "previous_ponv", "postoperative_opioids",
                'previous_chemotherapy', 'post_chemotherapy_nausea',
                'post_chemotherapy_vomiting']
    int_val = ['Surgery']
    float_val = ['fentanil_mcg', 'sufentanil_mcg', 'tramadol_dose_pacu', 'ketamine_dose',
                 'intraoperative_morphine_dose','how_many_months_ago_chemotherapy']
    #took out
    input_dict = {"Gender":0,
                  "Non_Smoker":0,
                  "previous_ponv":0,
                  "postoperative_opioids":0,
                  'pancreatectomy':0,
                  'hysterectomy_vlp':0,
                  'anexectomy_ovariectomy':0,
                  'cystectomy':0,
                  'extensive_lymphadenectomy':0,
                  'plastic':0,
                  'cytoreduction':0,
                  'hysterectomy':0,
                  'nephrectomy':0,
                  'mastectomy':0,
                  'thoracic':0,
                  'exploratory_laparotomy':0,
                  'hepatectomy':0,
                  'prostatectomy':0,
                  'breast_lumpectomy':0,
                  'spine_surgery':0,
                  'head_neck':0,
                  'orthopedic':0,
                  'fentanil_mcg':0,
                  'sufentanil_mcg':0,
                  'tramadol_dose_pacu':0,
                  'ketamine_dose':0,
                  'intraoperative_morphine_dose':0,
                  'previous_chemotherapy':0,
                  'how_many_months_ago_chemotherapy':0,
                  'post_chemotherapy_nausea':0,
                  'post_chemotherapy_vomiting':0,
                }
    # bool test
    for i, ing in enumerate(bool_val):
        user_input = request.form[ing]
        try:
            bool_input = bool(user_input)
        except:
            return render_template('index.html', message='Enter Boolean')
        input_dict[ing] = bool_input

    # surgery
    for i, ing in enumerate(int_val):
        user_input = request.form[ing]
        try:
            user_input in int_val
        except:
            return render_template('index.html', message='Pick valid surgery')
        input_dict[user_input] = 1

    # float test
    for i, ing in enumerate(float_val):
        user_input = request.form[ing]
        try:
            float_input = float(user_input)
        except:
            return render_template('index.html', message='Must be float')
        input_dict[ing] = float_input
    input_np = pd.DataFrame(input_dict, index=[0]).iloc[0,:]
    # show user final message
    # debug = list(input_np.iloc[0,:])
    # return '<br>'.join(debug)
    # final_message = ponv_prediction(np.array(input_np).reshape(1,-1))
    return '<br>'.join(list(str(input_np)))
    # return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)