import streamlit as st
import pandas as pd

@st.cache_data
def cargar_datos():
    df = pd.read_csv("goal15.forest_shares.csv")
    return df

df = cargar_datos()

st.title("Mi primera página")

st.header("Encabezado")

st.subheader("Sub-encabezado")

st.write("Ejemplo de mi primera página")

# Markdown

st.markdown("""
# Título
## Subtítulo
### Subsubtítulo

Lista ordenada:
1. Elemento uno
2. Elemento dos
3. Elemento tres

---

Lista no ordenada:
- Elemento uno
- Elemento dos
- Elemento tres

Estamos aprendiendo a usar *streamlit* :sunglasses:.

""")

st.dataframe(df.head(5))
st.caption("Tomado de: https://www.kaggle.com/datasets/konradb/deforestation-dataset")

st.image("images.jpg")
st.caption("Tomado de: https://www.pexels.com/photo/bird-s-eye-view-of-woodpile-1268076/")

st.video("https://www.youtube.com/watch?v=erERY_IgtzI")
st.caption("Tomado de: https://www.youtube.com/watch?v=erERY_IgtzI")