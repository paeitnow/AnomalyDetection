import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)

# Extraer los valores
values = data['value'].values

# Parámetro de periodo estimado (encontrado previamente)
estimated_period = 1438  # Suponiendo que este es el periodo estimado

# Número de periodos que queremos analizar
num_periods = len(values) // estimated_period

# Función para actualizar la gráfica en función del índice del periodo de confianza
def update_graph(val):
    periodo_confianza_index = int(float(val))  # Convertir el valor del slider a entero

    # Definir el rango del periodo de confianza
    inicio_confianza = periodo_confianza_index * estimated_period
    fin_confianza = (periodo_confianza_index + 1) * estimated_period

    # Segmentar los datos según el periodo de confianza
    segmento_confianza = values[inicio_confianza:fin_confianza]

    # Inicializar lista para almacenar las correlaciones
    correlaciones = []

    # Calcular la correlación entre el segmento de confianza y cada periodo
    for i in range(num_periods):
        segment = values[i * estimated_period:(i + 1) * estimated_period]
        # Calcular la correlación
        correlacion = np.corrcoef(segmento_confianza, segment)[0, 1]
        correlaciones.append(correlacion)

    # Limpiar la gráfica anterior
    axs[1].cla()
    axs[1].plot(range(num_periods), correlaciones, marker='o', linestyle='-', label='Correlación', color='blue')
    axs[1].set_xlabel('Índice del Periodo')
    axs[1].set_ylabel('Correlación')
    axs[1].set_title(f'Correlación con Segmento de Confianza (Índice {periodo_confianza_index})')
    axs[1].grid()
    axs[1].legend()

    # Redibujar la figura
    canvas.draw()

# Extraer los valores de anomalías
anomaly_timestamps = data['timestamp']
anomaly_values = data['value']
anomaly_labels = data['label']

# Crear la ventana principal de Tkinter
root = tk.Tk()
root.title('Ajuste de Periodo de Confianza')

# Crear la figura y los ejes
fig, axs = plt.subplots(2, 1, figsize=(10, 6))  # Reduce la altura de la figura


# Primera subgráfica: Detección de anomalías
axs[0].plot(anomaly_timestamps, anomaly_values, label='Valores', color='blue')
anomaly_points = data[data['label'] == 1]
axs[0].scatter(anomaly_points['timestamp'], anomaly_points['value'], color='red', label='Anomalías')
axs[0].set_xlabel('Timestamp')
axs[0].set_ylabel('Value')
axs[0].set_title('Detección de Anomalías')
axs[0].grid()
axs[0].legend()

# Segunda subgráfica: Correlación (esta se actualizará dinámicamente)
axs[1].set_xlabel('Índice del Periodo')
axs[1].set_ylabel('Correlación')
axs[1].set_title('Correlación entre Segmento de Confianza y Otros Segmentos')
axs[1].grid()

# Crear el canvas de la gráfica en Tkinter
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Crear el slider en la ventana de Tkinter
slider = tk.Scale(root, from_=0, to=num_periods-1, resolution=1, orient=tk.HORIZONTAL, label='Periodo de Confianza', command=lambda val: update_graph(val))
slider.set(0)  # Valor inicial del slider (índice 0)
slider.pack(side=tk.BOTTOM, fill=tk.X)

# Llamar a la función la primera vez para dibujar la gráfica inicial
update_graph(slider.get())

# Iniciar el bucle principal de Tkinter
root.mainloop()
