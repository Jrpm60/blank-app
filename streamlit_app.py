import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import time

st.title(" Aprendiendo Strem Lit")

st.write("Hola")
st.button ("reset", type="primary")

if st.button("Hola"):
    if st.button("quieres contuniuar"):
        st.write("hola")

with st.sidebar:
    st.write("Esta informacion aparecera a la izquierda")
    if st.button("quieres contuniuar"):
        st.write("hola")