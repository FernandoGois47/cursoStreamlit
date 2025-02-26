import streamlit as st
st.header("Bem Vindo ao mundo mágico do Gois")
"Toquem no botão para não salvar 👇"
st.button("Botão Salvar")
st.text_input("Movie title", "Life of Brian")
st.toggle("Toggle")

genre = st.radio(
  "Ta bonito? 👇",
  ["Ééééé....", "Meio boca", "Pagar uma caixa de chocolate"],
    )

options = ["gato", "sapo", "cama", "bala", "rato", "pijama", "dança", "cueca"]
selection = st.pills("Frase do dia", options, selection_mode="multi")
st.markdown(f"Sua frase é: {selection}.")


st.text_area("Escreva aqui tudo o que você acha de vc...")
