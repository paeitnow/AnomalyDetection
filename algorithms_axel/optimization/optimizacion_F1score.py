import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from operaciones import calcular_camino_optimo_mejorada
from datetime import datetime


# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)

# Extraer los valores
values = data['value'].values
labels = data['label'].values  # Extraer las etiquetas para evaluar el modelo

# Parámetro de periodo estimado
estimated_period = 1438  # Suponiendo que este es el periodo estimado

# Número de periodos que queremos analizar
num_periods = len(values) // estimated_period

# Inicializar variables para la optimización
best_f1 = 0
best_precision = 0
best_recall = 0
best_params = {}

# Rango de valores para la optimización
correlation_thresholds = np.arange(0.5, 0.8, 0.005)
segment_thresholds = np.arange(0.1, 0.5, 0.005)
segment_sizes = range(40, 120, 2)

# Función para calcular F1 score
def calculate_f1_score(precision, recall):
    if precision + recall == 0:
        return 0
    return 2 * (precision * recall) / (precision + recall)
aux = 0
# Ciclo para probar diferentes valores de umbrales
for umbral_correlacion in correlation_thresholds:
    # Calcular la matriz de correlación
    aux=aux+1
    # Obtener la hora actual
    hora_actual = datetime.now()
    # Formatear la hora como desees (por ejemplo, "HH:MM:SS")
    hora_formateada = hora_actual.strftime("%H:%M:%S")
    print(f"{aux} Hora: {hora_formateada}")
    matriz_correlacion = np.zeros((num_periods, num_periods))
    for i in range(num_periods):
        for j in range(num_periods):
            if i != j:  # Evitar correlación consigo mismo
                segment_i = values[i * estimated_period:(i + 1) * estimated_period]
                segment_j = values[j * estimated_period:(j + 1) * estimated_period]
                correlacion = np.corrcoef(segment_i, segment_j)[0, 1]
                matriz_correlacion[i, j] = correlacion

    # Obtener los periodos de confianza usando la función mejorada
    mejor_camino, _ = calcular_camino_optimo_mejorada(matriz_correlacion, umbral_correlacion)

    # Probar diferentes valores de umbral de segmentos y tamaño de segmentos
    for umbral_segmentos in segment_thresholds:
        for segment_size in segment_sizes:
            anomalies = []  # Lista para almacenar las anomalías detectadas

            # Ciclo para recorrer todos los periodos usando el mejor camino
            for i in range(num_periods):
                # Segmento actual que vamos a analizar
                segment = values[i * estimated_period:(i + 1) * estimated_period]

                # Comparar con el periodo de confianza más cercano del camino óptimo
                closest_periodo_confianza_index = min(mejor_camino, key=lambda x: abs(x - i))
                segmento_confianza = values[closest_periodo_confianza_index * estimated_period:(closest_periodo_confianza_index + 1) * estimated_period]
                
                # Calcular la correlación con el periodo de confianza más cercano
                correlacion = np.corrcoef(segmento_confianza, segment)[0, 1]

                # Si la correlación es baja, proceder a la detección de anomalías
                if correlacion < umbral_correlacion:
                    # Trocear el segmento y verificar anomalías por trozos
                    for j in range(0, len(segment), segment_size):
                        trozo_confianza = segmento_confianza[j:j + segment_size]
                        trozo_segmento = segment[j:j + segment_size]

                        if len(trozo_confianza) == len(trozo_segmento):
                            correlacion_trozo = np.corrcoef(trozo_confianza, trozo_segmento)[0, 1]

                            if correlacion_trozo < umbral_segmentos:
                                start_anomaly = i * estimated_period + j
                                end_anomaly = start_anomaly + segment_size
                                anomalies.extend(range(start_anomaly, end_anomaly))  # Guardamos los índices como anomalías

            # Calcular precisión, recall y F1 Score
            predicciones = np.zeros_like(labels)
            predicciones[anomalies] = 1

            true_positive = np.sum((labels == 1) & (predicciones == 1))
            false_positive = np.sum((labels == 0) & (predicciones == 1))
            false_negative = np.sum((labels == 1) & (predicciones == 0))

            precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
            recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0

            f1_score = calculate_f1_score(precision, recall)

            # Almacenar los mejores parámetros
            if f1_score > best_f1:
                best_f1 = f1_score
                best_precision = precision
                best_recall = recall
                best_params = {
                    'umbral_correlacion': umbral_correlacion,
                    'umbral_segmentos': umbral_segmentos,
                    'segment_size': segment_size
                }

# Imprimir los mejores parámetros y su puntuación
print(f"Mejores Parámetros: {best_params}")
print(f"Mejor Precisión: {best_precision:.4f}")
print(f"Mejor Recall: {best_recall:.4f}")
print(f"Mejor F1 Score: {best_f1:.4f}")
