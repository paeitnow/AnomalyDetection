# Utils

En esta carpeta se encuentran funciones que permiten realizar operaciones que serán útiles en otros scripts.

## Contenido de la carpeta

### 1. `operaciones.py`

Este script tiene varias funciones útiles.

#### Funciones:
- **calcular_periodo(ruta_csv, min_distance, prominence, threshold_percentage):** A partir de la ruta pasada como parámetro y los parámetros siguientes, calcula y devuelve el periodo de dicha señal
- **calcular_camino_optimo_mejorada(matriz_correlacion, umbral_correlacion):** A partir de la matriz de correlación y un umbral de correlación (poco relevante), devolvemos los mejores periodos que utilizaremos como periodos de referencia para analizar las señales
