import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/graf_seno_anomaly.csv')

# Extraer los valores
values = data['value']

# Parámetro de periodo estimado (encontrado previamente)
estimated_period = 360

# 1. Dividir la señal en segmentos de tamaño cercano al periodo estimado
num_segments = len(values) // estimated_period  # Número de segmentos completos

# Tomar solo los segmentos completos de la señal
segments = [values[i * estimated_period:(i + 1) * estimated_period] for i in range(num_segments)]

# 2. Crear un plot donde cada periodo se superpone en el mismo eje
plt.figure(figsize=(10, 6))

# Graficar cada segmento superpuesto en el mismo eje
for i, segment in enumerate(segments):
    plt.plot(range(len(segment)), segment, label=f'Periodo {i+1}', alpha=0.6)  # Solapamos en x=0 para cada periodo

plt.xlabel('Puntos dentro de un ciclo')
plt.ylabel('Valor de la señal')
plt.title(f'Señales superpuestas con periodo estimado ({estimated_period} unidades)')
plt.grid()

# Mostrar solo una leyenda para no saturar el gráfico
plt.legend([f'Periodo {i+1}' for i in range(min(num_segments, 10))], loc='upper right', bbox_to_anchor=(1.2, 1), fontsize='small')

plt.show()
