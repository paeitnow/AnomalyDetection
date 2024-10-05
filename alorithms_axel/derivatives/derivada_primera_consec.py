import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/graf_variable.csv')

# Extraer los valores
timestamps = data['timestamp']
values = data['value']

# Parámetro para el umbral de la primera derivada
derivative_threshold = 90  # Ajusta este valor para definir lo que es una variación anómala

# Calcular la primera derivada aproximada (diferencias entre valores consecutivos)
derivative = np.diff(values)

# Identificar anomalías donde la derivada exceda el umbral
anomalies = np.where(np.abs(derivative) > derivative_threshold)[0] + 1  # +1 para compensar el desplazamiento de la derivada

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar todos los puntos
plt.plot(timestamps, values, label='Valores', color='blue')

# Resaltar los puntos detectados como anomalías
plt.scatter(timestamps[anomalies], values[anomalies], color='red', label='Anomalías Detectadas (Primera Derivada)')

# Etiquetas y leyenda
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Detección de Anomalías usando la Primera Derivada')
plt.legend()

# Mostrar la gráfica
plt.show()
