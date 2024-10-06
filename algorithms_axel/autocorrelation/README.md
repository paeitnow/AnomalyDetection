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
