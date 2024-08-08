import streamlit as st

st.header("Text Page")
st.sidebar.button("PRess me")

col1, col2 = st.columns(2)
col2.header("col 2")
with col2:
  st.image("logos/microsoft_logo.png")

col1.header("Col 1")