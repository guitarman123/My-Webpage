import streamlit as st


st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

#write anything
with st.container():
    st.title('Hey! Welcome to My Website')
    st.subheader('This page is still in progress but '
                 'it will have links to some of my other '
                 'projects.')
    st.title('In progress.')
    st.write('still working on it.')
    st.write('Click the arrow at the top left to open all of the pages.')
    #st.write('[this is marty music >](https://www.martymusic.com/)')

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
    image_column, text_column2 = st.columns((1, 2))
    #with image_column:
        #insert image
    with  text_column2:
        st.subheader('blank')
        st.write('''
        1
        2
        3
        4
        5'''
        )
        #st.markdown("[marty's back in black](https://www.youtube.com/watch?v=VCyM7tjz2YA)")







