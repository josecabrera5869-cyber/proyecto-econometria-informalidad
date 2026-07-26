# 📊 Análisis Microeconométrico de la Informalidad Laboral en Ecuador

Este proyecto aplica modelos de respuesta binaria no lineales para identificar los determinantes socioeconómicos que inciden en la probabilidad de que un trabajador pertenezca al sector informal en el Ecuador.

## 1. Problema Investigado
La informalidad laboral representa uno de los mayores desafíos estructurales del mercado de trabajo ecuatoriano, precarizando las condiciones de vida de la fuerza laboral. Este estudio delimita y evalúa el fenómeno analizando el peso relativo del capital humano, brechas de género y factores geográficos sobre la probabilidad de caer en la informalidad.

## 2. Fuente de Datos
Los microdatos provienen de la **Encuesta Nacional de Empleo, Desempleo y Subempleo (ENEMDU)** acumulada a diciembre, levantada de forma oficial por el Instituto Nacional de Estadística y Censos (INEC). La muestra considera a la Población Ocupada de 15 años o más. El diccionario detallado de variables se encuentra en `data/diccionario_variables.md`.

## 3. Modelo Econométrico
Se especifican y estiman modelos de respuesta binaria por Máxima Verosimilitud:
- **Modelo Logit:** Basado en una función de distribución logística.
- **Modelo Probit:** Basado en la distribución normal estándar acumulada.
La especificación estructural evalúa la probabilidad en función de los años de escolaridad, la edad cronológica, el género y el área geográfica de residencia.

## 4. Principales Resultados
Tras calcular los Efectos Marginales Promedio (AME), se identificaron los siguientes impactos críticos en la probabilidad:
- **Educación:** Reduce el riesgo de informalidad en **2.8 puntos porcentuales** por cada año de escolaridad adicional.
- **Género (Mujer):** Incrementa la probabilidad de incurrir en informalidad en un **8.6%** frente a los hombres.
- **Área Geográfica (Rural):** Incrementa la probabilidad en un **19.8%**, constituyendo el factor más penalizante debido a segmentaciones del mercado.

## 5. Estructura del Repositorio
```text
proyecto-econometria-informalidad/
├── .devcontainer/     # Configuración del entorno de desarrollo virtual
├── dashboard/         # Código fuente de la interfaz gráfica interactiva
│   └── app.py         # Aplicación del Dashboard en Streamlit
├── data/              # Almacenamiento de microdatos y documentación
│   └── diccionario_variables.md
├── notebooks/         # Cuadernos Jupyter de exploración y modelado
├── src/               # Scripts de procesamiento y estimación econométrica
├── LICENSE            # Licencia MIT de código abierto
├── README.md          # Presentación y documentación general del proyecto
└── requirements.txt   # Dependencias y librerías de Python requeridas
```

## 6. Procedimiento de Reproducción e Instalación
Para replicar el entorno de desarrollo y ejecutar el proyecto localmente sin depender de rutas absolutas:
1. Clone este repositorio público en su máquina local o ábralo en GitHub Codespaces.
2. Instale todas las dependencias y librerías econométricas necesarias ejecutando en su terminal:
   ```bash
   pip install -r requirements.txt
   ```
3. Para ejecutar y visualizar el Dashboard interactivo en su navegador, corra el siguiente comando:
   ```bash
   streamlit run dashboard/app.py
   ```

## 7. Enlaces del Proyecto
- **Repositorio de GitHub (Código Fuente):** https://github.com
- **Dashboard Interactivo (Aplicación en Vivo):** https://streamlit.app

---
*Nota: Este proyecto incluye en sus secciones del Minipaper impreso la respectiva **Declaración del uso de Inteligencia Artificial** en cumplimiento de los estándares de transparencia académica.*
