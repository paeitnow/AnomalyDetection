# Comparison

Esta carpeta contiene scripts dedicados a la comparación de diferentes series de datos.

## Contenido de la carpeta

### 1. `comparar_periodos_solapados.py`

Este script muestra todos los periodos de la señal solapados en la misma gráfica.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos todos los periodos de una señal solapados.

#### Parámetros:
- **estimated_period:** Estableceremos el periodo de la señal manualmente

#### Notas:
- Este script solo pretender dar una idea del comporamiento de los distintos periodos de la señal

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/comparison/image_comparar_periodos_solapados.png)
  
### 2. `comparar_periodos_auto_solapados.py`

Este script muestra todos los periodos de la señal solapados en la misma gráfica.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos todos los periodos de una señal solapados.

#### Parámetros:
- **threshold_percentage:** Este valor puede ser ajustado según la señal.
- **min_distance:** Mínima distancia entre picos para considerarlos como distintos
- **prominence:** Ajusta la prominencia para filtrar picos más pequeños

#### Notas:
- Este script solo pretender dar una idea del comporamiento de los distintos periodos de la señal
- Utilizaremos la función 'calcular_periodo' que se encuentra dentro del script [operaciones.py](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/utils/operaciones.py)

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/comparison/image_comparar_periodos_auto_solapados.png)

### 3. `comparar_periodos_mapa_densidad.py`

Este script muestra una gráfica de densidad para ver en que puntos del periodo solapado hay una mayor densidad. 
Pretendía dar una idea de en qué partes hay una mayor concentración de anomalías, pero el resultado es muy poco intuitivo

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/comparison/image_comparar_periodos_mapa_densidad.png)

### 4. `comparar_periodos_media_y_desviacion.py`

Este script muestra una gráfica de la media y la desviación de todos los periodos de la señal.

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/comparison/image_comparar_periodos_media_y_desviacion.png)


