import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv')

# Extraer los valores
timestamps = data['timestamp']
values = data['value']
labels = data['label']

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar todos los puntos
plt.plot(timestamps, values, label='Valores', color='blue')

# Resaltar los puntos con label == 1 (anomalías)
anomaly_points = data[data['label'] == 1]
plt.scatter(anomaly_points['timestamp'], anomaly_points['value'], color='red', label='Anomalías')

# Etiquetas y leyenda
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Detección de Anomalías')
plt.legend()

# Mostrar la gráfica
plt.show()
