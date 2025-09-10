import streamlit as st

text_list = []

user_input = st.text_input('Enter some text')

if st.button('Append'):
    text_list.append(user_input)

if st.button('Clear'):
    text_list = []

st.write(text_list)

