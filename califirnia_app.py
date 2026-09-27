#------ stp1:- install the packages------------------------ 

import numpy as np 
import joblib 
import streamlit as st 

#------step no.2:- load the model---------------------------

obj = joblib.load('california2.joblib')  # it is dictionar 
model = obj['model']                     # it is model 
cols = obj['columns']   # load columns 

#----- create an app using streamlit---------------------------------

st.title('California app')

In=[]

for i in cols:
    v = st.number_input(f'Enter {i} value:- ')  # for loop on columns 
    In.append(v)
if st.button('click'):
    input = np.array([In])
    out = model.predict(input)
    st.success(f'The Median House Value is : {out}')



# to run file type in terminal :- cd Streamlit_UI  press enter
# after that type :- python -m streamlit run califirnia_app.py   presss enter 