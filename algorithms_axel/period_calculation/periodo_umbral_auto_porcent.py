import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv')

# Extraer los valores
timestamps = data['timestamp']
values = data['value']

# 1. Realizar la Transformada de Fourier
fft_values = np.fft.fft(values)
fft_freq = np.fft.fftfreq(len(values), d=(timestamps[1] - timestamps[0]))  # Frecuencias asociadas a la FFT

# 2. Calcular la autocorrelación
autocorr = np.fft.ifft(np.conj(fft_values) * fft_values).real

# 3. Buscar todos los máximos
autocorr_trimmed = autocorr[1:]  # Recortamos el primer elemento
peaks, properties = find_peaks(autocorr_trimmed)

# 4. Filtrar máximos usando umbral dinámico (basado en porcentaje del valor máximo)
threshold_percentage = 0.50  # Umbral al 10% del valor máximo
threshold = threshold_percentage * np.max(autocorr_trimmed)

# Filtrar picos según el umbral
filtered_peaks = peaks[autocorr_trimmed[peaks] > threshold]

# 5. Calcular distancias entre máximos
if len(filtered_peaks) > 1:
    # Ajustamos los índices de los picos para la autocorrelación completa
    peak_indices = [peak + 1 for peak in filtered_peaks]  # Ajustamos por el recorte

    # Calcular las distancias entre picos
    distances = np.diff(peak_indices)  # Distancias entre picos
    period_average = np.mean(distances)  # Periodo promedio

    # Mostrar resultados
    print(f"Índices de máximos: {peak_indices}")
    print(f"Distancias entre máximos: {distances}")
    print(f"Periodo promedio estimado: {period_average:.2f}")
else:
    peak_indices = []
    distances = []
    period_average = None

# 6. Graficar la autocorrelación y los máximos encontrados
plt.figure(figsize=(10, 6))
plt.plot(autocorr, label='Autocorrelación', color='purple')
plt.axhline(y=threshold, color='orange', linestyle='--', label=f'Umbral ({threshold_percentage*100:.1f}%)')  # Línea del umbral
if len(peak_indices) > 0:
    plt.scatter(peak_indices, autocorr[peak_indices], color='red', label='Máximos Filtrados')
plt.xlabel('Desfase')
plt.ylabel('Autocorrelación')
plt.title('Autocorrelación de la Señal con Umbral Dinámico')
plt.grid()
plt.legend()
plt.show()
