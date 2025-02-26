import streamlit as st
st.header("Bem Vindo ao mundo mágico do Gois")
st.text_input("Titulo do filme", "É o Brian!")
modo_carnaval = st.toggle("Modo Carnaval")
if modo_carnaval:
    st.write("🎉🎶")
    st.balloons()  # Efeito de balões para comemorar!
else:
    st.write("Modo Carnaval desativado. Que pena! 😢")
  
st.text_area("Escreva aqui tudo o que você acha de vc...")
genre = st.radio(
  "Ta bonito? 👇",
  ["Ééééé....", "Meio boca", "Pagar uma caixa de chocolate"],
    )

st.selectbox(
  "Qual sua cor menos favorita?",
  ("Sanduiche", "Macarrão", "Vermelho"),
)

"Marque seu heroi favorito"
st.checkbox("Capitão caverna")
st.checkbox("Homem Sereia")
st.checkbox("Homem cueca")




"Toquem no botão para não salvar 👇"
st.button("Botão Salvar")


