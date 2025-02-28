import streamlit as st

st.title("_Streamlit_ é :blue[Legal] :sunglasses:")


st.button("Reset")

A, B, C = st.columns(3)

with A:
  st.header("Gatinho")
  st.image("https://jpimg.com.br/uploads/2025/01/10-curiosidades-sobre-os-filhotes-de-gato.jpg")
with A:
  st.header("Catchoro")
  st.image("https://denisemazzola.com/wp-content/uploads/Dog-Psychology.svg")
with A:
  st.header("Digimon")
  st.image("https://m.media-amazon.com/images/M/MV5BNjk1NTQ4NmEtZWM5MC00OTUwLTk2YTItOGU5OTVmNGEyNGNhXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg")
  
