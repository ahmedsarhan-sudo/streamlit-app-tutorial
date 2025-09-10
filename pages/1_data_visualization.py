import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import random as rd
import re

@st.cache_data
def data_load(file):
    if file.name.endswith('.xlsx'):
        df = pd.read_excel(file)
        return df
    
    elif file.name.endswith('.csv'):
        df = pd.read_csv(file)
        return df
    

file = st.file_uploader('Upload file' , type=['xlsx' , 'csv'])

if file != None:
    
    df = data_load(file=file)


    default_columns = st.session_state

    if 'columns_selected' not in default_columns:
        default_columns['columns_selected'] = df.columns.tolist()


    columns_to_show = st.multiselect('Select columns to show : ' ,options= df.columns ,
                                        default= default_columns['columns_selected'])


    columns_remove_btn = st.button('Remove all columns')

    if columns_remove_btn:
        default_columns['columns_selected'] = []
        st.rerun()


    columns_recolumns_btn = st.button('Return all columns')

    if columns_recolumns_btn:
        default_columns['columns_selected'] = df.columns.tolist()
        st.rerun()


    rows_to_show = st.slider('Choose number of rows to display :' , min_value=5 ,
                max_value=df.shape[0])
    
    st.dataframe(df[:rows_to_show][columns_to_show])


    columns_numirec = df.select_dtypes('number').columns.tolist()

    

    tab_1,tap_2,tap_3 = st.tabs(tabs = ['Scatter' ,'Histogram' , 'Client Details'])

    with tab_1:

        col_1,col_2 = st.columns(2)
        col_3,col_4 = st.columns(2)
        
        with col_1:
            axis_x_scatt = st.selectbox('Select column to be axis \'x\' for scatter' , options=columns_numirec)
        with col_2:
            color_scatt = st.selectbox('Select column to be color for scatter' , options=columns_numirec)
        with col_3:
            size_scatt = st.selectbox('Select column to be size for scatter' , options=columns_numirec)
        with col_4:
            color_map = st.selectbox('Color Maps Style' , options=['plasma', 'rainbow' , 'viridis'])


        size_over = st.selectbox('Size of colomn' , options=[20,40,10])

        
        if st.button('Show the diagram.'):
            try:
                fig_scatter = px.scatter(
                df ,
                axis_x_scatt ,
                color=color_scatt ,
                size=size_scatt ,
                size_max=size_over,
                color_continuous_scale=color_map
                )
                    
                fig_scatter.update_layout(
                    yaxis_title = 'Count'
                )

                st.plotly_chart(fig_scatter)

            except:
                st.warning('Size cannot be negative.')
                
                st.warning(f'{size_scatt} : Have a negative value.')


    with tap_2:
        axis_x_hist = st.selectbox('Select column to be axis \'x\' for histogram' , options=columns_numirec)

        fig_histogram = px.histogram(df , axis_x_hist )
        st.plotly_chart(fig_histogram)


    with tap_3:

        col_5,col_6 = st.columns(2)
        
        with col_5:
            
            index = st.number_input('Enter Index' ,min_value = 0 , max_value=df.shape[0] , step=1)
            show_client = st.button('Show Client')
            if show_client:
                st.write(df.iloc[index])

    

