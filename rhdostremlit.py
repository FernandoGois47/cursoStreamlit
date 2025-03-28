import streamlit as st
import datetime


with st.container(True):
st.title("Funcionario")

A, B = st.columns(2)

with A:
  st.subheader("Editar Dados")
  nome = st.text_input("Nome")
  sobrenome = st.text_input("Sobrenome")

  d = st.date_input("Qual sua data de nascimento", datetime.date(2025, 28, 3))

  estadocivil = st.selectbox(
    "Estado Civil:",
    ("Solteiro", "Casado", "Divorciado", "Viúvo"),
  )
  sexo = st.selectbox(
    "Sexo:",
    ("Masculino", "Feminino", "Outros"),
  )

with B:
  salario = st.number_input("Qual seu salário")
