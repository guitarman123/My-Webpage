import streamlit as st
import random

st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

number = random.randint(1, 100)
st.title('Number Guessing Game!')
st.write('Use the slider to choose a number and press check see if you\'re right')
user_choice = st.slider('Pick a number', 0, 100)
pressed = st.button('check')
if pressed:
    if user_choice == number:
        st.write('You guessed the number!')
    elif user_choice > number:
        st.write('Too big guess a smaller number.')
    elif user_choice < number:
        st.write('Too small guess a bigger number.')