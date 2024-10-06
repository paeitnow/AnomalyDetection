import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)

# Extraer los valores
values = data['value'].values

# Parámetro de periodo estimado (encontrado previamente)
estimated_period = 1438  # Suponiendo que este es el periodo estimado

# Índice del periodo de confianza (0, 1, 2, etc.)
periodo_confianza_index = 63  # Cambia este valor según el periodo de confianza deseado

# Definir el rango del periodo de confianza
inicio_confianza = periodo_confianza_index * estimated_period
fin_confianza = (periodo_confianza_index + 1) * estimated_period

# Segmentar los datos según el periodo de confianza
segmento_confianza = values[inicio_confianza:fin_confianza]

# Número de periodos que queremos analizar
num_periods = len(values) // estimated_period

# Inicializar listas para almacenar las correlaciones
correlaciones = []

# Calcular la correlación entre el segmento de confianza y cada periodo
for i in range(num_periods):
    segment = values[i * estimated_period:(i + 1) * estimated_period]
    # Calcular la correlación
    correlacion = np.corrcoef(segmento_confianza, segment)[0, 1]  # Correlación entre los dos segmentos
    correlaciones.append(correlacion)

# Definir el umbral de correlación
umbral_correlacion = 0.75  # Cambia este valor según el umbral deseado

# Identificar los periodos que están por debajo del umbral
periodos_bajos = [i for i, correlacion in enumerate(correlaciones) if correlacion < umbral_correlacion]

# Imprimir los periodos con correlación por debajo del umbral
print(f"Periodos con correlación por debajo de {umbral_correlacion}: {periodos_bajos}")

# Extraer los valores de anomalías
anomaly_timestamps = data['timestamp']
anomaly_values = data['value']
anomaly_labels = data['label']

# Crear la figura y los ejes
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Resaltar los puntos con label == 1 (anomalías) en la primera subgráfica
axs[0].plot(anomaly_timestamps, anomaly_values, label='Valores', color='blue')
anomaly_points = data[anomaly_labels == 1]
axs[0].scatter(anomaly_points['timestamp'], anomaly_points['value'], color='red', label='Anomalías')
axs[0].set_xlabel('Timestamp')
axs[0].set_ylabel('Value')
axs[0].set_title('Detección de Anomalías')
axs[0].grid()
axs[0].legend()

# Graficar las correlaciones en la segunda subgráfica
axs[1].plot(range(num_periods), correlaciones, marker='o', linestyle='-', label='Correlación', color='blue')
axs[1].set_xlabel('Índice del Periodo')
axs[1].set_ylabel('Correlación')
axs[1].set_title('Correlación entre Segmento de Confianza y Otros Segmentos')
axs[1].axhline(y=umbral_correlacion, color='red', linestyle='--', label=f'Umbral = {umbral_correlacion}')  # Línea del umbral
axs[1].grid()
axs[1].legend()

# Ajustar el layout
plt.tight_layout()

# Mostrar la gráfica
plt.show()
