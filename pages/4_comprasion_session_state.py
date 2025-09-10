import streamlit as st

if 'text_list' not in st.session_state:
    st.session_state['text_list'] = []

user_input = st.text_input('Enter some text')

if st.button('Append'):
    st.session_state['text_list'].append(user_input)

if st.button('Clear'):
    st.session_state['text_list'] = []

st.write(st.session_state)

