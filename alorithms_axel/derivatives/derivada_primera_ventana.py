import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/graf_variable.csv')

# Extraer los valores
timestamps = data['timestamp']
values = data['value']

# Parámetro para el umbral de la derivada y el tamaño de la ventana
derivative_threshold = 100  # Ajusta este valor para definir lo que es una variación anómala
window_size = 3  # Número de valores siguientes para calcular la media

# Listas para almacenar resultados
derivatives = []
anomalies = []

# Recorremos los valores, excepto los últimos (donde no hay suficientes valores siguientes para calcular la media)
for i in range(len(values) - window_size):
    # Calculamos la media de los X valores siguientes
    future_mean = np.mean(values[i+1:i+1+window_size])
    
    # Calculamos la derivada aproximada (diferencia entre el valor actual y la media futura)
    derivative = values[i] - future_mean
    derivatives.append(derivative)
    
    # Detectar anomalías si la derivada supera el umbral
    if abs(derivative) > derivative_threshold:
        anomalies.append(i)  # Guardar el índice de la anomalía

# Rellenar el final de la lista de derivadas con NaN (porque no tenemos suficientes valores futuros)
derivatives.extend([np.nan] * window_size)

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar todos los puntos
plt.plot(timestamps, values, label='Valores', color='blue')

# Resaltar los puntos detectados como anomalías
plt.scatter(timestamps[anomalies], values[anomalies], color='red', label='Anomalías Detectadas (Derivada con media futura)')

# Etiquetas y leyenda
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Detección de Anomalías usando Derivada con Media Futura')
plt.legend()

# Mostrar la gráfica
plt.show()
