import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipeline.pkl','rb'))
df = pickle.load(open('X.pkl','rb'))
st.set_page_config(page_title='price predictor')
st.title("Mumbai Flat Price Predictor")
st.warning("Prices are in Cr")

selected_bhk = st.selectbox("Select BHK",sorted(df['flat_type'].unique()))
selected_location = st.selectbox("Select Location",sorted(df['address'].unique()))
buildup_area = st.number_input("Enter Buildup Area (SQFT)")
which_floor = st.selectbox("Which floor",["lower(<20)","middle(20-50)","higher"])
furnishing = st.selectbox("Select Furnishing Type",sorted(df['furnishing'].unique()))
bedrooms = st.selectbox("Select Number of Bedrooms",sorted(df['bedrooms'].unique()))
balcony = st.selectbox("Select Number of Balcony",sorted(df['balcony'].unique()))


btn = st.button("Submit")
if which_floor == "lower(<20)":
    which_floor = "lower"
elif which_floor == "middle(20-50)":
    which_floor = "middle"
else:
    which_floor = which_floor

if btn:
    input = [selected_bhk,selected_location,buildup_area,which_floor,furnishing,bedrooms,balcony]
    new_df = pd.DataFrame([input],columns=df.columns)
    lower = round(np.expm1(pipe.predict(new_df)[0]) - np.expm1(pipe.predict(new_df)[0])*0.05,2)
    upper = round(np.expm1(pipe.predict(new_df)[0]) + np.expm1(pipe.predict(new_df)[0])*0.05,2)
    st.header(f"Your Flat price is between {lower} Cr. to {upper} Cr")
    
