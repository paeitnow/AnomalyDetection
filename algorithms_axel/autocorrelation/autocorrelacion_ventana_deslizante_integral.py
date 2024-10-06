import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)

# Extraer los valores
timestamps = data['timestamp']
values = data['value']
labels = data['label']

# Parámetro de periodo estimado (encontrado previamente)
estimated_period = 1438  # Este valor puede venir de algún cálculo externo

# Número de periodos por ventana
num_periods_per_window = 4  # Por ejemplo, 3 periodos por ventana
window_size = estimated_period * num_periods_per_window

# Función para calcular la autocorrelación de un segmento
def autocorrelate(segment):
    n = len(segment)
    result = np.correlate(segment, segment, mode='full')  # Autocorrelación completa
    return result[result.size // 2:]  # Devolver solo la parte positiva

# Crear ventanas deslizantes con solapamiento
overlapping_windows = []
for i in range(0, len(values) - window_size + 1, estimated_period):  # Deslizamos de un periodo a la vez
    overlapping_windows.append(values[i:i + window_size])

# Lista para almacenar las sumas de las integrales
integral_sums = np.zeros(len(values))  # Inicializamos en ceros, con el mismo tamaño que la señal

# Crear la primera gráfica: Autocorrelaciones
plt.figure(figsize=(14, 8))

# Primera subgráfica: Señal original y anomalías
plt.subplot(2, 1, 1)  # (número de filas, número de columnas, índice de gráfico)
plt.plot(timestamps, values, label='Valores', color='blue')

# Resaltar los puntos con label == 1 (anomalías)
anomaly_points = data[data['label'] == 1]
plt.scatter(anomaly_points['timestamp'], anomaly_points['value'], color='red', label='Anomalías')

plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Señal Original y Detección de Anomalías')
plt.legend()
plt.grid()

# Segunda subgráfica: Suma de las integrales de autocorrelación
for i, window in enumerate(overlapping_windows):
    autocorr_window = autocorrelate(window)
    
    # Calcular la integral de la autocorrelación (área bajo la curva)
    autocorr_integral = np.trapz(autocorr_window)  # Usamos trapz para calcular la integral
    
    # Sumamos esta integral a los periodos involucrados en esta ventana
    start_period = i * estimated_period
    for j in range(window_size):  # Repartimos la integral en los periodos de la ventana
        if start_period + j < len(integral_sums):
            integral_sums[start_period + j] += autocorr_integral

# Graficar la suma de las integrales de autocorrelación
plt.subplot(2, 1, 2)  # Segunda subgráfica
plt.plot(timestamps, integral_sums, label='Suma de Integrales de Autocorrelación', color='orange')

plt.xlabel('Timestamp')
plt.ylabel('Suma de Integrales')
plt.title('Suma de las Integrales de Autocorrelación por Periodo')
plt.grid()
plt.legend()

# Mostrar la gráfica combinada
plt.tight_layout()
plt.show()
