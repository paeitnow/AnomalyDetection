# Moving Window

En esta carpeta se encuentran dos algoritmos relacionados con el cálculo de la media móvil o "moving window". Estos algoritmos son útiles cuando se requiere realizar un análisis basado en datos dentro de una ventana de tamaño fijo que se desplaza a lo largo de una secuencia de datos.

## Contenido de la carpeta

### 1. `moving_average.py`

Este script implementa un algoritmo de media móvil simple. La media móvil es un método estadístico para suavizar datos, eliminando el ruido y resaltando las tendencias a lo largo del tiempo. 

#### Descripción:
- **Entrada:** Una lista de datos numéricos (por ejemplo, una serie de tiempos) y el tamaño de la ventana.
- **Salida:** Una lista de medias móviles, donde cada valor representa la media de los datos dentro de la ventana correspondiente.

### 2. `weighted_moving_average.py`

Este archivo contiene una implementación de la media móvil ponderada. A diferencia de la media móvil simple, en este algoritmo se asignan pesos diferentes a los valores dentro de la ventana, dando más importancia a ciertos valores (normalmente, los más recientes).

#### Descripción:
- **Entrada:** Una lista de datos numéricos, el tamaño de la ventana y una lista de pesos.
- **Salida:** Una lista de medias móviles ponderadas, calculadas tomando en cuenta los pesos asignados a cada valor dentro de la ventana.

## Aplicaciones

- **Análisis financiero:** para suavizar el comportamiento de una serie de precios o valores.
- **Procesado de señal:** para reducir el ruido en una señal y destacar patrones relevantes.
- **Análisis de datos en tiempo real:** para tomar decisiones basadas en datos recientes con cierto nivel de suavizado.

Ambos scripts están diseñados para ser fáciles de utilizar y modificar, adaptándose a diferentes tipos de series de datos y tamaños de ventana.
