import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv')

# Extraer los valores
values = data['value']

# Parámetro de periodo estimado (encontrado previamente)
estimated_period = 1438

# 1. Dividir la señal en segmentos de tamaño cercano al periodo estimado
num_segments = len(values) // estimated_period  # Número de segmentos completos

# Tomar solo los segmentos completos de la señal
segments = np.array([values[i * estimated_period:(i + 1) * estimated_period] for i in range(num_segments)])

# 2. Calcular la media y desviación estándar para cada punto dentro del periodo
mean_values = np.mean(segments, axis=0)  # Media de los segmentos
std_values = np.std(segments, axis=0)    # Desviación estándar de los segmentos

# 3. Graficar la media y las áreas sombreadas de +/- 1 desviación estándar
plt.figure(figsize=(10, 6))

# Rellenar el área de la desviación estándar alrededor de la media
plt.fill_between(range(estimated_period), mean_values - std_values, mean_values + std_values, 
                 color='lightblue', alpha=0.5, label='±1 Desviación Estándar')

# Graficar la media
plt.plot(range(estimated_period), mean_values, color='blue', label='Media')

plt.xlabel('Puntos dentro de un ciclo')
plt.ylabel('Valor de la señal')
plt.title(f'Señales superpuestas por periodo estimado ({estimated_period} unidades)')
plt.grid()
plt.legend()
plt.show()
