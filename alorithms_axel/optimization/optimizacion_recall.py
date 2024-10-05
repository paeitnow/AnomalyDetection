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
best_precision = 0
best_recall = 0
best_params = {}

# Rango y pasos para la optimización
correlation_thresholds = np.arange(0.5, 0.81, 0.01)
segment_thresholds = np.arange(0.3, 0.72, 0.02)
period_thresholds = np.arange(0.8, 0.96, 0.1)
segment_sizes = range(10, 101, 10)

# Función para detectar anomalías y calcular precisión y recall
def detect_anomalies(values, labels, estimated_period, umbral_correlacion, umbral_segmentos, umbral_nuevo_periodo, segment_size):
    anomalies = []  # Lista para almacenar las anomalías detectadas
    periodo_confianza_index = 0  # Inicializar el índice del periodo de confianza

    # Ciclo para recorrer todos los periodos
    for i in range(num_periods):
        # Segmento actual que vamos a analizar
        segment = values[i * estimated_period:(i + 1) * estimated_period]

        # Calcular la correlación con el periodo de confianza actual
        segmento_confianza = values[periodo_confianza_index * estimated_period:(periodo_confianza_index + 1) * estimated_period]
        correlacion = np.corrcoef(segmento_confianza, segment)[0, 1]

        # Si la correlación es baja, proceder a la detección de anomalías
        if correlacion < umbral_correlacion:
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
            periodo_confianza_index = i  # Actualizar el periodo de confianza

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
    
    return precision, recall
i=0
# Búsqueda de parámetros
for umbral_correlacion in correlation_thresholds:
    i=i+1
    print(i)
    for umbral_segmentos in segment_thresholds:
        for umbral_nuevo_periodo in period_thresholds:
            for segment_size in segment_sizes:
                precision, recall = detect_anomalies(values, labels, estimated_period, umbral_correlacion, umbral_segmentos, umbral_nuevo_periodo, segment_size)

                # Almacenar si se obtiene un mejor resultado
                if precision + recall > best_precision + best_recall:  # Puedes cambiar la lógica para priorizar precisión o recall
                    best_precision = precision
                    best_recall = recall
                    best_params = {
                        'umbral_correlacion': umbral_correlacion,
                        'umbral_segmentos': umbral_segmentos,
                        'umbral_nuevo_periodo': umbral_nuevo_periodo,
                        'segment_size': segment_size
                    }

# Imprimir los mejores parámetros y su puntuación
print(f"Mejores Parámetros: {best_params}")
print(f"Mejor Precisión: {best_precision:.4f}")
print(f"Mejor Recall: {best_recall:.4f}")
