import streamlit as st
import helper
import pickle
from xgboost import XGBClassifier

model = pickle.load(open('model.pkl','rb'))
rfmodel = pickle.load(open('rfmodel.pkl','rb'))

st.header('Duplicate Question Pairs')

q1 = st.text_input('Enter question 1')
q2 = st.text_input('Enter question 2')

if st.button('Find'):
    query = helper.query_point_creator(q1,q2)
    result = model.predict(query)[0]
    # result2 = rfmodel.predict(query)[0]

    if result:
        st.title('Duplicate')
        # st.header('Duplicate')
    else:
        st.title('Not Duplicate')
        # st.header('Not Duplicate')
