import pickle
import pandas as pd
import numpy as np

# read in the model
my_model = pickle.load(open("lr_pickled_model.p","rb"))
scaler = pickle.load(open("ponv_scaler.p","rb"))
# pickle standardscaler and load here

# create a function to take in user-entered amounts and apply the model
def ponv_prediction(amounts_float, model=my_model):
    
    # # put everything in terms of tablespoons
    # # flour, milk, sugar, butter, eggs, baking powder, vanilla, salt
    # multipliers = [16, 16, 16, 16, 3, .33, .33, .33]
    #
    # # sum up the total values to get the total number of tablespoons in the batter
    # total = np.dot(multipliers, amounts_float)
    #
    # # note the proportion of flour and sugar
    # flour_cups_prop = multipliers[0] * amounts_float[0] * 100.0 / total
    # sugar_cups_prop = multipliers[2] * amounts_float[2] * 100.0 / total

    sc_amounts_float = scaler.transform(amounts_float)
    # inputs into the model
    input_df = sc_amounts_float

    # make a prediction
    prediction = my_model.predict(input_df)[0]

    # return a message
    message_array = ["Lower risk of PONV",
                     "Higher risk of PONV!"]

    return message_array[prediction]
