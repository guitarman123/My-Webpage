import streamlit as st


st.set_page_config(page_title = 'K\'s Python Projects', page_icon = '🎸', layout = 'wide')

#write anything
with st.container():
    st.title('Song List')
    st.subheader('Here\'s a list of songs that I think would be fun to cover.')

#more
with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
        st.write('[I Won\'t Back Down - Tom Petty](https://music.youtube.com/watch?v=3efKaFVBcMU)')
        st.write('[Simple Man - Lynyrd Skynyrd](https://music.youtube.com/watch?v=l-5aPNxv-pU)')
        st.write('[When I Come Around - Green Day](https://music.youtube.com/watch?v=06HcqK2vvlw)')
        st.write('[1979 - Smashing Pumpkins](https://music.youtube.com/watch?v=A6M0yLxLCNA)')
        st.write('[Sweet Child O\' Mine - Guns N\' Roses](https://music.youtube.com/watch?v=oMfMUfgjiLg)')
        st.write('[Otherside - RHCP](https://music.youtube.com/watch?v=8901V1M5lDk)')
        st.write('[Paranoid - Black Sabbath](https://music.youtube.com/watch?v=xpM59e6lyws)')
        st.write('[Tuesday\'s Gone - Lynyrd Skynyrd](https://music.youtube.com/watch?v=iExsbDuVqeE)')
        st.write('[It\'s a Long Way To The Top (If You Wanna Rock and Roll) - AC/DC](https://music.youtube.com/watch?v=vj_rvLVpqg8)')
        st.write('[Learn to Fly - Foo Figthers](https://music.youtube.com/watch?v=HJMLLKgknvk)')
        st.write('[Times Like These - Foo Fighters](https://music.youtube.com/watch?v=EpRPOTh1KUg)')
        st.write('[Sunshine of Your Love - Cream](https://music.youtube.com/watch?v=y_u1eu6Lpds)')
        st.write('[Sweet Home Alabama - Lynyrd Skynyrd](https://music.youtube.com/watch?v=y_u1eu6Lpds)')
        st.write('[Soul to Squeeze - RHCP](https://music.youtube.com/watch?v=B72Q1uon78c)')
        st.write('[Back in Black - AC/DC](https://music.youtube.com/watch?v=9vWNauaZAgg)')
        st.write('[Free bird - Lynyrd Skynyrd](https://music.youtube.com/watch?v=CqnU_sJ8V-E)')
        st.write('[Scar Tissue - RHCP](https://music.youtube.com/watch?v=tpYdGgzCW-M)')
        st.write('[Seven Nation Army - White Stripes](https://music.youtube.com/watch?v=D_QLxj8jCF0)')
        st.write('[Life in The Fast Lane - Eagles](https://music.youtube.com/watch?v=po6QU0z1rSs)')
        st.write('[Smells Like Teen Spirit - Nirvana](https://music.youtube.com/watch?v=7TDeBi34OtE)')
        st.write('There\'s more I would like to cover but this is just a short list for starters'
                 ' and I\'ll add more some time.')
        st.write('If there are any bugs let me know.')

        st.write('##')
        #st.write('''
        #This is a website where I will post my python projects and other projects.''')

with st.container():
    st.write('---')
    #st.header('My Projects')
   ## st.write('##')
    #image_column, text_column2 = st.columns((1, 2))
    #with image_column:
        #insert image
    #with  text_column2:
        #st.subheader('blank')
        #st.write('''
        #1
        #2
        #3
        #4
        #5'''
        #)
        #st.markdown("[marty's back in black](https://www.youtube.com/watch?v=VCyM7tjz2YA)")