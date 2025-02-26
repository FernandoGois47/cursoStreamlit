import streamlit as st
st.header("Bem Vindo ao mundo mágico do Gois")
"Toquem no botão para não salvar 👇"
st.button("Botão Salvar")
st.text_area("Enter Text")
st.text_input("Movie title", "Life of Brian")
st.toggle("Toggle")

st.radio(
  "Ta bonito? 👇",
  ["Ééééé....", "Meio boca", "Pagar uma caixa de chocolate"],
  key="visibility",
  label_visibility=st.session_state.visibility,
  disabled=st.session_state.disabled,
  horizontal=st.session_state.horizontal,
    )
