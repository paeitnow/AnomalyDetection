import pandas as pd
import numpy as np

# Cargar los datos del archivo CSV
ruta = 'C:/Users/Axel/OneDrive/Documents/UPC/PAE/g.csv'
data = pd.read_csv(ruta)

# Extraer los valores
values = data['value'].values

# Parámetro de periodo estimado
estimated_period = 1438  # Suponiendo que este es el periodo estimado

# Definir el umbral de correlación
umbral_correlacion = 0.75  # Cambia este valor según el umbral deseado

# Número de periodos que queremos analizar
num_periods = len(values) // estimated_period

# Inicializar la matriz de correlación
matriz_correlacion = np.zeros((num_periods, num_periods))

# Calcular la matriz de correlación
for i in range(num_periods):
    for j in range(num_periods):
        if i != j:  # Evitar correlación consigo mismo
            segment_i = values[i * estimated_period:(i + 1) * estimated_period]
            segment_j = values[j * estimated_period:(j + 1) * estimated_period]
            correlacion = np.corrcoef(segment_i, segment_j)[0, 1]
            matriz_correlacion[i, j] = correlacion

# Filtrar los periodos de confianza que cumplen el umbral
periodos_confianza = np.where(np.max(matriz_correlacion, axis=1) >= umbral_correlacion)[0]

# Función para encontrar el camino óptimo
def encontrar_mejor_camino(matriz, periodos):
    mejor_camino = []
    mejor_puntuacion = 0

    for inicio in periodos:
        camino_actual = [inicio]
        puntuacion_total = 0

        while True:
            # Obtener las correlaciones del periodo actual
            correlaciones = matriz[camino_actual[-1]]
            # Filtrar los periodos que aún no están en el camino y que cumplen el umbral
            candidatos = np.where(correlaciones >= umbral_correlacion)[0]
            candidatos = [cand for cand in candidatos if cand not in camino_actual]
            
            # Si no hay más candidatos, terminamos
            if not candidatos:
                break
            
            # Encontrar el candidato con la máxima correlación
            siguiente = candidatos[np.argmax(correlaciones[candidatos])]
            camino_actual.append(siguiente)
            puntuacion_total += correlaciones[siguiente]

        # Calcular la puntuación promedio
        puntuacion_promedio = puntuacion_total / len(camino_actual)
        
        # Actualizar el mejor camino si es necesario
        if puntuacion_promedio > mejor_puntuacion:
            mejor_puntuacion = puntuacion_promedio
            mejor_camino = camino_actual

    return mejor_camino, mejor_puntuacion

# Encontrar el mejor camino
mejor_camino, mejor_puntuacion = encontrar_mejor_camino(matriz_correlacion, periodos_confianza)

# Imprimir los resultados
print(f"Mejor camino: {mejor_camino} con puntuación promedio: {mejor_puntuacion:.4f}")
