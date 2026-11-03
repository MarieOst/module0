import streamlit as st
import requests

st.title("My Streamlit App")

with st.sidebar:
    st.subheader("Sidebar")
    st.write("Ma super sidebar")
    st.image("https://via.placeholder.com/150", caption="ClaimGuard Portal")


st.button("Click me!")

text = st.text_input("Clé d'accès", type="password")

