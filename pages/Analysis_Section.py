import streamlit as st
import plotly.express as px
import pandas as pd


st.header('Welcome to Analytics')

st.write('Average Price Across Mumbai')
data = pd.read_csv('location.csv')
fig = px.scatter_mapbox(data,lat='latitude',lon='longitude',size='flat_price',
                         color='flat_price', hover_name='location',zoom=8.5,
                         mapbox_style="open-street-map",color_continuous_scale='plotly3')
st.plotly_chart(fig,use_container_width=True)

df = pd.read_csv('data_for_model.csv')[['flat_type','flat_price','location1',
                                                 'buildupArea_sqft','bedrooms','bathrooms']]

st.write("Distribution of Price According to Flat Type")
locations = df['location1'].unique().tolist()
locations.insert(0,'Overall')
selected_location = st.selectbox("Select Location",locations)
if selected_location == 'Overall':
    fig1 = px.box(df,x='flat_type',y='flat_price')
    st.plotly_chart(fig1,use_container_width=True)
else:    
    d = df[df['location1'] == selected_location]
    fig2 = px.box(d,x='flat_type',y='flat_price')
    st.plotly_chart(fig2,use_container_width=True)

st.write("Relation Between Builup Area and Price")
fig3 = px.scatter(data_frame=df,x='buildupArea_sqft',y='flat_price',color='bedrooms',
                  color_continuous_scale='plotly3')
st.plotly_chart(fig3,use_container_width=True)

st.write("BHK Pie Chart")
locations1 = df['location1'].unique().tolist()
locations1.insert(0,'Overall')
selected_location1 = st.selectbox("Select Location1",locations1)
if selected_location1 == 'Overall':
    fig3 = px.pie(data_frame=df,names='bedrooms')
    st.plotly_chart(fig3,use_container_width=True)
else:
    d1 = df[df['location1'] == selected_location1]   
    fig4 = px.pie(data_frame=d1,names='bedrooms') 
    st.plotly_chart(fig4,use_container_width=True)