import streamlit as st
import secrets
import random

st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

st.title('Number guessing game.')
st.write('Use the slider below to pick a number then press check to see if your right!')


def game():
    user_choice = st.number_input('Pick a Number:', 1, 10)
    number = random.randrange(1, 10)
    
    if st.button('Check'):
        if user_choice == number:
            st.write('You win!')
        if user_choice > number:
            st.write(f'Too big!{number}')
        if user_choice < number:
            st.write(f'Too small!{number}')

game()