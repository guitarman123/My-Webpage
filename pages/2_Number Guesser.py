import streamlit as st
import random

st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

number = random.randint(0, 20)

while True:
    guess = st.number_input('Pick a number.', 0, 20)
    if guess == number:
        st.write('You guessed the number!')
    if guess < number:
        st.write('Too low.')
    if guess > number:
        st.write('Too high.')