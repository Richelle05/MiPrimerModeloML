import streamlit as st
import joblib
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Iris Classifier", page_icon="🌸")

# Título y descripción
st.title("🌸 Clasificador de Flores Iris")
st.write("Usa este aplicativo para probar tus modelos entrenados (KNN y SVM).")

# Función para cargar los modelos
@st.cache_resource
def load_model(model_path):
    return joblib.load(model_path)

# Barra lateral para selección de modelo
st.sidebar.header("Configuración")
model_option = st.sidebar.selectbox(
    "Selecciona el modelo que deseas usar:",
    ("KNN", "SVM")
)

# Cargar el modelo seleccionado
# Cargar el modelo seleccionado
if model_option == "KNN":
    # Agrega 4 espacios (o un Tab) al inicio de la siguiente línea:
    model = load_model("modelo_iris_knn.pkl") 
else:
    # También esta línea debe llevar 4 espacios al inicio:
    model = load_model("modelo_iris_svm.pkl")

# Interfaz de entrada de datos (Características de Iris)
st.subheader("Entrada de Datos")
col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider("Longitud del Sépalo (cm)", 4.0, 8.0, 5.4)
    sepal_width = st.slider("Ancho del Sépalo (cm)", 2.0, 4.5, 3.4)

with col2:
    petal_length = st.slider("Longitud del Pétalo (cm)", 1.0, 7.0, 1.3)
    petal_width = st.slider("Ancho del Pétalo (cm)", 0.1, 2.5, 0.2)

# Botón de predicción
if st.button("Clasificar"):
    # Preparar los datos para el modelo
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    
    # Realizar la predicción
    prediction = model.predict(input_data)
    
    # Mapeo de nombres de las especies (ajusta según tu entrenamiento)
    # Por defecto en Iris: 0: Setosa, 1: Versicolor, 2: Virginica
    species_names = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    result = species_names.get(prediction[0], f"Clase {prediction[0]}")

    # Mostrar resultado con animación
    st.balloons()
    st.success(f"El modelo {model_option} predice que la especie es: **{result}**")

# Información técnica
st.divider()
st.caption("Asegúrate de que los archivos .pkl estén en la raíz de tu repositorio de GitHub.")
