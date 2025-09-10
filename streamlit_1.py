import streamlit as st
import time

st.header('Shape Calculation')
side = st.sidebar
side.title('Shape Selecting')

with side:
    shape = st.selectbox('Choose shape :' , ['Shapes' , 'Circle' , 'Rectangle'])
    area = None
    premiter = None


if shape == 'Circle':
    radius = st.number_input('Radius :' , min_value=0.0 , max_value=100.0  , step = 1.0)
    area = radius ** 2 * 3.14
    premiter = 2*radius*3.14


elif shape == 'Rectangle':
    width = st.number_input('Width :' , min_value=0.0 , max_value=100.0 , step=1.0)
    length = st.number_input('lexngth :' , min_value=0.0 , max_value=100.0 , step=1.0)
    area =  width*length
    premiter = (width+length)*2

compute_btn = st.button('Compute area and premiter')

with st.spinner('Computing...'):
    if compute_btn:
        time.sleep(1)
        st.success(f'Area : {area}')
        st.success(f'Premiter : {premiter}')

