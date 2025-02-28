import streamlit as st
import datetime

st.title("Aluno")

A, B = st.columns(2)

with A:
  st.subheader("Editar Dados")
  title = st.text_input("Nome Completo")
  title = st.text_input format="MM.DD.YYYY" ("Data de Nascimento:")
  

  st.selectbox(
    "Sexo:",
    ("Masculino", "Feminino", "Outros"),
  )

  title = st.text_input("RG:")
  title = st.text_input("Nome do Pai:")
  title = st.text_input("Nome do Mãe:")
  title = st.text_input("E-mail:")

with B:
  st.subheader(" ")
  title = st.text_input("Logradouro:")
  title = st.text_input("Número:")
  title = st.text_input("Bairro:")
  title = st.text_input("CEP:")
