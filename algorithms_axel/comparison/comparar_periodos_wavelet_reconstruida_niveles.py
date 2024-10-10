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
coeffs_ref = pywt.wavedec(reference_period, wavelet='db1', level=3)

# Función para reconstruir la señal desde un nivel específico de la wavelet
def reconstruct_signal(coeffs, level):
    coeffs_reconstructed = [np.zeros_like(c) for c in coeffs]
    coeffs_reconstructed[:level+1] = coeffs[:level+1]  # Mantener los primeros niveles
    return pywt.waverec(coeffs_reconstructed, wavelet='db1')

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
    coeffs = pywt.wavedec(current_period, wavelet='db1', level=3)
    
    # Obtener el número de niveles de la descomposición
    num_levels = len(coeffs)

    # Crear figura para mostrar la señal original y las reconstruidas
    fig, axs = plt.subplots(num_levels + 1, 1, figsize=(10, 2 * (num_levels + 1)))  # +1 para la señal original

    time_axis = np.arange(period_length)  # Eje de tiempo común para ambos períodos

    # Graficar la señal original del periodo actual
    axs[0].plot(time_axis, current_period, label=f'Período {i+1} Original', color='blue', alpha=0.7)
    axs[0].set_title('Período Original')
    axs[0].legend()

    # Graficar la señal reconstruida para cada nivel
    for j in range(num_levels):
        reconstructed_signal = reconstruct_signal(coeffs, level=j)
        axs[j + 1].plot(time_axis, current_period, label='Original', color='blue', alpha=0.7)
        axs[j + 1].plot(time_axis, reconstructed_signal[:period_length], label=f'Reconstruido Nivel {j}', color='red', alpha=0.7)
        axs[j + 1].set_title(f'Período Original vs Reconstrucción Nivel {j}')
        axs[j + 1].legend()

    # Ajustar el layout
    plt.tight_layout()
    plt.show()
