# Period Calculation

En esta carpeta se encuentran algoritmos destinados a calcular el periodo de una serie temporal, es decir, la duración de los ciclos repetitivos en los datos.

## Contenido de la carpeta

### 1. `fft_period.py`

Este script utiliza la Transformada Rápida de Fourier (FFT) para analizar la frecuencia de los datos y determinar el periodo dominante en una serie temporal. La FFT descompone una señal en sus componentes de frecuencia, lo que permite identificar la periodicidad.

#### Descripción:
- **Entrada:** Una lista de datos numéricos (serie temporal) y el intervalo de muestreo.
- **Salida:** El periodo dominante en los datos, basado en la frecuencia principal identificada por la FFT.

### 2. `autocorrelation_period.py`

Este archivo implementa un método alternativo para calcular el periodo, utilizando el análisis de autocorrelación. Este enfoque detecta el lag en el cual los datos son más similares a sí mismos, lo que indica un ciclo o repetición.

#### Descripción:
- **Entrada:** Una lista de datos numéricos y el número de lags a analizar.
- **Salida:** El periodo estimado basado en el lag más alto en la autocorrelación.

## Aplicaciones

- **Análisis de series temporales cíclicas:** para identificar patrones repetitivos, como temporadas en datos financieros o meteorológicos.
- **Procesamiento de señales:** para detectar componentes periódicas en señales ruidosas.
