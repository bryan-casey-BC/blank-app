import streamlit as st
def func_page_1():
    st.title('Page 1')
st.set_page_config(

    page_title='Hello world',
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Hello world**'
        }
)
st.sidebar.title('Hello world')
st.title('Hello world')