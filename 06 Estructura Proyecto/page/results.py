import pandas as pd
import streamlit as st

def cargar_datos():
    df = pd.read_csv("data/encuesta.csv")
    return df

df = cargar_datos()

st.title("Resultados de nuestro estudio")

st.write("Aquí va un texto que hable de su propio estudio y de los resultados esperados.")

st.dataframe(df.tail(20))