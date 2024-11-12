import pandas as pd
import streamlit as st

data = pd.read_csv("data/mumbai_flats_cleaned_v4.csv")
data.drop(columns=['floor_type'],inplace=True)
data.drop_duplicates(inplace=True)
st.set_page_config(page_title='Recommendation section')
def recommend_flats(data, location=None, bhk_type=None, min_price=None, max_price=None, top_n=5):
    
    filtered_data = data.copy()
    if location:
        filtered_data = filtered_data[filtered_data['location1'] == location]
    if bhk_type:    
        filtered_data = filtered_data[filtered_data['flat_type'] == bhk_type]

    if min_price is not None:
        filtered_data = filtered_data[filtered_data['flat_price'] >= min_price]
    if max_price is not None:
        filtered_data = filtered_data[filtered_data['flat_price'] <= max_price]

    recommended_flats = filtered_data.sort_values(by='flat_price').head(top_n)
    recommended_flats.reset_index(drop=True, inplace=True)
    return recommended_flats

st.title('Mumbai Flats Recommendation')
st.warning("Prices are in Cr")

locations = data['location1'].unique().tolist()
locations.insert(0,None)

flat_type = data['flat_type'].unique().tolist()
flat_type.insert(0,None)

selected_location = st.selectbox("Select Location",locations)
selected_bhk = st.selectbox("Select BHK",flat_type)

minimum_price = st.number_input("Enter Your Minimum Budget in Cr(45 lakhs then 0.45)",value=0.3)
maximum_price = st.number_input("Enter Your Maximum Budget in Cr(45 lakhs then 0.45)",value=1.0)


top = st.slider("Number of Recommendations", 3, 5,10)

if st.button("Recommend"):
    flats = recommend_flats(data=data,location=selected_location,bhk_type=selected_bhk,
                    min_price=minimum_price,max_price=maximum_price,top_n=top)
    
    
    st.dataframe(flats)
