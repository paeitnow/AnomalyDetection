import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv')

# Extraer los valores
values = data['value']
labels = data['label']

# Parámetros de la señal
period_length = 1438  # Muestras por periodo
num_periods = len(values) // period_length  # Número de periodos

# Función para calcular la FFT de un periodo
def calculate_fft(signal, sample_rate):
    N = len(signal)
    # Asegúrate de que la señal sea un numpy array
    signal = np.asarray(signal)  # Convertir a numpy array
    fft_vals = fft(signal)
    fft_freq = np.fft.fftfreq(N, d=1/sample_rate)
    return fft_freq[:N // 2], np.abs(fft_vals[:N // 2])  # Tomamos solo la mitad positiva

# Frecuencia de muestreo (ajusta según el intervalo de tiempo real entre las muestras)
sample_rate = 1  # Cambia este valor si es necesario

# FFT del periodo de referencia (primer periodo sin anomalías)
reference_period = values[0:period_length]
fft_freq_ref, fft_vals_ref = calculate_fft(reference_period, sample_rate)

# Comparar FFT de cada periodo con el de referencia
for i in range(1, num_periods):
    period_start = i * period_length
    period_end = (i + 1) * period_length
    current_period = values[period_start:period_end]

    # Calcular la FFT del periodo actual
    fft_freq, fft_vals = calculate_fft(current_period, sample_rate)
    
    # Crear figura para mostrar la señal y la FFT
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Graficar las señales originales solapadas
    time_axis = np.arange(period_length)  # Eje de tiempo común para ambos períodos
    axs[0].plot(time_axis, reference_period, label='Período de Referencia', color='green', alpha=0.7)
    axs[0].plot(time_axis, current_period, label=f'Período {i+1}', color='blue', alpha=0.7)
    axs[0].set_xlabel('Muestras')
    axs[0].set_ylabel('Valor')
    axs[0].set_title(f'Comparación de Señales: Período de Referencia vs Período {i+1}')
    axs[0].legend()

    # Graficar la FFT
    axs[1].plot(fft_freq_ref, fft_vals_ref, label='FFT Período de Referencia', color='green', alpha=0.7)
    axs[1].plot(fft_freq, fft_vals, label=f'FFT Período {i+1}', color='blue', alpha=0.7)
    axs[1].set_xlabel('Frecuencia (Hz)')
    axs[1].set_ylabel('Magnitud')
    axs[1].set_title(f'Comparación de FFT: Período de Referencia vs Período {i+1}')
    axs[1].legend()

    # Ajustar el layout
    plt.tight_layout()
    plt.show()
