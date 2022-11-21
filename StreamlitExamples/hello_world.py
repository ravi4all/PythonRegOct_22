# pip install streamlit
import streamlit as st

st.title("This is streamlit")
st.write("Hello How are you...")

val = st.slider("val_1")
st.write(val, "squared is :",val * val)