import streamlit as st  # Importa Streamlit para crear el dashboard.

st.title("Análisis de distancias")  # Muestra el título del dashboard.
st.write("Bienvenido al primer dashboard")  # Muestra un mensaje de bienvenida.

distancia = st.slider("Seleccione una distancia en cm", 0, 50, 20)  # Crea un control para elegir una distancia entre 0 y 50 cm.
st.write("Distancia seleccionada:", distancia)  # Muestra la distancia elegida.

if distancia < 20:  # Comprueba si la distancia elegida es menor que 20 cm.
    st.write("Objeto cerca")  # Muestra este mensaje si la distancia es menor que 20 cm.
else:  # Se ejecuta si la distancia es 20 cm o más.
    st.write("Distancia segura")  # Muestra este mensaje si la distancia es segura.