import pandas as pd
import numpy as np
import streamlit as st


a=[1,2,3,4,5,6,7,8]
n = np.array(a)
nd = n.reshape((2,4))
dic = {
    'name':'ayaansh',
    'age':11,
    'city':'gurugram'
}

st.dataframe(a)
st.dataframe(n)
st.dataframe(nd)
st.dataframe(dic)
st.table(dic)
st.json(dic)
st.write(dic)