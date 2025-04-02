import streamlit as st
import datetime

st.title("Funcionario")



st.subheader("Editar Dados")
nome = st.text_input("Nome")
sobrenome = st.text_input("Sobrenome")

niver = st.date_input("Qual sua data de nascimento", datetime.date.today())

estadocivil = st.selectbox(
  "Estado Civil:",
  ("Solteiro", "Casado", "Divorciado", "Viúvo"),
)
sexo = st.selectbox(
  "Sexo:",
  ("Masculino", "Feminino", "Outros"),
)
salario = st.number_input("Qual seu salário")

if salario >= 2500:
  st.write("Noooosssaaa, vai rola aumento! Parabéns!")
aumento = 0
i = 0
for i in range(100,500):
  salario = aumento + 100
print(f'Salário {salario}')

else:
  st.write("Não foi dessa vez")




