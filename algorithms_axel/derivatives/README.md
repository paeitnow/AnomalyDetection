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
(https://github.com/paeitnow/AnomalyDetection/blob/main/algorithms_axel/derivatives/image_derivada_primera_consec.png)


### 2. `central_difference.py`

Este archivo contiene una implementación del método de diferencias centrales, que es una mejora sobre las diferencias finitas. El método central calcula la derivada en un punto utilizando los valores en los puntos adyacentes a ambos lados, lo que puede mejorar la precisión.

#### Descripción:
- **Entrada:** Una lista de valores de la función y el espaciado entre los puntos.
- **Salida:** Una lista de valores que representan la derivada numérica, calculada mediante diferencias centrales.

## Aplicaciones

- **Física:** para calcular velocidades y aceleraciones a partir de posiciones medidas en diferentes tiempos.
- **Análisis de datos científicos:** para determinar la tasa de cambio en series temporales.
- **Ingeniería:** para evaluar la respuesta de un sistema en función del tiempo u otras variables.

Estos algoritmos son útiles en situaciones donde no se conoce la forma analítica de una función, pero se disponen de mediciones o datos discretos.
