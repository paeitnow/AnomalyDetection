import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
data = pd.read_csv('C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv')

# Extraer los valores
timestamps = data['timestamp']
values = data['value']

# Asegúrate de que los timestamps están en formato correcto (opcional)
# timestamps = pd.to_datetime(timestamps)  # Descomenta si los timestamps son fechas

# 1. Realizar la Transformada de Fourier
fft_values = np.fft.fft(values)
fft_freq = np.fft.fftfreq(len(values), d=(timestamps[1] - timestamps[0]))  # Frecuencias asociadas a la FFT

# 2. Filtrar solo las frecuencias positivas
positive_freqs = fft_freq[:len(fft_freq)//2]
positive_fft_values = np.abs(fft_values[:len(fft_values)//2])

# 3. Identificar la frecuencia dominante
dominant_freq = positive_freqs[np.argmax(positive_fft_values)]
period = 1 / dominant_freq  # Calcular el período

# 4. Calcular la autocorrelación usando la FFT
# La autocorrelación es la inversa de la FFT de la magnitud al cuadrado
autocorr = np.fft.ifft(np.conj(fft_values) * fft_values).real

# Normalizar la autocorrelación
autocorr /= np.max(autocorr)

# 5. Graficar la señal, su Transformada de Fourier y la autocorrelación
plt.figure(figsize=(12, 12))

# Señal Original
plt.subplot(3, 1, 1)
plt.plot(timestamps, values, label='Señal Original', color='blue')
plt.xlabel('Timestamp')
plt.ylabel('Valor')
plt.title('Señal Periódica')
plt.grid()
plt.legend()

# Transformada de Fourier
plt.subplot(3, 1, 2)
plt.plot(positive_freqs, positive_fft_values, color='green', label='Transformada de Fourier')
plt.xlabel('Frecuencia [Hz]')
plt.ylabel('Magnitud')
plt.title('Espectro de Frecuencia')
plt.axvline(x=dominant_freq, color='red', linestyle='--', label='Frecuencia Dominante')
plt.legend()
plt.grid()

# Autocorrelación
plt.subplot(3, 1, 3)
# Aseguramos que la autocorrelación tiene la misma longitud que la señal original
plt.plot(autocorr[:len(values)], color='purple', label='Autocorrelación')
plt.xlabel('Desfase')
plt.ylabel('Autocorrelación Normalizada')
plt.title('Autocorrelación de la Señal')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# Mostrar el período
print(f'Frecuencia Dominante: {dominant_freq:.2f} Hz')
print(f'Período: {period:.2f} s')
