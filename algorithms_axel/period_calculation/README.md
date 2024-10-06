# Period Calculation

En esta carpeta se encuentran algoritmos destinados a calcular el periodo de una serie temporal, es decir, la duración de los ciclos repetitivos en los datos.

## Contenido de la carpeta

### 1. `periodo_max_significativo.py`

Este script muestra la autocorrelación de la señal de entrada, nos muestra dónde se encuentra el primer máximo y no devuelve su valor.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la autocorrelación de la señal de entrada y el primer máximo significativo.

#### Notas:
- Esta gráfica pretende ser orientativa. el resultado no es muy fiable.
- El cálculo del primer máximo a partir de 'from scipy.signal import find_peaks' no resulta el mejor.

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/period_calculation/image_periodo_max_significativo.png)

### 2. `periodo_umbral_autocorrelacion.py`

Este script muestra la autocorrelación de la señal de entrada, nos muestra el umbral establecido y todos los picos de los máximos que se encuentran por encima.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la autocorrelación de la señal de entrada y los máximos significativos.

#### Notas:
- Esta gráfica pretende ser orientativa. el resultado no es muy fiable.
- El cálculo del primer máximo a partir de 'from scipy.signal import find_peaks' no resulta el mejor.
- Los máximos encontrados pueden ser muy cercanos, todavía falta definir la prominencia y la mínima distancia entre máximos
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/period_calculation/image_periodo_umbral_autocorrelacion.png)

### 3. `periodo_umbral_auto_porcent.py`

Este script muestra la autocorrelación de la señal de entrada, nos muestra el umbral establecido y todos los picos de los máximos que se encuentran por encima.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la autocorrelación de la señal de entrada y los máximos significativos.

#### Notas:
- Esta gráfica pretende ser orientativa. el resultado no es muy fiable.
- El cálculo del primer máximo a partir de 'from scipy.signal import find_peaks' no resulta el mejor.
- Los máximos encontrados pueden ser muy cercanos, todavía falta definir la prominencia y la mínima distancia entre máximos
- Queda solucionado el problema que teníamos con 'periodo_umbral_autocorrelacion' en el umbral al poder establecer un porcentaje
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/period_calculation/image_periodo_umbral_auto_porcent.png)

### 4. `periodo_umbral_auto_porcent_segundovalor.py`

Este script muestra la autocorrelación de la señal de entrada, nos muestra el umbral establecido y todos los picos de los máximos que se encuentran por encima, exceptuando el primero.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la autocorrelación de la señal de entrada y los máximos significativos.

#### Notas:
- Esta gráfica pretende ser orientativa. el resultado no es muy fiable.
- El cálculo del primer máximo a partir de 'from scipy.signal import find_peaks' no resulta el mejor.
- Los máximos encontrados pueden ser muy cercanos, todavía falta definir la prominencia y la mínima distancia entre máximos
- Queda solucionado el problema que teníamos con 'periodo_umbral_autocorrelacion' en el umbral al poder establecer un porcentaje
- Soluciona el problema de 'periodo_umbral_auto_porcent' al descartar el primer máximo de la autocorrelación
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/period_calculation/image_periodo_umbral_auto_porcent_segundovalor.png)

### 5. `periodo_umbral_descarte_seg_y_terc.py`

Este script muestra la autocorrelación de la señal de entrada y el umbral establecido. Nos permite calcular el periodo a partir de encontrar el segundo y tercer máximos de la autocorrelación y ver su distancia

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la autocorrelación de la señal de entrada y el segundo y tercer máximos significativos.

#### Parámetros:
- **threshold_percentage:** Este valor puede ser ajustado según la señal.
- **min_distance:** Mínima distancia entre picos para considerarlos como distintos
- **prominence** Ajusta la prominencia para filtrar picos más pequeños

#### Notas:
- La prominencia y la mínima distancia nos permiten acabar de ajustar la señal para no obtener falsos máximos y poder obtener un periodo fiable
- el segundo y tercer periodo son los más fiables para el cálculo del periodo
- Este script se encuentra en operaciones.py para devolver el periodo a partir de pasar como parámetros la señal de entrada y los parámetros aquí expuestos.
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/period_calculation/image_periodo_umbral_descarte_seg_y_terc.png)

### 6. `periodo_umbral_slider.py`

Este script muestra la autocorrelación de la señal de entrada y el umbral establecido. 
Tiene un slide para poder variar el parámetro 'threshold_percentage' y ver como varían los maximos

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la autocorrelación de la señal de entrada y los máximos significativos a paratir de los parámetros ajustados. También disponemos de un slide para modificar el 'threshold_percentage'

#### Parámetros:
- **threshold_percentage:** Este valor puede ser ajustado según la señal.
- **min_distance:** Mínima distancia entre picos para considerarlos como distintos
- **prominence** Ajusta la prominencia para filtrar picos más pequeños

#### Notas:
- Nos permite variar el valor del umbral para ver cómo varía el periodo
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/period_calculation/image_periodo_umbral_slider.png)

### 7. `periodo_umbral_slider_definitivo.py`

Este script muestra la autocorrelación de la señal de entrada y el umbral establecido.
Tiene tres slides para poder variar el parámetro 'threshold_percentage', 'min_dinstance' y 'prominence' para ver como varía el cálculo periodo

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la autocorrelación de la señal de entrada y los máximos significativos a paratir de los parámetros ajustados. También disponemos de un slide para modificar el 'threshold_percentage', 'min_dinstance' y 'prominence'

#### Parámetros:
- **threshold_percentage:** Este valor puede ser ajustado según la señal.
- **min_distance:** Mínima distancia entre picos para considerarlos como distintos
- **prominence** Ajusta la prominencia para filtrar picos más pequeños

#### Notas:
- Nos permite variar el valor del umbral, mínima distancia y prominencia para ver cómo varía el periodo
  
#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/period_calculation/image_periodo_umbral_slider_definitivo.png)





