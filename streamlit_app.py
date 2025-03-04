import streamlit as st
from pages.page_1 import func_page_1
from pages.page_2 import func_page_2
from pages.page_3 import func_page_3

def main():
    st.sidebar.subheader('Page selection')
    page_selection = st.sidebar.selectbox('Please select a page',['Main Page',
    'Page 1','Page 2','Page 3'])
    pages_main = {
        'Main Page': main_page,
        'Page 1': run_page_1,
        'Page 2': run_page_2,
        'Page 3': run_page_3
    }

    # Run selected page
    pages_main[page_selection]()

def main_page():
    st.title('Main Page')
def run_page_1():
    func_page_1()
def run_page_2():
    func_page_2()
def run_page_3():
    func_page_3()

if __name__ == '__main__':
    main()