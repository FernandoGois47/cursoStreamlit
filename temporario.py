import streamlit as st
st.header("Bem Vindo ao mundo mágico do Gois")
"Toquem no botão para não salvar 👇"
st.button("Botão Salvar")
st.text_input("Movie title", "Life of Brian")
st.toggle("Toggle")
st.text_area("Escreva aqui tudo o que você acha de vc...")
genre = st.radio(
  "Ta bonito? 👇",
  ["Ééééé....", "Meio boca", "Pagar uma caixa de chocolate"],
    )

sujeitos = ["O gato", "O sapo", "O rato", "A cueca"]
verbos = ["dança", "pula", "come", "fugiu"]
complementos = ["na cama", "com o pijama", "a bala", "do sapo"]
selection = st.pills("Frase do dia", options, selection_mode="multi")
st.markdown(f"Sua frase é: {selection}.")



