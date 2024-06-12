import streamlit as st
import pickle
import pandas as pd
import numpy as np

pipe = pickle.load(open('pipeline.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))
st.set_page_config(page_title='price predictor')
st.title("Mumbai Flat Price Predictor")
st.warning("Prices are in Cr")

selected_bhk = st.selectbox("Select BHK",sorted(df['flat_type'].unique()))
selected_location = st.selectbox("Select Location",sorted(df['location1'].unique()))
buildup_area = st.number_input("Enter Buildup Area (SQFT)")
age_property = st.selectbox("Age of property",["0-2","3-10","11-20","21-50","Greater than 50"])
furnishing = st.selectbox("Select Furnishing Type",sorted(df['furnishing'].unique()))
bedrooms = st.selectbox("Select Number of Bedrooms",sorted(df['bedrooms'].unique()))
bathrooms = st.selectbox("Select Number of Bathrooms",sorted(df['bathrooms'].unique()))
balcony = st.selectbox("Select Number of Balcony",sorted(df['balcony'].unique()))
parking = st.selectbox("Parking",sorted(df['parking'].unique()))

btn = st.button("Submit")

if age_property == "0-2":
    age_property =  "new construction"
elif age_property == "3-10":
    age_property = "recent construction"
elif age_property == "11-20":
    age_property = "modern property"
elif age_property == "21-50":
    age_property = "mid age property"  
else:
    age_property = "old propert" 

if btn:
    input = [selected_bhk,selected_location,buildup_area,age_property,furnishing,bedrooms,bathrooms,balcony,parking]
    new_df = pd.DataFrame([input],columns=df.columns)
    lower = round(np.expm1(pipe.predict(new_df)[0]) - np.expm1(pipe.predict(new_df)[0])*0.05,2)
    upper = round(np.expm1(pipe.predict(new_df)[0]) + np.expm1(pipe.predict(new_df)[0])*0.05,2)
    st.header(f"Your Flat price is between {lower} Cr. to {upper} Cr")
    
