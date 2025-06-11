import streamlit as st

st.title("Text Input: ")

name = st.text_input("Enter Your Name: ")
if name:
    st.write(f"Hello, {name}!")
age = st.slider("Select Your Age:", 0,100,25)
st.write(f"Your age is, {age}!")

options = ["Python","Javascript","C++","Verilog"]
choice = st.selectbox("Choose your Favourite Language: ", options)
st.write(f"Your selected choice is {choice}")
