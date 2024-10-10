import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv')

# Extraer los valores
values = data['value'].values
labels = data['label'].values  # Anomalías originales

# Parámetros de la señal
period_length = 1438  # Muestras por periodo
num_periods = len(values) // period_length  # Número de periodos

# Parámetros de segmentación
segment_size = 100  # Tamaño de cada segmento para la correlación
correlation_threshold = 0  # Umbral para la correlación (puedes ajustar este valor)

# Período de referencia (primer periodo)
reference_period = values[0:period_length]

# Función para calcular la correlación de segmentos
def segment_correlation(segment_ref, segment_curr):
    if len(segment_ref) != len(segment_curr):
        raise ValueError("Los segmentos deben tener la misma longitud para calcular la correlación")
    
    return np.corrcoef(segment_ref, segment_curr)[0, 1]  # Correlación de Pearson

# Comparar la señal de referencia con cada período actual
scoring_periods = []  # Lista para almacenar los "scores" de cada periodo

for i in range(1, num_periods):
    period_start = i * period_length
    period_end = (i + 1) * period_length
    
    # Asegurarse de que los índices no excedan el tamaño de los valores
    if period_end > len(values):
        break
    
    current_period = values[period_start:period_end]
    current_labels = labels[period_start:period_end]  # Anomalías originales de este periodo
    
    # Dividir el periodo en segmentos
    num_segments = period_length // segment_size
    
    # Crear figura para mostrar la señal y las anomalías por segmentos
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))  # Subplot con 2 gráficos verticales

    time_axis = np.arange(period_length)  # Eje de tiempo común para ambos períodos

    # Graficar la señal original del periodo de referencia y el periodo actual
    ax1.plot(time_axis, reference_period, label='Período de Referencia', color='green', alpha=0.7)
    ax1.plot(time_axis, current_period, label=f'Período {i+1}', color='blue', alpha=0.7)
    
    # Detectar anomalías por segmentos usando la correlación
    anomalies = np.zeros(period_length, dtype=bool)  # Marcar las anomalías detectadas
    segment_correlations = []  # Guardar las correlaciones de los segmentos para calcular el score
    
    for j in range(num_segments):
        segment_start = j * segment_size
        segment_end = (j + 1) * segment_size
        
        # Extraer segmentos del periodo de referencia y actual
        segment_ref = reference_period[segment_start:segment_end]
        segment_curr = current_period[segment_start:segment_end]
        
        # Calcular la correlación entre segmentos
        corr = segment_correlation(segment_ref, segment_curr)
        segment_correlations.append(corr)  # Añadir la correlación a la lista
        
        if corr < correlation_threshold:
            # Marcar todo el segmento como anómalo
            anomalies[segment_start:segment_end] = True
    
    # Graficar la correlación en el segundo subplot
    segment_time_axis = np.arange(0, len(segment_correlations) * segment_size, segment_size)  # Ajustar el eje x a la cantidad de correlaciones
    ax2.plot(segment_time_axis, segment_correlations, marker='o', label='Correlación de Segmentos', color='purple')
    ax2.axhline(y=correlation_threshold, color='red', linestyle='--', label='Umbral de Correlación')


    # Configurar los subplots
    ax1.set_xlabel('Muestras')
    ax1.set_ylabel('Valor')
    ax1.set_title(f'Comparación de Señales: Período {i+1}')
    ax1.legend()

    ax2.set_xlabel('Muestras (inicio del segmento)')
    ax2.set_ylabel('Correlación')
    ax2.set_title('Correlación entre Segmentos')
    ax2.legend()

    # Mostrar anomalías detectadas y originales
    anomaly_indices = np.where(anomalies)[0]
    ax1.scatter(anomaly_indices, current_period[anomaly_indices], color='red', label='Anomalías Detectadas (Segmentos)', zorder=5)

    original_anomalies = np.where(current_labels == 1)[0]  # Suponiendo que 1 marca anomalías
    ax1.scatter(original_anomalies, current_period[original_anomalies], color='orange', label='Anomalías Originales', zorder=5)

    # Calcular el "scoring" del periodo (promedio de las correlaciones de segmentos)
    avg_correlation = np.mean(segment_correlations)
    scoring_periods.append(avg_correlation)  # Guardar el score para este periodo
    
    # Ajustar el layout
    plt.tight_layout()
    plt.show()

# Mostrar los scores de cada periodo al final
for i, score in enumerate(scoring_periods):
    print(f"Periodo {i+1}: Scoring = {score:.3f}")
