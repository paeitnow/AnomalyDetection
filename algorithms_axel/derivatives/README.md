# Derivatives

Esta carpeta contiene algoritmos que calculan derivadas numéricas a partir de datos discretos. Estos métodos son útiles en el análisis de datos cuando se desea conocer la tasa de cambio de una variable a lo largo de otra (por ejemplo, la derivada de una función de tiempo).

## Contenido de la carpeta

### 1. `finite_difference.py`

Este script implementa el método de diferencias finitas para calcular la derivada numérica de una función en puntos discretos.

#### Descripción:
- **Entrada:** Una lista de valores de la función (por ejemplo, posiciones a lo largo del tiempo) y el espaciado entre los puntos (por ejemplo, el intervalo de tiempo).
- **Salida:** Una lista de valores que representan la derivada numérica de los datos proporcionados.

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
