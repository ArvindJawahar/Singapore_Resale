# Import necessary libraries
import streamlit as st
import pandas as pd
import pickle

# Load data
data = pd.read_csv(r'E:\GitHub\Singapore_Resale\Data\Singapore_Resale_Flat_Prices_Predicting.csv')

# Create dictionary to get the encoded values
town_dict = dict(zip(data['town'].unique(), data['town_code'].unique()))
model_dict = dict(zip(data['flat_model'].unique(), data['flat_modelcode'].unique()))
town_list = data['town'].unique()
model_list = data['flat_model'].unique()
room_category = {'1 ROOM': 1,
       '2 ROOM':2,
       '3 ROOM':3,
       '4 ROOM':4,
       '5 ROOM':5,
       'EXECUTIVE':6,
       'MULTI GENERATION':7}
type_list = list(room_category.keys())

# Set page config for the web app
st.set_page_config(page_title='Resale Price Prediction', layout='wide')
st.title('Singapore Flat Resale Price Prediction')

# Create columns in UI
col1,col2,col3,col4 = st.columns(4)

with col1:
   # Create input field for year input
   selling_year = st.number_input('Selling Year',value=None, placeholder="yyyy") #number_input

with col2:
   # Create input field for month input
   selling_month = int(st.select_slider('Selling month',options=[1,2,3,4,5,6,7,8,9,10,11,12])) #select_slider

with col3:
   # Create input field for town
   town_key= st.selectbox('Town',options=town_list)

with col4:
    # Create input field for flat type
    flat_type_key = st.selectbox('Flat Type',options=type_list)



with col1:
    # Create sub-columns within col1 for storey range
    subcol1, subcol2 = st.columns(2)

    with subcol1:
        # Create input field for storey range min
        storey_range_min = st.text_input('Storey range (Min)', value=None, placeholder="e.g., 01")  # text_input

    with subcol2:
        # Create input field for storey range max
        storey_range_max = st.text_input('Storey range (Max)', value=None, placeholder="e.g., 03")  # text_input

with col2:
   # Create input field for floor area
    floor_area_sqm = st.number_input('Floor Area (sqm)',value=None, placeholder="Type floor area...") #number_input

with col3:
   # Create input field for flat model
    flat_model = st.selectbox('Flat Model',options = model_list) #text_input

with col4:
   # Create input field for lease commence date
    lease_commence_date = st.number_input('Lease Commence Date',value=None, placeholder="yyyy") #number_input

# Absolute path to the pickle file
file_path = "E:/GitHub/Singapore_Resale/linear_regression_model.pkl"

# Function to load pickled model
def model_data():
    with open(file_path, "rb") as files:
        model = pickle.load(files)
    return model

# Function to predict
def predict(model, selling_year, selling_month, town_code, storey_min, storey_max, floor_area_sqm, flat_modelcode, lease_commence_date):
    pred_value = model.predict([[selling_year, selling_month, town_code, storey_min, storey_max, floor_area_sqm,
                                 flat_modelcode, lease_commence_date]])

    return pred_value

# Create predict button
button_clicked = st.button('Predict Price')
if button_clicked:
    town = town_dict[town_key]
    flat_type = room_category[flat_type_key]

    # Retrieve values from input fields
    storey_min = storey_range_min.strip()
    storey_max = storey_range_max.strip()

    # Check if both input fields are not empty
    if storey_min and storey_max:
        storey_min = int(storey_min)
        storey_max = int(storey_max)
    else:
        st.error("Please enter valid values for both minimum and maximum storey range.")
        st.stop()

    flat_modelcode = model_dict[flat_model]

    # Call predict function
    pred = predict(model_data(), selling_year, selling_month, town, storey_min, storey_max, floor_area_sqm, flat_modelcode, lease_commence_date)

    # Display predicted price in dollar
    st.success(f'Predicted Price: ${pred[0]:,.2f}')

        # Display predicted price in INR
    st.success(f'Resale Price in INR: ₹{(pred[0] * 63.02):,.2f}')
