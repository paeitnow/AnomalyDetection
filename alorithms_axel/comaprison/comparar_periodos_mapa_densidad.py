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
segments = [values[i * estimated_period:(i + 1) * estimated_period] for i in range(num_segments)]

# Crear una matriz vacía para acumular la densidad de los puntos
density_matrix = np.zeros((len(segments[0]),))

# 2. Acumular la densidad en cada punto de los segmentos
for segment in segments:
    density_matrix += np.histogram(np.arange(len(segment)), bins=np.arange(len(segment)+1), weights=segment)[0]

# 3. Normalizar para que los valores estén entre 0 y 1 (esto ayudará a los colores)
density_matrix /= np.max(density_matrix)

# 4. Graficar la densidad como un heatmap de fondo
plt.figure(figsize=(10, 6))
plt.imshow(density_matrix[np.newaxis, :], cmap='Greys', aspect='auto', extent=[0, len(segments[0]), np.min(values), np.max(values)])

# 5. Graficar las líneas de cada periodo en color claro
for segment in segments:
    plt.plot(range(len(segment)), segment, color='lightblue', alpha=0.1)

plt.xlabel('Puntos dentro de un ciclo')
plt.ylabel('Valor de la señal')
plt.title(f'Señales superpuestas por periodo estimado ({estimated_period} unidades)')
plt.grid()
plt.show()
