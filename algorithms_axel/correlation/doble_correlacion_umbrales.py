import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)

# Extraer los valores
values = data['value'].values

# Parámetro de periodo estimado (encontrado previamente)
estimated_period = 1438  # Suponiendo que este es el periodo estimado

# Índice del periodo de confianza (0, 1, 2, etc.)
periodo_confianza_index = 0  # Cambia este valor según el periodo de confianza deseado

# Definir el rango del periodo de confianza
inicio_confianza = periodo_confianza_index * estimated_period
fin_confianza = (periodo_confianza_index + 1) * estimated_period

# Segmentar los datos según el periodo de confianza
segmento_confianza = values[inicio_confianza:fin_confianza]

# Número de periodos que queremos analizar
num_periods = len(values) // estimated_period

# Inicializar listas para almacenar las correlaciones
correlaciones = []

# Calcular la correlación entre el segmento de confianza y cada periodo
for i in range(num_periods):
    segment = values[i * estimated_period:(i + 1) * estimated_period]
    correlacion = np.corrcoef(segmento_confianza, segment)[0, 1]  # Correlación entre los dos segmentos
    correlaciones.append(correlacion)

# Definir el umbral de correlación
umbral_correlacion = 0.90  # Cambia este valor según el umbral deseado

# Identificar los periodos que están por debajo del umbral
periodos_bajos = [i for i, correlacion in enumerate(correlaciones) if correlacion < umbral_correlacion]

# Parámetro para trocear los periodos en segmentos más pequeños (por ejemplo, en segmentos de 100 muestras)
segment_size = 60  # Cambia esto según el tamaño que quieras para cada trozo

# Definir un nuevo umbral para la correlación de los segmentos troceados
umbral_segmentos = 0.5  # Cambia este valor según el umbral deseado para detectar anomalías

# Inicializar lista para almacenar los resultados de anomalías
anomalies = []

# Analizar los periodos bajos
for i in periodos_bajos:
    segment = values[i * estimated_period:(i + 1) * estimated_period]
    
    # Trocear tanto el segmento de confianza como el segmento actual
    for j in range(0, len(segment), segment_size):
        # Obtener los trozos del periodo de confianza y del periodo bajo el umbral
        trozo_confianza = segmento_confianza[j:j + segment_size]
        trozo_segmento = segment[j:j + segment_size]
        
        # Verificar que ambos trozos tengan el mismo tamaño (esto puede fallar en el último segmento si el tamaño no es múltiplo exacto)
        if len(trozo_confianza) == len(trozo_segmento):
            # Calcular la correlación entre los trozos
            correlacion_trozo = np.corrcoef(trozo_confianza, trozo_segmento)[0, 1]
            
            # Si la correlación del trozo está por debajo del nuevo umbral, consideramos que hay una anomalía
            if correlacion_trozo < umbral_segmentos:
                start_anomaly = i * estimated_period + j  # Índice de inicio del trozo en la señal original
                end_anomaly = start_anomaly + segment_size  # Índice de fin del trozo
                anomalies.extend(range(start_anomaly, end_anomaly))  # Guardamos los índices como anomalías

# Graficar la señal original y las anomalías detectadas
plt.figure(figsize=(14, 6))

# Graficar la señal original
plt.plot(data['timestamp'], values, label='Señal Original', color='blue')

# Graficar los puntos detectados como anomalías
anomaly_points = np.array([values[i] for i in anomalies])
anomaly_timestamps = np.array([data['timestamp'][i] for i in anomalies])

plt.scatter(anomaly_timestamps, anomaly_points, color='red', label='Anomalías Detectadas', s=20)

# Configurar etiquetas y título
plt.xlabel('Timestamp')
plt.ylabel('Valor de la señal')
plt.title('Señal Original con Anomalías Detectadas')
plt.legend()
plt.grid(True)
plt.show()
