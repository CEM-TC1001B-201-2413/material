import streamlit as st

pages = [
    st.Page("page/home.py", title="Inicio"),
    st.Page("page/data.py", title="Estudios previos"),
    st.Page("page/form.py", title="Encuesta"),
    st.Page("page/results.py", title="Resultados obtenidos")
    ]

pg = st.navigation(pages)

pg.run()