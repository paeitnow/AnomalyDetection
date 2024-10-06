import pandas as pd
import numpy as np
from operaciones import calcular_camino_optimo  # Importar la función desde operaciones.py

# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)

# Extraer los valores
values = data['value'].values

# Parámetro de periodo estimado
estimated_period = 1438  # Suponiendo que este es el periodo estimado

# Definir el umbral de correlación
umbral_correlacion = 0.75  # Cambia este valor según el umbral deseado

# Número de periodos que queremos analizar
num_periods = len(values) // estimated_period

# Inicializar la matriz de correlación
matriz_correlacion = np.zeros((num_periods, num_periods))

# Calcular la matriz de correlación
for i in range(num_periods):
    for j in range(num_periods):
        if i != j:  # Evitar correlación consigo mismo
            segment_i = values[i * estimated_period:(i + 1) * estimated_period]
            segment_j = values[j * estimated_period:(j + 1) * estimated_period]
            correlacion = np.corrcoef(segment_i, segment_j)[0, 1]
            matriz_correlacion[i, j] = correlacion

# Llamar a la función para encontrar el mejor camino
mejor_camino, mejor_puntuacion = calcular_camino_optimo(matriz_correlacion, umbral_correlacion)

# Imprimir los resultados
print(f"Mejor camino: {mejor_camino} con puntuación promedio: {mejor_puntuacion:.4f}")
