import streamlit as st
import datetime

st.title("Funcionario")

A, B = st.columns(2)

with A:
  st.subheader("Editar Dados")
  title = st.text_input("Nome")
  title = st.text_input("Sobrenome")

  d = st.date_input("Qual sua data de nascimento", datetime.date(2025, 28, 3))

  st.selectbox(
    "Estado Civil:",
    ("Solteiro", "Casado", "Divorciado", "Viúvo"),
  )
  st.selectbox(
    "Sexo:",
    ("Masculino", "Feminino", "Outros"),
  )

with B:
