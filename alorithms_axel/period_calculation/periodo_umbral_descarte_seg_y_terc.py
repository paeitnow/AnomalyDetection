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

# 3. Recortar el primer elemento (autocorrelación en lag 0)
autocorr_trimmed = autocorr[1:]  # Recortamos el primer elemento

# 4. Buscar máximos con restricciones de distancia y prominencia
min_distance = 10  # Mínima distancia entre picos (ajusta este valor según el tamaño de tu señal)
prominence = 0.1  # Ajusta la prominencia para filtrar picos más pequeños

peaks, properties = find_peaks(autocorr_trimmed, distance=min_distance, prominence=prominence)

# 5. Filtrar picos según el threshold basado en el segundo valor más alto
sorted_autocorr_values = np.sort(autocorr_trimmed[peaks])[::-1]  # Ordenar en orden descendente
if len(sorted_autocorr_values) > 1:
    second_highest_value = sorted_autocorr_values[1]  # Segundo valor más alto
else:
    second_highest_value = sorted_autocorr_values[0]  # Si solo hay un pico, usar el máximo

threshold_percentage = 0.75  # Umbral al 75% del segundo valor más alto
threshold = threshold_percentage * second_highest_value

# Filtrar los picos que están por encima del umbral
filtered_peaks = peaks[autocorr_trimmed[peaks] > threshold]

# 6. Mantener solo los dos primeros máximos consecutivos significativos
if len(filtered_peaks) > 1:
    # Ajustamos los índices de los picos para la autocorrelación completa
    peak_indices = [peak + 1 for peak in filtered_peaks[:2]]  # Solo los dos primeros máximos

    # Calcular las distancias entre los dos primeros máximos
    distances = np.diff(peak_indices)  # Distancias entre los dos primeros picos
    period_average = np.mean(distances)  # Periodo promedio

    # Mostrar resultados
    print(f"Índices de los dos primeros máximos: {peak_indices}")
    print(f"Distancia entre los dos primeros máximos: {distances}")
    print(f"Periodo promedio estimado: {period_average:.2f}")
else:
    peak_indices = []
    distances = []
    period_average = None

# 7. Graficar la autocorrelación y los máximos encontrados
plt.figure(figsize=(10, 6))
plt.plot(autocorr, label='Autocorrelación', color='purple')
plt.axhline(y=threshold, color='orange', linestyle='--', label=f'Umbral ({threshold_percentage*100:.1f}% del segundo valor más alto)')  # Línea del umbral
if len(peak_indices) > 0:
    plt.scatter(peak_indices, autocorr[peak_indices], color='red', label='Máximos Filtrados')
plt.xlabel('Desfase')
plt.ylabel('Autocorrelación')
plt.title('Autocorrelación de la Señal con Umbral Dinámico y Filtro de Máximos')
plt.grid()
plt.legend()
plt.show()
