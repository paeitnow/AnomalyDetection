# Moving Window

En esta carpeta se encuentran los algoritmos relacionados con el cálculo de la media móvil o "moving window". Estos algoritmos son útiles cuando se requiere realizar un análisis basado en datos dentro de una ventana de tamaño fijo que se desplaza a lo largo de una secuencia de datos.

## Contenido de la carpeta

### 1. `ventana_media_movil_centrada.py`

Este script implementa un algoritmo de media móvil simple. 

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la señal de entrada, la ventana, y las anomalías (puntos que están fuera de la ventana).

#### Parámetros: 
- **time_window_size:** Tamaño de la ventana en el eje X (tiempo), debe ser un número par
- **value_range:**  # Rango de valores permitidos en el eje Y

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/moving_window/image_ventana_media_movil_centrada.png)

### 2. `ventana_media_movil_centrada_automatica.py`

Este script implementa un algoritmo de media móvil simple automático.
El tamaño de la ventana varía en proporción al tamaño de los datos de la señal de entrada

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la señal de entrada, la ventana, y las anomalías (puntos que están fuera de la ventana).

#### Parámetros: 
- **percentage_of_data:** Este valor es el tamaño de la ventana creada en base al tamaño total de la señal
- **value_range:** este valor es proporcional a la desviación estándar

#### Notas: 
- La desviación estándar de la ventana automática se multiplica por un valor aleatorio, en realidad este valor debería obtenerse con algún algoritmo como K-means

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/moving_window/image_ventana_media_movil_centrada_automatica.png)

