# Comparison

Esta carpeta contiene scripts dedicados a la comparación de diferentes series de datos. Los métodos de comparación pueden incluir métricas estadísticas, correlación cruzada, y otros enfoques para evaluar la similitud entre dos conjuntos de datos.

## Contenido de la carpeta

### 1. `cross_correlation.py`

Este script calcula la correlación cruzada entre dos series temporales. La correlación cruzada mide la similitud entre dos señales, considerando posibles desplazamientos (lags) entre ellas.

#### Descripción:
- **Entrada:** Dos listas de datos numéricos (series temporales) y el número de lags a analizar.
- **Salida:** Los valores de correlación cruzada para cada lag, indicando el nivel de similitud entre las series.

### 2. `mean_squared_error.py`

Este archivo implementa el cálculo del error cuadrático medio (MSE) entre dos conjuntos de datos. El MSE es una métrica que cuantifica la diferencia entre los valores predichos y los valores observados.

#### Descripción:
- **Entrada:** Dos listas de datos (valores predichos y valores observados).
- **Salida:** Un valor numérico que representa el MSE, donde un valor más bajo indica mayor similitud entre las dos series.

## Aplicaciones

- **Análisis comparativo:** para comparar el rendimiento de modelos predictivos con datos reales.
- **Procesamiento de señales:** para evaluar el alineamiento o desfase entre dos señales.
