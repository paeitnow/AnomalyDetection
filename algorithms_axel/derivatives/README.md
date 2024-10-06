# Derivatives

Esta carpeta contiene algoritmos que detectan anomalías a partir del cálculo de la derivada.

## Contenido de la carpeta

### 1. `derivada_primera_consec.py`

Este script implementa el método de diferencias finitas para calcular la derivada numérica de una función en puntos discretos.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la señal de entrada, y las anomalías detectadas a partir del umbral de derivación.

#### Parámetros: 
- **derivative_threshold:** Podemos ajustar este valor para definir qué es una variación anómala

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/derivatives/image_derivada_primera_consec.png)


### 2. `derivada_primera_ventana.py`

Este script implementa el método de diferencias finitas para calcular la derivada numérica de una función en puntos discretos. La diferencia con el anterior es que no toma dos puntos para hacer la derivada, sino que toma una ventana y calcula la media de los puntos dentro de la ventana. El calculo de la derivada se hace a partir de un punto y la derivada de la media de la ventana.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la señal de entrada, y las anomalías detectadas a partir del umbral de derivación y el tamaño de la ventana.

#### Parámetros: 
- **derivative_threshold:** Podemos ajustar este valor para definir qué es una variación anómala
- **window_size:** Número de valores siguientes para calcular la media futura

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/derivatives/image_derivada_primera_ventana.png)

### 3. `derivada_primera_ventana_graf_deriv.py`

Este script implementa el método de diferencias finitas para calcular la derivada numérica de una función en puntos discretos. La diferencia con el anterior es que no toma dos puntos para hacer la derivada, sino que toma una ventana y calcula la media de los puntos dentro de la ventana. El calculo de la derivada se hace a partir de un punto y la derivada de la media de la ventana. 
En este caso podemos visualizar además la gráfica de la derivada, y el umbral de la derivada.

#### Descripción:
- **Entrada:** Un archivo .csv con una columna de tiempo llamada 'timestamp' y los datos en la ventana 'value'.
- **Salida:** Una gráfica donde mostramos la señal de entrada, y las anomalías detectadas a partir del umbral de derivación y el tamaño de la ventana.

#### Parámetros: 
- **derivative_threshold:** Podemos ajustar este valor para definir qué es una variación anómala
- ***window_size:** Número de valores siguientes para calcular la media futura

#### Ejemplo de ejecución:
![No se puede cargar la imagen](https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/derivatives/image_derivada_primera_ventana_graf_deriv.png)

