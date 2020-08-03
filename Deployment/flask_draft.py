import streamlit as st
import pandas as pd
import pickle

def load_model(input_dict):
    input_x = pd.DataFrame(input_dict, index=[0])
    my_model = pickle.load(open("lr_pickled_model.p","rb"))
    scaler = pickle.load(open("ponv_scaler.p","rb"))
    sc_x = scaler.transform(input_x)
    prediction = round(my_model.predict_proba(sc_x),2)
    print(f'{prediction})
    #return prediction

st.title('PONV Probability Calculator')

ponv_result = st.empty()

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
              'morphine_dose':0,
              'previous_chemotherapy':0,
              'how_many_months_ago_chemotherapy':0,
              'post_chemotherapy_nausea':0,
              'post_chemotherapy_vomiting':0,
              }

gender = st.radio('Gender:', ('Male', 'Female'))
if gender == 'Male':
    input_dict['Gender'] = 0
else:
    input_dict['Gender'] = 1

smoker = st.radio('Smoker:', ('Yes', 'No'))
if smoker == 'Yes':
    input_dict['Non_Smoker'] = 0
else:
    input_dict['Non_Smoker'] = 1

previous_ponv = st.radio('Prior PONV:', ('Yes', 'No'))
if previous_ponv == 'Yes':
    input_dict['previous_ponv'] = 1
else:
    input_dict['previous_ponv'] = 0

postoperative_opioids = st.radio('Post Operative Opioids:', ('Yes', 'No'))
if postoperative_opioids == 'Yes':
    input_dict['postoperative_opioids'] = 1
else:
    input_dict['postoperative_opioids'] = 0

# Creating list for Surgery Selection input
clean_surg_list = [
    'Pancreatectomy',
     'Hysterectomy(Laproscopic)',
     'Anexectomy/Ovariectomy',
     'Cystectomy',
     'Extensive Lymphadenectomy',
     'Plastic Surgery',
     'Cytoreduction',
     'Hysterectomy',
     'Nephrectomy',
     'Mastectomy',
     'Thoracic',
     'Exploratory_laparotomy',
     'Hepatectomy',
     'Prostatectomy',
     'Breast lumpectomy',
     'Spine surgery',
     'Head neck',
     'Orthopedic',
    'Other'
]

option = st.selectbox('Surgicel Procedure:',(sorted(clean_surg_list)))

input_surg_list = [
    'pancreatectomy',
    'hysterectomy_vlp',
    'anexectomy_ovariectomy',
    'cystectomy',
    'extensive_lymphadenectomy',
    'plastic',
    'cytoreduction',
    'hysterectomy',
    'nephrectomy',
    'mastectomy',
    'thoracic',
    'exploratory_laparotomy',
    'hepatectomy',
    'prostatectomy',
    'breast_lumpectomy',
    'spine_surgery',
    'head_neck',
    'orthopedic']
input_surg_dict = dict(zip(clean_surg_list,input_surg_list))
if option == 'Other':
    pass
else:
    input_dict[input_surg_dict[option]] = 1

input_dict['fentanil_mcg'] = st.slider('Fentinal (mcg)', min_value=0.0, max_value=500.0, step=1.0)/1000
input_dict['sufentanil_mcg']=st.slider('Sufentanil (mcg)', min_value=0.0, max_value=500.0, step=1.0)/1000
input_dict['tramadol_dose_pacu']=st.slider('tramadol (mg)', min_value=0.0, max_value=50.0, step=1.0)
input_dict['ketamine_dose']=st.slider('ketamine (mg)', min_value=0.0, max_value=50.0, step=1.0)
input_dict['morphine_dose']=st.slider('Morphine (mg)', min_value=0.0, max_value=50.0, step=1.0)

pr_chemo = st.radio('Prior Chemotherapy:', ('Yes', 'No'))
if pr_chemo == 'Yes':
    input_dict['previous_chemotherapy'] = 1
    input_dict['how_many_months_ago_chemotherapy'] = st.number_input('Last Chemo (mos. ago)')
else:
    input_dict['previous_chemotherapy'] = 0

chemo_nausea = st.radio('Post Chemo Nausea:', ('Yes', 'No'))
if chemo_nausea == 'Yes':
    input_dict['post_chemotherapy_nausea'] = 1
else:
    input_dict['post_chemotherapy_nausea'] = 0

chemo_vomit = st.radio('Post Chemo Vomit:', ('Yes', 'No'))
if chemo_vomit == 'Yes':
    input_dict['post_chemotherapy_vomiting'] = 1
else:
    input_dict['post_chemotherapy_vomiting'] = 0

# if st.button('PONV Probability'):
ponv_result.header(load_model(input_dict)[0,1])

# To debug potential values
st.write(input_dict)