import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

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
autocorr_trimmed = autocorr[1:]  # Recortar el primer elemento

# 3. Función para actualizar gráfico basado en el threshold, min_distance y prominence dinámicos
def update_graph(_):
    plt.cla()  # Limpiar la figura antes de dibujar

    # Obtener los valores actuales de los sliders
    threshold_percentage = threshold_slider.get()
    min_distance = int(distance_slider.get())
    prominence = prominence_slider.get()
    
    # Encontrar picos con restricciones de distancia y prominencia
    peaks, properties = find_peaks(autocorr_trimmed, distance=min_distance, prominence=prominence)

    # Ordenar picos por valor descendente
    sorted_autocorr_values = np.sort(autocorr_trimmed[peaks])[::-1]
    if len(sorted_autocorr_values) > 1:
        second_highest_value = sorted_autocorr_values[1]
    else:
        second_highest_value = sorted_autocorr_values[0]

    # Calcular el threshold basado en el segundo valor más alto
    threshold = threshold_percentage * second_highest_value

    # Filtrar picos que están por encima del umbral
    filtered_peaks = peaks[autocorr_trimmed[peaks] > threshold]
    
    # Mostrar picos filtrados y su distancia
    if len(filtered_peaks) > 1:
        peak_indices = [peak + 1 for peak in filtered_peaks[:2]]
        distances = np.diff(peak_indices)
        period_average = np.mean(distances)

        print(f"Índices de los dos primeros máximos: {peak_indices}")
        print(f"Distancia entre los dos primeros máximos: {distances}")
        print(f"Periodo promedio estimado: {period_average:.2f}")
    else:
        peak_indices = []
        period_average = None
    
    # Graficar la autocorrelación con el threshold
    ax.plot(autocorr, label='Autocorrelación', color='purple')
    ax.axhline(y=threshold, color='orange', linestyle='--', label=f'Umbral ({threshold_percentage*100:.1f}%)')  # Línea del umbral
    if len(filtered_peaks) > 0:
        ax.scatter([p + 1 for p in filtered_peaks], autocorr[filtered_peaks + 1], color='red', label='Máximos Filtrados')
    
    ax.set_xlabel('Desfase')
    ax.set_ylabel('Autocorrelación')
    ax.set_title('Autocorrelación con Umbral Dinámico')
    ax.grid()
    ax.legend()
    canvas.draw()  # Redibujar la figura


# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title('Ajuste del Umbral, Distancia y Prominencia con Sliders')

# Crear la figura de matplotlib
fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)  # Crear una figura de matplotlib en Tkinter
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Crear el slider para el umbral
threshold_slider = tk.Scale(root, from_=0.1, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, label='Threshold %', command=update_graph)
threshold_slider.set(0.75)  # Valor inicial del slider
threshold_slider.pack(side=tk.BOTTOM, fill=tk.X)

# Crear el slider para min_distance
distance_slider = tk.Scale(root, from_=1, to=100, resolution=1, orient=tk.HORIZONTAL, label='Min Distance', command=update_graph)
distance_slider.set(10)  # Valor inicial del slider
distance_slider.pack(side=tk.BOTTOM, fill=tk.X)

# Crear el slider para prominence
prominence_slider = tk.Scale(root, from_=0.01, to=1.0, resolution=0.01, orient=tk.HORIZONTAL, label='Prominence', command=update_graph)
prominence_slider.set(0.1)  # Valor inicial del slider
prominence_slider.pack(side=tk.BOTTOM, fill=tk.X)

# Llamar a la función la primera vez para dibujar
update_graph(None)

# Iniciar el bucle principal de Tkinter
root.mainloop()
