import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/graf_periodica.csv')

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

# 4. Encontrar el segundo valor más alto de la autocorrelación
sorted_autocorr_values = np.sort(autocorr_trimmed[peaks])[::-1]  # Ordenar en orden descendente
if len(sorted_autocorr_values) > 1:
    second_highest_value = sorted_autocorr_values[1]  # Segundo valor más alto
else:
    second_highest_value = sorted_autocorr_values[0]  # Si solo hay un pico, usar el máximo

# 5. Definir el umbral como un porcentaje del segundo valor más alto
threshold_percentage = 0.75  # Umbral al 10% del segundo valor más alto
threshold = threshold_percentage * second_highest_value

# Filtrar picos según el umbral
filtered_peaks = peaks[autocorr_trimmed[peaks] > threshold]

# 6. Calcular distancias entre máximos
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

# 7. Graficar la autocorrelación y los máximos encontrados
plt.figure(figsize=(10, 6))
plt.plot(autocorr, label='Autocorrelación', color='purple')
plt.axhline(y=threshold, color='orange', linestyle='--', label=f'Umbral ({threshold_percentage*100:.1f}% del segundo valor más alto)')  # Línea del umbral
if len(peak_indices) > 0:
    plt.scatter(peak_indices, autocorr[peak_indices], color='red', label='Máximos Filtrados')
plt.xlabel('Desfase')
plt.ylabel('Autocorrelación')
plt.title('Autocorrelación de la Señal con Umbral Dinámico (Basado en el Segundo Valor Más Alto)')
plt.grid()
plt.legend()
plt.show()
