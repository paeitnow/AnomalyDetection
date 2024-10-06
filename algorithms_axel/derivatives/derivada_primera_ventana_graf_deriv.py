import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/graf_variable.csv')

# Extraer los valores
timestamps = data['timestamp']
values = data['value']

# Parámetros para la detección de anomalías
derivative_threshold = 150  # Umbral de la derivada
window_size = 4  # Número de valores siguientes para calcular la media futura

# Listas para almacenar resultados
derivatives = []
anomalies = []

# Recorremos los valores, excepto los últimos (donde no hay suficientes valores futuros)
for i in range(len(values) - window_size):
    # Calcular la media de los X valores siguientes
    future_mean = np.mean(values[i+1:i+1+window_size])
    
    # Calcular la derivada (diferencia entre el valor actual y la media futura)
    derivative = values[i] - future_mean
    derivatives.append(derivative)
    
    # Detectar anomalías si la derivada supera el umbral
    if abs(derivative) > derivative_threshold:
        anomalies.append(i)  # Guardar el índice de la anomalía

# Rellenar la lista de derivadas con NaN al final para los valores sin suficientes futuros
derivatives.extend([np.nan] * window_size)

# Crear una figura con dos subgráficos
fig, ax = plt.subplots(2, 1, figsize=(10, 10))

# Subgráfico 1: Valores originales y anomalías
ax[0].plot(timestamps, values, label='Valores', color='blue')
ax[0].scatter(timestamps[anomalies], values[anomalies], color='red', label='Anomalías Detectadas')
ax[0].set_xlabel('Timestamp')
ax[0].set_ylabel('Value')
ax[0].set_title('Valores Originales y Anomalías Detectadas')
ax[0].legend()

# Subgráfico 2: Derivada de la diferencia con la media futura
ax[1].plot(timestamps, derivatives, label='Derivada (Valor - Media Futura)', color='green')
ax[1].axhline(y=derivative_threshold, color='red', linestyle='--', label='Umbral Positivo')
ax[1].axhline(y=-derivative_threshold, color='red', linestyle='--', label='Umbral Negativo')
ax[1].scatter(timestamps[anomalies], [derivatives[i] for i in anomalies], color='orange', label='Anomalías en Derivada')
ax[1].set_xlabel('Timestamp')
ax[1].set_ylabel('Derivative')
ax[1].set_title('Derivada basada en la Media Futura')
ax[1].legend()

# Ajustar el espaciado entre subgráficos
plt.tight_layout()

# Mostrar la gráfica
plt.show()
