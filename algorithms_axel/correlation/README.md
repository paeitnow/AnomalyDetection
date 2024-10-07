# Correlation

En esta carpeta se encuentran algoritmos dedicados al cálculo de la correlación entre diferentes conjuntos de datos. La correlación mide el grado en que dos variables están relacionadas.

## Contenido de la carpeta

### 1. `correlacion_signal_periodo_confianza.py`

Este script calcula la correlación de un periodo (periodo_confianza_index) con el resto, y nos muestra en una gráfica el valor normalizado de la correlación.
Esto nos permite conocer cómo de parecidos son dos periodos

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de datos 'value'.
- **Salida:** Una gráfica donde mostramos la correlación del periodo de referencia con el resto de periodos.

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_correlaci%C3%B3n_signal_periodo_confianza.png)

### 2. `correlacion_signal_periodo_confianza_anomaly.py`

Este script calcula la correlación de un periodo (periodo_confianza_index) con el resto, y nos muestra en una gráfica el valor normalizado de la correlación.
Esto nos permite conocer cómo de parecidos son dos periodos

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de datos 'value', tiempo 'timestap' y anaomalías 'labels'.
- **Salida:** Una gráfica donde mostramos la señal original con las anomalías correspondientes. Otra gráfica donde se muestra la correlación de los distintos periodos a partir del periodo de referencia.
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_correlaci%C3%B3n_signal_periodo_confianza_anomaly.png)

### 3. `correlacion_signal_periodo_confianza_anomaly_slide.py`

Este script calcula la correlación de un periodo (periodo_confianza_index) con el resto, y nos muestra en una gráfica el valor normalizado de la correlación.
Esto nos permite conocer cómo de parecidos son dos periodos
Disponemos de una barra de slide para modificar el periodo de referencia y ver la correlación de este con el resto de periodos

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de datos 'value', tiempo 'timestap' y anaomalías 'labels'.
- **Salida:** Una gráfica donde mostramos la señal original con las anomalías correspondientes. Otra gráfica donde se muestra la correlación de los distintos periodos a partir del periodo de referencia.
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_correlaci%C3%B3n_signal_periodo_confianza_anomaly_slide.png)

### 4. `correlacion_umbral.py`

Este script calcula la correlación de un periodo (periodo_confianza_index) con el resto, y nos muestra en una gráfica el valor normalizado de la correlación.
Esto nos permite conocer cómo de parecidos son dos periodos
Muestra también el valor de dicho umbral

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de datos 'value', tiempo 'timestap' y anaomalías 'labels'.
- **Salida:** Una gráfica donde mostramos la señal original con las anomalías correspondientes. Otra gráfica donde se muestra la correlación de los distintos periodos a partir del periodo de referencia y un umbral

#### Notas:
- El script nos indica los periodos que se encuentran por debajo del umbral establecido.
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_correlaci%C3%B3n_umbral.png)

### 5. `doble_correlacion_umbrales.py`

Este script calcula la correlación entre periodos para determinar su parecido, y a partir de establecer un umbral, vuelve a realizar la correlación entre segmentos de dichos periodos, para ver cómo de parecidos son a lo largo de todo un periodo. 

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de datos 'value', tiempo 'timestap' y anaomalías 'labels'.
- **Salida:** Una gráfica donde mostramos la señal original con las anomalías detectadas al hacer la correlación entre los segmentos de los periodos

#### Notas:
- El fijar un periodo de referencia resulta un inconveniente al tener periodos que varían con el tiempo
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_doble_correlacion_umbrales.png)

### 6. `doble_correlacion_umbrales_periodo_variable.py`

Este script calcula la correlación entre periodos para determinar su parecido, y a partir de establecer un umbral, vuelve a realizar la correlación entre segmentos de dichos periodos, para ver cómo de parecidos son a lo largo de todo un periodo. 
El periodo de referencia cambia a lo largo del tiempo, perimitiendo adaptarnos a los cambios que sufran los periodos a lo largo del tiempo

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de datos 'value', tiempo 'timestap' y anaomalías 'labels'.
- **Salida:** Una gráfica donde mostramos la señal original con las anomalías detectadas al hacer la correlación entre los segmentos de los periodos

#### Notas:
- Hemos modificado el tener un periodo de referencia fijo
- El calculo del siguiente periodo de referencia se establece a través de un umbral
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_doble_correlacion_umbrales_periodo_variable.png)

### 7. `doble_correlacion_umbrales_periodo_variable_scoring.py`

Este script es igual que `doble_correlacion_umbrales_periodo_variable.py`, pero le añadimos un scoring para obtener el recall y la precisión

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_doble_correlacion_umbrales_periodo_variable_scoring.png)

### 8. `doble_correlacion_umbrales_periodo_variable_scoring_operaciones.py`

Este script ya no tiene fijado un periodo de referencia, sino que llama a la función 'mejor_camino, mejor_puntuacion = calcular_camino_optimo_mejorada(matriz_correlacion, umbral_correlacion)' para calcular todos los periodos óptimos que utilizaremos como referencia.
La correlación entre periodos se hará con el periodo de referencia más cercano. 
Con el apoyo de scripts como ['optimizacion_F1score'](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/optimization/optimizacion_F1score.py) podremos encontrar los mejores parámetros para obtener un mayor scoring.

Los parámetros a optimizar serán:
- **umbral_correlacion:** analizaremos los periodos si están por debajo de cierto valor
- **segment_size:** Tamaño del segmento para la correlación por trozos
- **umbral_segmentos:** Umbral para detectar anomalías en trozos  

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_doble_correlacion_umbrales_periodo_variable_scoring_operaciones.png)
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/correlation/image_doble_correlacion_umbrales_periodo_variable_scoring_operaciones_2.png)

