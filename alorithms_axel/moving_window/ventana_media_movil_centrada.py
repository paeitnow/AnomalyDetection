import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/graf_periodica.csv')

# Extraer los valores
timestamps = data['timestamp']
values = data['value']

# Parámetros de la ventana cuadrada
time_window_size = 6  # Tamaño de la ventana en el eje X (tiempo), debe ser un número par
value_range = 100  # Rango de valores permitidos en el eje Y

# Listas para almacenar resultados
window_center = []
anomalies = []

# Definimos el tamaño de la media móvil centrada (debe ser par para dividir la ventana a ambos lados)
half_window = time_window_size // 2

# Recorremos los datos usando una ventana centrada
for i in range(len(values)):
    if i < half_window or i >= len(values) - half_window:
        # No calcular para los extremos donde no hay suficientes datos a ambos lados
        window_center.append(np.nan)
    else:
        # Definimos la ventana centrada
        window = values[i-half_window:i+half_window]
        
        # Calculamos la media dentro de la ventana centrada
        window_mean = window.mean()
        window_center.append(window_mean)
        
        # Detectamos anomalías si el valor se sale de la ventana cuadrada
        if abs(values[i] - window_mean) > value_range:
            anomalies.append(i)  # Guardamos el índice de la anomalía

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar todos los puntos
plt.plot(timestamps, values, label='Valores', color='blue')

# Graficar el centro de la ventana (media móvil centrada)
plt.plot(timestamps, window_center, label='Media Móvil Centrada', color='green')

# Graficar el área de la ventana cuadrada (eje Y)
upper_limit = np.array(window_center) + value_range
lower_limit = np.array(window_center) - value_range
plt.fill_between(timestamps, lower_limit, upper_limit, color='yellow', alpha=0.3, label='Ventana Cuadrada')

# Resaltar los puntos detectados como anomalías
plt.scatter(timestamps[anomalies], values[anomalies], color='red', label='Anomalías Detectadas')

# Etiquetas y leyenda
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Detección de Anomalías usando Media Móvil Centrada')
plt.legend()

# Mostrar la gráfica
plt.show()
