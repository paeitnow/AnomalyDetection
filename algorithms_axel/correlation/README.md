# Correlation

En esta carpeta se encuentran algoritmos dedicados al cálculo de la correlación entre diferentes conjuntos de datos. La correlación mide el grado en que dos variables están relacionadas.

## Contenido de la carpeta

### 1. `pearson_correlation.py`

Este script calcula la correlación de Pearson, una medida de correlación lineal entre dos conjuntos de datos. Un valor cercano a 1 indica una fuerte correlación positiva, mientras que un valor cercano a -1 indica una fuerte correlación negativa.

#### Descripción:
- **Entrada:** Dos listas de datos numéricos.
- **Salida:** Un valor entre -1 y 1 que representa la correlación entre los dos conjuntos de datos.

### 2. `spearman_correlation.py`

Este archivo implementa el cálculo de la correlación de Spearman, que mide la relación monotónica entre dos conjuntos de datos. A diferencia de la correlación de Pearson, Spearman no requiere que la relación sea lineal.

#### Descripción:
- **Entrada:** Dos listas de datos numéricos.
- **Salida:** Un valor entre -1 y 1 que representa la correlación de Spearman.

## Aplicaciones

- **Análisis de variables:** para estudiar la relación entre diferentes variables en ciencia, economía, etc.
- **Modelado predictivo:** para evaluar cómo se correlacionan los predictores con las respuestas observadas.
