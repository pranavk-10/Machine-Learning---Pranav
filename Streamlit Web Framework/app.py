import streamlit as st
import pandas as pd
import numpy as np

st.title("APP")

st.write("Santrupt and Pranav are Probably Friends")

df = pd.DataFrame({
    "first columnn": [1,2,3,4,5],
    "second column": [10,20,30,40,50]
})

st.write("Here is the Dataframe: ")
st.write(df)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),columns=['a','b','c']
)

st.line_chart(chart_data)