import streamlit as st
import random

st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

def game():
    user_choice = st.selectbox("Choose your move:", ["Rock", "Paper", "Scissors"])

    if st.button('Play'):
        computer = random.choice('r','p','s')
        if computer == user_choice:
            st.write('Tie')
        elif computer == 'r' and user_choice == 'p':
            st.write('You win!')
        elif computer == 'p' and user_choice == 's':
            st.write('You win!')
        elif computer == 's' and user_choice == 'r':
            st.write('You win!')

        else:
            st.write('You lost!')
game()