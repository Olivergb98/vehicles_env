import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('vehicles_us.csv')  # importar df
car_data.columns = car_data.columns.str.strip()  # limpiar nombres de columnas

st.title('Vehículos y sus gráficas')  # Título
st.header('Histograma')
st.write('Marca la siguiente casilla para contruir un histograma sobre el odómetro de los vehículos')

build_histogram = st.checkbox('Construir un histograma')

if build_histogram:  # si la casilla de verificación está seleccionada
    st.write('Construcción de un histograma para la columna odómetro')
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Creación del botón de la gráfica de dispersión

st.header('Gráfico de dispersión')
st.write('Pulsa el botón para crear un gráfico de dispersión del odómetro')

build_scatter = st.button('Construir un gráfico de dispersión')

if build_scatter:
    st.write('Construcción de un gráfico de dispersión para la columna odómetro')
    # usando el precio como referencia
    sfig = px.scatter(car_data, x="odometer", y="price")

    # mostrar scatter
    st.plotly_chart(sfig, use_container_width=True)
