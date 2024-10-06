import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)
# Extraer los valores
values = data['value']

# Parámetro de periodo estimado (encontrado previamente)
estimated_period = 1438  # Este valor puede venir de algún cálculo externo

# Número de periodos por ventana
num_periods_per_window = 3  # Por ejemplo, 3 periodos por ventana
window_size = estimated_period * num_periods_per_window

# Función para calcular la autocorrelación de un segmento
def autocorrelate(segment):
    n = len(segment)
    result = np.correlate(segment, segment, mode='full')  # Autocorrelación completa
    return result[result.size // 2:]  # Devolver solo la parte positiva

# Crear ventanas deslizantes con solapamiento
overlapping_windows = []
for i in range(0, len(values) - window_size + 1, estimated_period):  # Deslizamos de un periodo a la vez
    overlapping_windows.append(values[i:i + window_size])

# 2. Crear un plot donde se muestra la autocorrelación de cada ventana deslizante
plt.figure(figsize=(10, 6))

# Graficar la autocorrelación de cada ventana deslizante
for i, window in enumerate(overlapping_windows):
    autocorr_window = autocorrelate(window)
    plt.plot(range(len(autocorr_window)), autocorr_window, label=f'Autocorr ventana {i+1}', alpha=0.6)

plt.xlabel('Lag')
plt.ylabel('Autocorrelación')
plt.title(f'Autocorrelaciones de ventanas deslizantes ({num_periods_per_window} periodos por ventana)')
plt.grid()

# Mostrar solo una leyenda para no saturar el gráfico
plt.legend([f'Autocorr {i+1}' for i in range(min(len(overlapping_windows), 10))], loc='upper right', bbox_to_anchor=(1.2, 1), fontsize='small')

plt.show()
