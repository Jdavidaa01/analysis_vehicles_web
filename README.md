# Proyecto: Análisis Exploratorio de Datos de Vehículos (EDA) 🚗💨

Este proyecto es una aplicación web interactiva diseñada para analizar anuncios de venta de coches en EE. UU. Utiliza herramientas de ciencia de datos para visualizar tendencias de precios basadas en el año del modelo y el kilometraje.

## 🔗 Enlace al Repositorio
[https://github.com/Jdavidaa01/analysis_vehicles_web](https://github.com/Jdavidaa01/analysis_vehicles_web)

## 🌐 Aplicación en Vivo (Render)
[https://analisis-exploratorio-vehiculos.onrender.com/]
(https://analisis-exploratorio-vehiculos.onrender.com/)
---

## 📋 Descripción
La aplicación permite filtrar y visualizar datos de forma dinámica mediante el uso de casillas de verificación (checkboxes). El objetivo es facilitar la comprensión de cómo factores como la antigüedad del vehículo afectan su valor de mercado.

### 🛠️ Stack Tecnológico
* **Lenguaje:** Python 3.10+
* **Framework Web:** Streamlit
* **Visualización:** Plotly Graph Objects (interactividad avanzada)
* **Procesamiento de Datos:** Pandas

---

## 📊 Funcionalidades Principales
* **Histogramas Interactivos:** Análisis de la frecuencia de vehículos por año de fabricación.
* **Gráficos de Dispersión:** Correlación entre el año del modelo y el precio de venta con escalas de color (Viridis).
* **Interfaz de Usuario:** Uso de `st.checkbox` para visualizaciones múltiples simultáneas.

---

## 🚀 Instalación y Ejecución Local

1. **Clonar el proyecto:**
   ```bash
   git clone [https://github.com/Jdavidaa01/analysis_vehicles_web.git](https://github.com/Jdavidaa01/analysis_vehicles_web.git)
   cd analysis_vehicles_web
   ```
2. **Configurar entorno virtual**
```bash
python -m venv vehicles_env
source vehicles_env/Scripts/activate  # En Windows use: vehicles_env\Scripts\activate
```
3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```
4. **Ejecutar app**
```bash
streamlit run app.py
```
_ _ _
📁 Estructura del Proyecto

* app.py: Código fuente de la aplicación Streamlit.

* datasets/: Contiene el archivo fuente vehicles_us.csv.

* notebooks/: Cuadernos de Jupyter para experimentación previa.

* requirements.txt: Librerías necesarias para el despliegue en la nube.