# Autocorrelation

En esta carpeta se encuentran algoritmos relacionados con el cálculo de la autocorrelación, una herramienta estadística que mide cómo un conjunto de datos se correlaciona consigo mismo en distintos retrasos temporales (lags).

## Contenido de la carpeta

### 1. `autocorrelation.py`

Este script implementa el cálculo de la autocorrelación para una serie de datos. La autocorrelación mide la similitud de los datos con versiones desplazadas de sí mismos, lo que ayuda a identificar patrones repetitivos o periodicidad.

#### Descripción:
- **Entrada:** Una lista de datos numéricos (como una serie temporal) y el número máximo de lags que se desean analizar.
- **Salida:** Un gráfico o una lista que muestra los valores de autocorrelación para cada lag.

## Aplicaciones

- **Series temporales:** para identificar patrones cíclicos o estacionales en datos financieros, meteorológicos o de otro tipo.
- **Procesamiento de señales:** para detectar la presencia de componentes repetitivas en señales discretas.
- **Análisis predictivo:** para comprender la dependencia de los datos en función del tiempo.

Este script es una herramienta fundamental para cualquier análisis de series temporales.
