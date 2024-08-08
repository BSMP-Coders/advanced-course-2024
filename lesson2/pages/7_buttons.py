import streamlit as st

st.title("This is the Button webpage")
st.write("hi")

button1 = st.button("Button1")

if button1:
  st.write("hey you clicked button1")
  button1 = st.empty()

like = st.checkbox("do you like this app?")
button2 = st.button("like Submitt")

if button2:
  if like:
    st.write("Thanks for liking the app!")
  else:
    st.write("ahh sorry you didn like this app, well do betting next time")


### header 2 multi
st.header("mutli select")
animals = st.radio("What is your fav animal?", ("Cat", "Dog","Bird"))
animals2 = st.multiselect("What is your fav animal?", ("Cat", "Dog","Bird"))
button3 = st.button("Print Action for Animal")
if button3:
  if animals2 == ["Dog"]:
    st.write("woof woof")
  elif animals2 == ["Dog", "Cat"]:
    st.write("dogs vs cats")
  
