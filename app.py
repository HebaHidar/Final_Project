import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.cluster import KMeans
st.set_page_config(page_title='Deployment-HebaHidar')

st.write ('This is Deployment for Customer Segmentation from bank in India (Real Data From Kaggle)')
st.write ('<h1 style="text-align:center;color:purple;"> Customer Segmentation Deployment </h1>' , unsafe_allow_html=True)

input_1 = st.number_input('Enter The Total Customer Account Balance')
st.write('Total Balance Is',input_1)

st.write('/')

input_2 = st.slider ('How Many Times Did You Collect?' ,1, 6 , 2 )
st.write (input_2,'Times')

ave_balnce = st.write ('This Is The Average Customer Account Balance' ,input_1/input_2)

input_3 = st.number_input('Enter The Total Customer Transaction Amount')
st.write('Total Transaction Amount Is',input_3)

st.write('/')

input_4 = st.slider ('How Many Times Did You Collect The Amount?' ,1 , 6 , 2 )
st.write (input_4 ,'Times')

ave_amount =st.write('This Is The Average Customer Transaction Amount',input_3/input_4)

Model_kmeans = pickle.load(open('model.pkl','rb'))


data = [[ave_balnce,ave_amount]]
df = pd.DataFrame(data, columns=['CustAccountBalance','TransactionAmount (INR)'])
if st.button('Calculate'):
    y_pred= Model_kmeans.predict(df)

    






