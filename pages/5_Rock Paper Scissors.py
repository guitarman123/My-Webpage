import streamlit as st
import random

st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

def game():
    user_choice = st.selectbox("Choose your move:", ["Rock", "Paper", "Scissors"])

    if st.button('Play'):
        computer = random.choice('Rock','Paper','Scissors')
        if computer == user_choice:
            st.write('Tie')
        elif computer == 'Rock' and user_choice == 'Paper':
            st.write('You win!')
        elif computer == 'Paper' and user_choice == 'Scissors':
            st.write('You win!')
        elif computer == 'Scissors' and user_choice == 'Rock':
            st.write('You win!')

        else:
            st.write('You lost!')
game()