import streamlit as st
import pandas as pd
import numpy as np

st.title('Hello, Streamlit!')
st.write('Welcome to your first Streamlit app.')

# 간단한 데이터 입력 예제
user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Hello, {user_input}!")




