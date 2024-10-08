import streamlit as st

pages = [
    st.Page("page/home.py", title="Inicio"),
    st.Page("page/data.py", title="Estudios previos")
    ]

pg = st.navigation(pages)

pg.run()