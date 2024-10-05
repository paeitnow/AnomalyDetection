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

# 3. Buscar el siguiente máximo
# Ignorar el primer valor (desfase 0)
autocorr_trimmed = autocorr[1:]  # Recortamos el primer elemento

# Buscar todos los picos en la autocorrelación
peaks, properties = find_peaks(autocorr_trimmed)

# Filtrar el siguiente máximo significativo
if len(peaks) > 1:
    next_peak_index = peaks[1] + 1  # Ajustamos el índice por el recorte
    next_peak_value = autocorr[next_peak_index]
else:
    next_peak_index = None
    next_peak_value = None

# 4. Graficar la autocorrelación
plt.figure(figsize=(10, 6))
plt.plot(autocorr, label='Autocorrelación', color='purple')
if next_peak_index is not None:
    plt.axvline(x=next_peak_index, color='red', linestyle='--', label='Siguiente Máximo Significativo')
plt.xlabel('Desfase')
plt.ylabel('Autocorrelación')
plt.title('Autocorrelación de la Señal')
plt.grid()
plt.legend()
plt.show()

# Mostrar el siguiente máximo
if next_peak_value is not None:
    print(f'Siguiente máximo en la autocorrelación encontrado en el índice {next_peak_index}, valor: {next_peak_value:.2f}')
else:
    print('No se encontró un siguiente máximo significativo en la autocorrelación.')
