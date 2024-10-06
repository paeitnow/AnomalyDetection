import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)

# Extraer los valores
values = data['value'].values
labels = data['label'].values  # Extraer las etiquetas para evaluar el modelo

# Parámetro de periodo estimado (encontrado previamente)
estimated_period = 1438  # Suponiendo que este es el periodo estimado

# Inicializar variables
num_periods = len(values) // estimated_period
umbral_correlacion = 0.74  # Cambia este valor según el umbral deseado para correlaciones
umbral_segmentos = 0.3  # Cambia este valor según el umbral deseado para detectar anomalías
umbral_nuevo_periodo = 0.9 # Modificamos el periodo de confianza si estamos por encima de este valor
segment_size = 80  # Tamaño del segmento para la correlación por trozos

# Seleccionar el periodo de confianza inicial (por defecto, 0)
periodo_confianza_index = 0
anomalies = []  # Lista para almacenar las anomalías detectadas

# Ciclo para recorrer todos los periodos
for i in range(num_periods):
    # Segmento actual que vamos a analizar
    segment = values[i * estimated_period:(i + 1) * estimated_period]

    # Calcular la correlación con el periodo de confianza actual
    segmento_confianza = values[periodo_confianza_index * estimated_period:(periodo_confianza_index + 1) * estimated_period]
    correlacion = np.corrcoef(segmento_confianza, segment)[0, 1]

    print(f"Correlación entre periodo de confianza {periodo_confianza_index} y periodo {i}: {correlacion:.4f}")

    # Si la correlación es baja, proceder a la detección de anomalías
    if correlacion < umbral_correlacion:
        print(f"Periodo {i} está por debajo del umbral de correlación. Analizando a trozos...")

        # Trocear el segmento de confianza y el segmento actual
        for j in range(0, len(segment), segment_size):
            trozo_confianza = segmento_confianza[j:j + segment_size]
            trozo_segmento = segment[j:j + segment_size]

            # Verificar que ambos trozos tengan el mismo tamaño
            if len(trozo_confianza) == len(trozo_segmento):
                correlacion_trozo = np.corrcoef(trozo_confianza, trozo_segmento)[0, 1]

                # Si la correlación del trozo está por debajo del nuevo umbral, consideramos que hay una anomalía
                if correlacion_trozo < umbral_segmentos:
                    start_anomaly = i * estimated_period + j
                    end_anomaly = start_anomaly + segment_size
                    anomalies.extend(range(start_anomaly, end_anomaly))  # Guardamos los índices como anomalías

    # Evaluar si la correlación es alta para actualizar el periodo de confianza
    if correlacion >= umbral_nuevo_periodo:
        print(f"Periodo {i} es el nuevo periodo de confianza.")
        periodo_confianza_index = i  # Actualizar el periodo de confianza

# Graficar la señal original y las anomalías detectadas
plt.figure(figsize=(14, 6))

# Graficar la señal original
plt.plot(data['timestamp'], values, label='Señal Original', color='blue')

# Graficar los puntos detectados como anomalías
if anomalies:
    anomaly_points = np.array([values[i] for i in anomalies])
    anomaly_timestamps = np.array([data['timestamp'][i] for i in anomalies])
    plt.scatter(anomaly_timestamps, anomaly_points, color='red', label='Anomalías Detectadas', s=20)

# Configurar etiquetas y título
plt.xlabel('Timestamp')
plt.ylabel('Valor de la señal')
plt.title('Señal Original con Anomalías Detectadas')
plt.legend()
plt.grid(True)
plt.show()

# Calcular la precisión y el recall
predicciones = np.zeros_like(labels)  # Inicializar las predicciones como ceros
predicciones[anomalies] = 1  # Marcar las anomalías detectadas

# Verdaderos positivos, falsos positivos y falsos negativos
true_positive = np.sum((labels == 1) & (predicciones == 1))
false_positive = np.sum((labels == 0) & (predicciones == 1))
false_negative = np.sum((labels == 1) & (predicciones == 0))

# Calcular precisión y recall manualmente
precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0

# Imprimir los resultados
print(f"Precisión: {precision:.4f}")
print(f"Recall: {recall:.4f}")
