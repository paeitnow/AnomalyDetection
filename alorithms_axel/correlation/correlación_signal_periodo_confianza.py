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
    # Calcular la correlación
    correlacion = np.corrcoef(segmento_confianza, segment)[0, 1]  # Correlación entre los dos segmentos
    correlaciones.append(correlacion)

# Graficar las correlaciones
plt.figure(figsize=(10, 6))
plt.plot(range(num_periods), correlaciones, marker='o', linestyle='-')
#plt.axhline(y=0, color='r', linestyle='--')  # Línea horizontal en y=0 para referencia
plt.xlabel('Índice del Periodo')
plt.ylabel('Correlación')
plt.title('Correlación entre Segmento de Confianza y Otros Segmentos')
plt.grid()
plt.xticks(range(num_periods))  # Asegurar que los ticks estén alineados
plt.tight_layout()
plt.show()
