import streamlit as st
import random

st.title('Number Guessing Game')

HI = 10 
secret_number = random.randint(1, HI)

num_guesses = 0

guess = st.number_input('What is your guess?', value=10, step=1)
if guess:
  num_guesses += 1
    
  if guess > secret_number:
    st.write('Too high!')
  elif guess < secret_number:
    st.write('Too low!')
  else:
    st.write(f'You guessed it in {num_guesses} guesses!')