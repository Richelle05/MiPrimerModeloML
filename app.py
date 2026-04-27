import streamlit as st
import random
import time

# Configuración de página
st.set_page_config(page_title="Generador de Ecuaciones", page_icon="📝")

# Título con estilo
st.title("🎓 Desafío de Álgebra")
st.write("Resuelve la ecuación de primer grado y verifica tu resultado.")

# Inicializar variables de estado para mantener la ecuación al recargar
if 'a' not in st.session_state:
    st.session_state.a = random.randint(1, 10)
    st.session_state.b = random.randint(1, 20)
    st.session_state.x_true = random.randint(-10, 10)
    # Calculamos c para que la solución sea entera: c = ax + b
    st.session_state.c = st.session_state.a * st.session_state.x_true + st.session_state.b

# Mostrar la ecuación
st.subheader(f"Resuelve para $x$:")
st.latex(f"{st.session_state.a}x + {st.session_state.b} = {st.session_state.c}")

# Entrada del usuario
user_input = st.number_input("Introduce el valor de x:", step=1)

# Botón de verificación
if st.button("Verificar respuesta"):
    if user_input == st.session_state.x_true:
        st.balloons()  # Animación de éxito
        st.success(f"¡Correcto! El valor de $x$ es {st.session_state.x_true}.")
        time.sleep(2)
        # Resetear para una nueva ecuación
        for key in ['a', 'b', 'x_true', 'c']:
            del st.session_state[key]
        st.rerun()
    else:
        st.error("Respuesta incorrecta. ¡Inténtalo de nuevo!")

# Botón para generar otra nueva
if st.sidebar.button("Generar nueva ecuación"):
    for key in ['a', 'b', 'x_true', 'c']:
        del st.session_state[key]
    st.rerun()
