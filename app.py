import pandas as pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go
import streamlit as st

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

print(car_data.head())
print(car_data.info())


# Se agrega encabezado
st.header("Venta de coches", divider=True)

# Declaración del boton de histograma
hist_button = st.button('Construcción histograma')

# Lógica  del botón para histograma
if hist_button:

    st.header("Histograma", divider=True)

    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de modelos de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['model_year'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución de los modelos de carros')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)

# Declaración del boton de grafico de dispersión
dis_button = st.button('Construcción gráfico de dispersión')

if dis_button:

    st.header("Gráfico de dispersion", divider=True)

    st.write(
        ' Creación de un grafico de disperión para ver la relación '
        'ente modelos de carros y su precio')

    # Creación del grafico de dispersion
    fig = go.Figure(
        data=[go.Scatter(x=car_data['model_year'], y=car_data['price'], mode='markers')])

    # Agrega titulo de grafico de dispersion
    fig.update_layout(title_text='Grafico de dispersion')

    # Muestra de grafico de dispersion
    st.plotly_chart(fig, use_container_width=True)
