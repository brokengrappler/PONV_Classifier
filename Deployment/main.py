from flask import Flask, request, render_template
from make_prediction import muffin_or_cupcake

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
    ingredients = ['gender_code', 'non_smoker', 'previous_ponv', 'postoperative_opioids',
                   'surgery', 'fentanil_mcg', 'sufentanil_mcg', 'tramadol_dose_pacu', 'ketamine_dose',
                   'intraoperative_morphine_dose', 'previous_chemotherapy', 'how_many_months_ago_chemotherapy',
                   'post_chemotherapy_nausea', 'post_chemotherapy_vomiting']

    # error messages to ensure correct units of measure
    bool_val = ["Gender", "Non_Smoker", "Prior_Ponv", "postoperative_opioids",
                'previous_chemotherapy', 'how_many_months_ago_chemotherapy',
                'post_chemotherapy_nausea', 'post_chemotherapy_vomiting']
    str_val = ["Surgery"]
    float_val = ['fentanil_mcg', 'sufentanil_mcg', 'tramadol_dose_pacu', 'ketamine_dose',
                'intraoperative_morphine_dose']
    # hold all amounts as floats

    # bool test
    for i, ing in enumerate(ingredients):
        user_input = request.form[ing]
        try:
            float_ingredient = float(user_input)
        except:
            return render_template('index.html', message=messages[i])
        amounts.append(float_ingredient)
    # str test
    for i, ing in enumerate(ingredients):
        user_input = request.form[ing]
        try:
            float_ingredient = float(user_input)
        except:
            return render_template('index.html', message=messages[i])
        amounts.append(float_ingredient)
    # float test
    for i, ing in enumerate(ingredients):
        user_input = request.form[ing]
        try:
            float_ingredient = float(user_input)
        except:
            return render_template('index.html', message=messages[i])
        amounts.append(float_ingredient)

    # show user final message
    final_message = muffin_or_cupcake(amounts)
    return render_template('index.html', message=final_message)

if __name__ == '__main__':
    app.run(debug=True)