import streamlit as st

st.title("Aluno")

A, B = st.columns(2)



with A:
  st.subheader("Editar Dados")
  title = st.text_input("Nome Completo")
