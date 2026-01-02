# importaciones
import streamlit as st
import pandas as pd
import plotly.graph_objects as pltgo

# lectura del csv dataframe 
df_cars = pd.read_csv('datasets/vehicles_us.csv')

st.header('Análisis Exploratorio de Datos de Vehículos')

# Mostrar el dataframe (opcional, puedes descomentarlo)
# st.write('### Listado de vehículos')
# st.dataframe(df_cars.head())

st.write('Selecciona las gráficas que deseas visualizar:')

# Crear casillas de verificación (checkbox)
build_histogram = st.checkbox('Mostrar Histograma')
build_scatter = st.checkbox('Mostrar Gráfico de Dispersión')

# Lógica para el Histograma
if build_histogram:
    st.write('### Creación del histograma: Año vs. Cantidad')
    fig = pltgo.Figure(data=[pltgo.Histogram(
        x=df_cars['model_year'],
        marker_color='#3366CC',
        marker_line=dict(width=1, color='white'),
        opacity=0.75
    )])
    
    fig.update_layout(
        title_text='Distribución del año del modelo',
        xaxis_title='Año del modelo',
        yaxis_title='Cantidad de vehículos',
        title_x=0.5,
        template='plotly_white'
    )
    st.plotly_chart(fig, use_container_width=True)

# Lógica para la Dispersión
if build_scatter:
    st.write('### Creación de dispersión: Año del Modelo vs. Precio (USD)')
    fig_disp = pltgo.Figure(data=[pltgo.Scatter(
        x=df_cars['model_year'],
        y=df_cars['price'],
        mode='markers',
        marker=dict(
            size=7,
            color=df_cars['price'], 
            colorscale='Viridis',
            showscale=True,
            opacity=0.5
        )
    )])
    
    fig_disp.update_layout(
        title_text='Relación entre Año del Modelo y Precio',
        xaxis_title='Año del Modelo',
        yaxis_title='Precio (USD)',
        title_x=0.5,
        template='plotly_white'
    )
    st.plotly_chart(fig_disp, use_container_width=True)