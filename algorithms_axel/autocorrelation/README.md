# Autocorrelation

En esta carpeta se encuentran algoritmos relacionados con el cálculo de la autocorrelación, una herramienta estadística que mide cómo un conjunto de datos se correlaciona consigo mismo en distintos retrasos temporales (lags).

## Contenido de la carpeta

### 1. `signal_tf_autocorrelacion.py`

Este script muestra la señal original, calcula su Transformada de Fourier y muestra su gráfica. También realiza la autocorrelación y muestra su gráfica. 

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la señal de entrada, otra con la Transformada de Fourier de dicha señal, y otra con la autocorrelación.

#### Notas:
- Estas gráficas dan una idea de cómo se comportan las señales
- A partir del calculo de la autocorrelación podemos calcular el periodo de las señales tal y como hemos hecho en [**Period Calculation**](https://github.com/paeitnow/AnomalyDetection/tree/main/algorithms_axel/period_calculation):

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/autocorrelation/image_signal_tf_autocorrelacion.png)

### 2. `autocorrelacion_ventana_deslizante_y_grafica.py`

Este script muestra las autocorrelaciones de la señal solapados en una sola gráfica.
La autocorrelación se realiza a partir de establecer una ventana deslizante de cierto tamaño.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos todas las autocorrelaciones solapadas.

#### Parámetros:
- **estimated_period:** Escribimos el periodo de la señal de forma manual. (sustituible por la función calcular_periodo de operaciones.py)
- **num_periods_per_window:** Tamaño de la ventana para hacer la autocorrelación

#### Notas:
- Este script pretende dar una idea del comportamiento de las distintas autocorrelaciones. Para ver el parecido que tienen los periodos con sus periodos vecinos.
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/autocorrelation/image_autocorrelacion_ventana_deslizante_y_grafica.png)

### 3. `autocorrelacion_ventana_deslizante_integral.py`
 
Este script calcula la autocorrelación de los periodos agrupados en una ventana del tamaño seleccionado, y realiza la integral de estos. Luego suma las diferentes integrales asociadas a cada uno de los periodos y las muestra por pantalla. el resultado que podemos interpretar son los periodos que tienen una mayor autocorrelación con los periodos vecinos. 

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp', los datos en la ventana 'value' y las anomalías en 'label'.
- **Salida:** La gráfica de entrada con sus respectivas anomalías y otra gráfica con la suma de las integrales de la autocorrelación.

#### Parámetros:
- **estimated_period:** Escribimos el periodo de la señal de forma manual. (sustituible por la función calcular_periodo de operaciones.py)
- **num_periods_per_window:** Tamaño de la ventana para hacer la autocorrelación

#### Notas:
- Este script pretende dar una idea del comportamiento de los diferentes periodos, señalando cuales son los que tienen un mayor parecido con los periodos vecinos
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/autocorrelation/image_autocorrelacion_ventana_deslizante_integral.png)

### 4. `autocorrelacion_ventana_deslizante_circular.py`
 
Este script calcula la autocorrelación de los periodos agrupados en una ventana del tamaño seleccionado, y realiza la integral de estos. Luego suma las diferentes integrales asociadas a cada uno de los periodos y las muestra por pantalla. el resultado que podemos interpretar son los periodos que tienen una mayor autocorrelación con los periodos vecinos. 

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp', los datos en la ventana 'value' y las anomalías en 'label'.
- **Salida:** La gráfica de entrada con sus respectivas anomalías y otra gráfica con la suma de las integrales de la autocorrelación.

#### Parámetros:
- **estimated_period:** Escribimos el periodo de la señal de forma manual. (sustituible por la función calcular_periodo de operaciones.py)
- **num_periods_per_window:** Tamaño de la ventana para hacer la autocorrelación

#### Notas:
- Este script pretende dar una idea del comportamiento de los diferentes periodos, señalando cuales son los que tienen un mayor parecido con los periodos vecinos
- Soluciona el problema que tenía 'autocorrelacion_ventana_deslizante_integral.py' al no establecer una ventana circular que tuviera en cuenta los primeros y últimos periodos
- Para el cálculo de los mejores periodos no utilizaremos estos scripts, sino que utilizaremos la función [calcular_camino_optimo_mejorada](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/utils/operaciones.py) a partir de la matriz de correlación
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/autocorrelation/image_autocorrelacion_ventana_deslizante_circular.png)
