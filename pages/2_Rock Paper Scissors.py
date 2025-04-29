import random

import streamlit as st


st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

choices = ('r', 'p', 's')


while True:
    user_input = st.text_input('Rock, Paper, or Scissors? (r/p/s): ').lower()


#player's choice
    if user_input == 'r':
        st.write('You chose 🧱')
    elif user_input == 'p':
        st.write('You chose 📄')
    elif user_input == 's':
        st.write('You chose ✂')
    elif user_input not in choices:
            st.write('Invalid choice')
            continue

#computer's choice
    computers_rps = ['🧱', '📄', '✂']
    computer_choice = random.choice(computers_rps)
    st.write(f'Computer chose {computer_choice}')


#see if player or computer won

#handles ties
    if user_input == 'r' and computer_choice == '🧱':
        st.write('Tie!')
    if user_input == 'p' and computer_choice == '📄':
        st.write('Tie!')
    if user_input == 's' and computer_choice == '✂':
        st.write('Tie!')

#handles player wins
    if user_input == 'r' and computer_choice == '✂':
        st.write('You win!')
    if user_input == 'p' and computer_choice == '🧱':
        st.write('You win!')
    if user_input == 's' and computer_choice == '📄':
        st.write('You win!')

#handles computer wins
    if user_input == 'r' and computer_choice == '📄':
        st.write('You lose!')
    if user_input == 'p' and computer_choice == '✂':
        st.write('You lose!')
    if user_input == 's' and computer_choice == '🧱':
        st.write('You lose!')

    should_continue = text_input('Continue? (y/n): ').lower()
    if should_continue == 'n':
        break

