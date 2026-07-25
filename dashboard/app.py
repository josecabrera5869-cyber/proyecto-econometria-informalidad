import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard Econométrico", layout="wide")

st.title("📊 Determinantes de la Informalidad Laboral en Ecuador")
st.markdown("### Modelo de Respuesta Binaria - Proyecto Final de Econometría Aplicada")

st.sidebar.header("⚙️ Simulación del Perfil del Trabajador")
educacion = st.sidebar.slider("Años de Escolaridad", 0, 22, 12)
edad = st.sidebar.slider("Edad del Trabajador", 15, 65, 35)
mujer = st.sidebar.selectbox("Género", ["Hombre", "Mujer"])
rural = st.sidebar.selectbox("Área de Residencia", ["Urbana", "Rural"])

is_mujer = 1 if mujer == "Mujer" else 0
is_rural = 1 if rural == "Rural" else 0

z = 1.482 - 0.118 * educacion - 0.019 * edad + 0.362 * is_mujer + 0.831 * is_rural
prob_informal = 1 / (1 + np.exp(-z))

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Probabilidad Estimada de Informalidad Laboral", value=f"{prob_informal:.2%}")
    if prob_informal > 0.5:
        st.error("⚠️ El perfil analizado presenta un alto riesgo de pertenecer al sector informal.")
    else:
        st.success("✅ El perfil analizado presenta una alta probabilidad de empleo formal regulado.")

with col2:
    fig, ax = plt.subplots(figsize=(5, 3))
    colors = ['#ff4b4b' if prob_informal > 0.5 else '#00cc96']
    ax.bar(["Informalidad"], [prob_informal], color=colors, width=0.4)
    ax.set_ylim(0, 1)
    ax.set_ylabel("Probabilidad")
    st.pyplot(fig)
