import streamlit as st
import random

st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

st.title('Number Guessing Game!')
st.write('Use the slider to choose a number and press check see if you\'re right')
user_choice = st.slider('Pick a number', 0, 100)