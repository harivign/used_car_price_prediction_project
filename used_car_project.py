import streamlit as st 

# Title of the app
st.title('Used Car Price Prediction')

# Description
st.write('This is a web application to predict the price of a used car based on various features.')

# Input fields for user to enter car details
car_name = st.text_input('Car Name')
year = st.number_input('Year of Purchase', min_value=1900, max_value=2023, step=1)
present_price = st.number_input('Present Price (in lakhs)', min_value=0.0, step=0.1)
kms_driven = st.number_input('Kms Driven', min_value=0, step=1)
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
seller_type = st.selectbox('Seller Type', ['Dealer', 'Individual'])
transmission = st.selectbox('Transmission Type', ['Manual', 'Automatic'])
owner = st.selectbox('Number of Previous Owners', [0, 1, 2, 3])

# Button to predict price
if st.button('Predict Price'):
    # Placeholder for prediction logic
    st.write('Prediction logic will be implemented here.')