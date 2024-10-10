import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pywt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv')

# Extraer los valores
values = data['value'].values
labels = data['label'].values

# Parámetros de la señal
period_length = 1438  # Muestras por periodo
num_periods = len(values) // period_length  # Número de periodos

# Transformada Wavelet del periodo de referencia
reference_period = values[0:period_length]
coeffs_ref = pywt.wavedec(reference_period, wavelet='db1', level=4)

# Comparar la Transformada Wavelet de cada periodo con el de referencia
for i in range(1, num_periods):
    period_start = i * period_length
    period_end = (i + 1) * period_length
    
    # Asegurarse de que los índices no excedan el tamaño de los valores
    if period_end > len(values):
        break
    
    current_period = values[period_start:period_end]
    
    # Obtener etiquetas de anomalías para el período actual
    anomaly_labels = labels[period_start:period_end]

    # Transformada Wavelet del periodo actual
    coeffs = pywt.wavedec(current_period, wavelet='db1', level=4)

    # Crear figura para mostrar la señal y los niveles de la transformada wavelet
    num_levels = min(len(coeffs_ref), len(coeffs))  # Número de niveles a graficar
    fig, axs = plt.subplots(num_levels + 1, 1, figsize=(10, 2 * (num_levels + 1)))  # 1 para la señal y niveles

    # Graficar la señal original del periodo de referencia
    time_axis = np.arange(period_length)  # Eje de tiempo común para ambos períodos
    axs[0].plot(time_axis, reference_period, label='Período de Referencia', color='green', alpha=0.7)
    axs[0].plot(time_axis, current_period, label=f'Período {i+1}', color='blue', alpha=0.7)
    
    # Marcar las anomalías
    anomalies = np.where(anomaly_labels == 1)[0]
    axs[0].scatter(anomalies, current_period[anomalies], color='red', label='Anomalías', zorder=5)
    
    axs[0].set_xlabel('Muestras')
    axs[0].set_ylabel('Valor')
    axs[0].set_title(f'Comparación de Señales: Período de Referencia vs Período {i+1}')
    axs[0].legend()

    # Graficar los niveles de la Transformada Wavelet
    for j in range(num_levels):
        axs[j + 1].plot(coeffs_ref[j], label='Nivel Ref', color='green', alpha=0.7)
        axs[j + 1].plot(coeffs[j], label=f'Nivel {j} Período {i+1}', color='purple', alpha=0.7)
        axs[j + 1].set_xlabel('Coeficientes de Wavelet')
        axs[j + 1].set_ylabel('Valor')
        axs[j + 1].set_title(f'Nivel {j} de la Transformada Wavelet: Período de Referencia vs Período {i+1}')
        axs[j + 1].legend()

    # Ajustar el layout
    plt.tight_layout()
    plt.show()
