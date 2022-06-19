import numpy as np
import pandas as pd
import streamlit as st
st.set_page_config(page_title='Census | Main', page_icon='logo.png', layout='centered', initial_sidebar_state='auto')
@st.cache()
def load_data():
	df = pd.read_csv('https://student-datasets-bucket.s3.ap-south-1.amazonaws.com/whitehat-ds-datasets/adult.csv', header=None)
	column_name =['age', 'workclass', 'fnlwgt', 'education', 'education-years', 'marital-status', 'occupation', 
               'relationship', 'race','gender','capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
	for i in range(df.shape[1]):
	  df.rename(columns={i:column_name[i]},inplace=True)
	df['native-country'] = df['native-country'].replace(' ?',np.nan)
	df['workclass'] = df['workclass'].replace(' ?',np.nan)
	df['occupation'] = df['occupation'].replace(' ?',np.nan)
	df.dropna(inplace=True)
	df.drop(columns='fnlwgt',axis=1,inplace=True)
	return df

df = load_data()
st.header('Census Data')
st.write('This app will help you to visualize the census data\n\n')
with st.expander('View Data'):
	st.table(df.head())
c1, c2 = st.columns(2)
with c1:
	if st.checkbox('Show column names'):
		st.table(df.columns)
with c2:
	if st.checkbox('Show data description'):
		st.table(df.describe())
c3, c4 = st.columns(2)
with c3:
	if st.checkbox('Show column data-types'):
		st.table(df.dtypes)
with c4:
	if st.checkbox('Show column data'):
		st.table(df[st.selectbox('Select column',df.columns)].value_counts())
