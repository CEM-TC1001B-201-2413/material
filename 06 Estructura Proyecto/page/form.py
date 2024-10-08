import streamlit as st

st.title("Instrumento de medición")

form = st.form("formulario")

nombre = form.text_input("Nombre")

edad = form.number_input("Edad",
                         min_value=18,
                         max_value=100,
                         value=20)

opciones_sexo = ["Hombre", "Mujer", "Prefiero no decir"]
sexo = form.radio("Sexo", opciones_sexo)

estados_mexico = [
    "Aguascalientes",
    "Baja California",
    "Baja California Sur",
    "Campeche",
    "Chiapas",
    "Chihuahua",
    "Coahuila",
    "Colima",
    "Durango",
    "Guanajuato",
    "Guerrero",
    "Hidalgo",
    "Jalisco",
    "Mexico",
    "Michoacán",
    "Morelos",
    "Nayarit",
    "Nuevo León",
    "Oaxaca",
    "Puebla",
    "Querétaro",
    "Quintana Roo",
    "San Luis Potosí",
    "Sinaloa",
    "Sonora",
    "Tabasco",
    "Tamaulipas",
    "Tlaxcala",
    "Veracruz",
    "Yucatán",
    "Zacatecas",
    "Otro Páis"
]

estado = form.selectbox("Estado de la república",
                        estados_mexico)

otro_estado = form.text_input("Otro")

form.write("Selecciona las opciones que apliquen")
cocacola = form.checkbox("Coca Cola")
sprite = form.checkbox("Sprite")
squirt = form.checkbox("Squirt")
fanta = form.checkbox("Fanta")

form.write("Selecciona las opciones que has ingerido")
alcohol = form.toggle("Alcohol")
tabaco = form.toggle("Tabaco")

conformidad = form.slider("¿Qué tan conforme estás?",
                          min_value=0,
                          max_value=10,
                          value=5)

nacimiento = form.date_input("¿Cuándo naciste?")

tiempo = form.time_input("Hora de registro")

submit = form.form_submit_button("Enviar respuesta")

if submit:
    encuesta_df = pd.read_csv("data/encuesta.csv")
    # Pares con:
    # "Nombre de la columna en archivo": variable
    if estado == "Otro Opción":
        estado_seleccionado = otro_estado
    else:
        estado_seleccionado = estado
    nueva_fila = pd.DataFrame([{
        "Nombre": nombre,
        "Edad": edad,
        "Sexo": sexo,
        "Estado", estado_seleccionado,
        "Coca Cola": cocacola,
        "Sprite": sprite,
        "Squirt": squirt,
        "Fanta": fanta,
        "Alcohol": alcohol,
        "Tabaco": tabaco,
        "Conformidad": conformidad,
        "Fecha de nacimiento": nacimiento,
        "Hora de registro": tiempo
        }])
    encuesta_df = pd.concat([encuesta_df, nueva_fila],
                            ignore_index=True)
    encuesta_df.to_csv("data/encuesta.csv", index=False)
    st.success("Registro guardado")
    
    
    
    
    
    
    
    

