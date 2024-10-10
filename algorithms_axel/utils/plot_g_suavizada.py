import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv')

# Extraer los valores
timestamps = data['timestamp']
values = data['value']
labels = data['label']

# Suavizado con promedio móvil
window_size = 5  # Tamaño de la ventana
moving_average = values.rolling(window=window_size, center=True).mean()

# Suavizado exponencial
exponential_smoothing = values.ewm(span=5, adjust=False).mean()

# Suavizado con Filtro de Savitzky-Golay
savgol_window_size = 5  # Debe ser un número impar
savgol_poly_order = 2    # Orden del polinomio
savgol_filtered = savgol_filter(values, savgol_window_size, savgol_poly_order)

# Crear la figura y los ejes
plt.figure(figsize=(12, 8))

# Graficar la señal original
plt.plot(timestamps, values, label='Valores Originales', color='blue', alpha=0.5)

# Graficar la señal suavizada con promedio móvil
plt.plot(timestamps, moving_average, label='Suavizado Promedio Móvil', color='orange')

# Graficar la señal suavizada con suavizado exponencial
plt.plot(timestamps, exponential_smoothing, label='Suavizado Exponencial', color='green')

# Graficar la señal suavizada con Filtro de Savitzky-Golay
plt.plot(timestamps, savgol_filtered, label='Suavizado Savitzky-Golay', color='purple')

# Resaltar los puntos con label == 1 (anomalías)
anomaly_points = data[data['label'] == 1]
plt.scatter(anomaly_points['timestamp'], anomaly_points['value'], color='red', label='Anomalías', alpha=0.7)

# Etiquetas y leyenda
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Detección de Anomalías y Suavizado de Señales')
plt.legend()

# Mostrar la gráfica
plt.show()
