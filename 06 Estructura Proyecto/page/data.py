import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos(nombre_archivo):
    df = pd.read_csv(nombre_archivo)
    return df

df_actores = cargar_datos("data/Actores.csv")
df_mapa = cargar_datos("data/municipios_edomex.csv")

st.title("Estudios previos")

st.write("Praesent risus velit, finibus in convallis sed, fringilla faucibus enim. Vestibulum quis est vitae ante accumsan gravida. Curabitur placerat nunc at massa semper ullamcorper. Donec ornare risus non ante dapibus eleifend. Cras eu augue quis nisi pellentesque facilisis vel ac mi. Nullam mollis pharetra mollis. Nunc ullamcorper et mi sed ultricies. Ut sit amet nisi semper felis porta semper. Vivamus tincidunt nunc eu lobortis venenatis. Praesent feugiat bibendum lectus, ac congue velit laoreet eu. Pellentesque vel libero ipsum. Morbi at mollis est, at gravida eros. Pellentesque in euismod dolor. Ut et magna enim. Mauris ut lacinia lectus. In faucibus purus vel libero maximus pellentesque quis nec turpis.")

st.dataframe(df_actores.head(20))
st.caption("Tomado de: http://www.google.com")

st.bar_chart(df_actores, x="Actores", y="Nivel de relevancia")

c1, c2, c3 = st.columns(3)

c1.metric("Gobierno Federal", "40%", "5%")
c2.metric("Sector Privado", "10%", "-3%")
c3.metric("Sindicatos", "15%", "1%")

st.map(df_mapa,
       latitude="Latitud",
       longitude="Longitud",
       color="Representatividad")



