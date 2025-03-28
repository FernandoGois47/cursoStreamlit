import streamlit as st

st.text_input("Titulo do filme", "É o Brian!")

with st.container(height=300):
    st.markdown(long_text)
