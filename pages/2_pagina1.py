import streamlit as st

st.title("Pagina 1")

st.page_link("pages/1_pagina2.py", label="Ir a pagina 2")

number = st.number_input("Insert a number")
number2 = st.number_input("Insert a number 2")

res = (lambda x, y: x+y) (number,number2)

if res:
    st.write(res)



