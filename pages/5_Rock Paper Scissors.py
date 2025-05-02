import streamlit as st
import random
import secrets

st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

st.title('Rock, Paper, Scissors!')
st.write('See if you can beat the computer in a game of rock, paper, scissors')

def game():
    rps = ['Rock','Paper', 'Scissors']
    user_choice = st.selectbox("Choose your move:", ["Rock", "Paper", "Scissors"])

    if st.button('Play'):
        computer = secrets.choice(rps)
        st.write(f'You chose {user_choice}.')
        st.write(f'Computer chose {computer}.')
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