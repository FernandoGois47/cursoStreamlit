import streamlit as st

st.title("Aluno")

A, B = st.columns(2)
st.subheader("Editar Dados")
with A:
title = st.text_input("Nome Completo")
