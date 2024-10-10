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

# Parámetros de la ventana deslizante
segment_size = 103  # Tamaño de cada ventana
step_size = 10  # Tamaño de paso para la ventana deslizante
correlation_threshold = 0.115  # Umbral para la correlación

# Período de referencia (primer periodo)
reference_period = values[0:period_length]

# Función para calcular la correlación entre ventanas
def window_correlation(segment_ref, segment_curr):
    if len(segment_ref) != len(segment_curr):
        raise ValueError("Las ventanas deben tener la misma longitud para calcular la correlación")
    
    return np.corrcoef(segment_ref, segment_curr)[0, 1]  # Correlación de Pearson

# Comparar la señal de referencia con cada período actual usando una ventana deslizante
scoring_periods = []  # Lista para almacenar los "scores" de cada periodo

for i in range(1, num_periods):
    period_start = i * period_length
    period_end = (i + 1) * period_length
    
    # Asegurarse de que los índices no excedan el tamaño de los valores
    if period_end > len(values):
        break
    
    current_period = values[period_start:period_end]
    current_labels = labels[period_start:period_end]  # Anomalías originales de este periodo

    # Comparar ventana deslizante del periodo de referencia con el periodo actual
    correlations = []
    sliding_positions = []  # Para el eje x de la gráfica
    
    # Graficar la señal en el subplot
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    time_axis = np.arange(period_length)  # Eje de tiempo para la señal

    # Graficar el periodo de referencia y el actual
    ax1.plot(time_axis, reference_period, label='Período de Referencia', color='green', alpha=0.7)
    ax1.plot(time_axis, current_period, label=f'Período {i+1}', color='blue', alpha=0.7)

    # Agregar el final del periodo anterior al inicio del periodo actual para una ventana deslizante circular
    if i > 1:
        previous_period = values[(i-1)*period_length: i*period_length]
        extended_current_period = np.concatenate((previous_period[-segment_size:], current_period))
    else:
        extended_current_period = current_period
    
    # Aplicar la ventana deslizante sobre el periodo actual
    for j in range(0, period_length - segment_size, step_size):
        window_ref = reference_period[j:j+segment_size]
        window_curr = extended_current_period[j:j+segment_size]

        # Calcular la correlación entre las ventanas
        corr = window_correlation(window_ref, window_curr)
        correlations.append(corr)
        sliding_positions.append(j + segment_size // 2)  # Posición de la ventana deslizante
    
    # Graficar las correlaciones en el segundo subplot
    ax2.plot(sliding_positions, correlations, marker='o', label='Correlación de Ventanas', color='purple')
    ax2.axhline(y=correlation_threshold, color='red', linestyle='--', label='Umbral de Correlación')

    # Mostrar anomalías detectadas y originales en la señal
    anomaly_indices = np.where(np.array(correlations) < correlation_threshold)[0]
    ax1.scatter(anomaly_indices * step_size, current_period[anomaly_indices * step_size], color='red', label='Anomalías Detectadas (Ventanas)', zorder=5)
    
    # Marcar las anomalías originales (guardadas en labels)
    original_anomalies = np.where(current_labels == 1)[0]  # Suponiendo que 1 marca anomalías
    ax1.scatter(original_anomalies, current_period[original_anomalies], color='orange', label='Anomalías Originales', zorder=5)

    # Etiquetas y leyendas
    ax1.set_xlabel('Muestras')
    ax1.set_ylabel('Valor')
    ax1.set_title(f'Comparación de Señales: Período {i+1}')
    ax1.legend()

    ax2.set_xlabel('Muestras')
    ax2.set_ylabel('Correlación')
    ax2.set_title(f'Correlación de Ventanas Deslizantes: Período {i+1}')
    ax2.legend()

    plt.tight_layout()
    plt.show()
