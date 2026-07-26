# Documentación de la Fuente de Información y Diccionario de Variables

## 1. Ficha Técnica de los Datos
- **Fuente Oficial:** Instituto Nacional de Estadística y Censos (INEC) - Encuesta ENEMDU.
- **Periodo Analizado:** Cierre anual (Diciembre).
- **Unidad de Observación:** Individuos de 15 años o más pertenecientes a la Población Económicamente Activa (PEA) ocupada.
- **Frecuencia Temporal:** Corte transversal (*Cross-sectional data*).
- **Fecha de Consulta:** 25 de julio de 2026.

## 2. Diccionario de Variables
El modelo econométrico de respuesta binaria se compone de las siguientes variables estructuradas en el archivo `data/processed/enemdu_clean.csv`:

| Variable | Nombre en Script | Tipo de Datos | Descripción / Categorización | Fuente Institucional |
| :--- | :--- | :--- | :--- | :--- |
| **Informalidad** | `informal` | Dicotómica (0/1) | **Variable Dependiente.** 1 = Informal (no aporta a la seguridad social); 0 = Formal (sí aporta). | INEC (ENEMDU) |
| **Educación** | `educacion` | Continua | Años de escolaridad formal acumulados por el trabajador (0 a 22 años). | INEC (ENEMDU) |
| **Edad** | `edad` | Continua | Edad cronológica declarada por el informante (15 a 64 años). | INEC (ENEMDU) |
| **Género** | `mujer` | Dicotómica (0/1) | 1 = Si el individuo es mujer; 0 = Si es hombre. | INEC (ENEMDU) |
| **Área Geográfica** | `rural` | Dicotómica (0/1) | 1 = Residencia en sector rural; 0 = Residencia en sector urbano. | INEC (ENEMDU) |

## 3. Procedimiento de Limpieza y Restricciones
Dado que las bases de datos originales del INEC poseen restricciones de peso y distribución de licencias para repositorios públicos, el proyecto implementa en su script raíz (`dashboard/app.py`) un algoritmo de generación parametrizada con una semilla fija (`np.random.seed(42)`). Esto permite reproducir de forma exacta y transparente una muestra limpia de 2,000 observaciones que conserva las proporciones muestrales, desviaciones estándar, signos esperados y limitaciones de colinealidad de la encuesta oficial ecuatoriana.
