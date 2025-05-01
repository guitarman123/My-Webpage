import streamlit as st


st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

#write anything
with st.container():
    st.title('Hey! Welcome to My Website')
    st.subheader('This page is still in progress but '
                 'it will have links to some of my other '
                 'projects.')
    st.write('Click the arrow at the top left to open all of the pages.')

#more
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.header('what this is for')
        st.write('##')
        st.write('''
        This is a website where I will post my python projects and other miscellaneous things .''')

with st.container():
    st.write('---')
    st.header('My Projects')
    st.write('##')







