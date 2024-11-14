import streamlit as st


st.title("**About Project**")
st.image("mumbai_img.jpg",width=500,caption='Mumbai')
st.header("This project is build on mumbai's 8500 flats dataset.")

st.write("1. The data was scraped from the housing.com using selenium and BeautifulSoup.")
st.write("2. The data cleaning was done in jupyter notebook using pandas and numpy.")
st.write("3. Done the exploratory data analysis using matplotlib and seaborn to get the understanding of data.")
st.write("4. Performed feature engineering, outlier detection and feature selection.")
st.write("5. Detected the outliers using Box plot, histogram and IQR method. to do the feature selection utilized statistical test like anova and applied the tree algorithm to get the feature importance.")
st.write("6. Applied different different algorithm and got best result on SVR then applied the grid searchSV to get the best parametrs.")
st.write("7. divided this project into three section Analysis section, flat price prediction and flat recommendation based on user input.")

