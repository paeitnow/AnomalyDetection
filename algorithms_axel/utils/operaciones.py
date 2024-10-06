import pandas as pd
import numpy as np
from scipy.signal import find_peaks

# Función para calcular el periodo
def calcular_periodo(ruta_csv, min_distance, prominence, threshold_percentage):
    # Cargar los datos del archivo CSV
    data = pd.read_csv(ruta_csv)

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
    peaks, properties = find_peaks(autocorr_trimmed, distance=min_distance, prominence=prominence)

    # 5. Filtrar picos según el threshold basado en el segundo valor más alto
    sorted_autocorr_values = np.sort(autocorr_trimmed[peaks])[::-1]  # Ordenar en orden descendente
    if len(sorted_autocorr_values) > 1:
        second_highest_value = sorted_autocorr_values[1]  # Segundo valor más alto
    else:
        second_highest_value = sorted_autocorr_values[0]  # Si solo hay un pico, usar el máximo

    threshold = threshold_percentage * second_highest_value

    # Filtrar los picos que están por encima del umbral
    filtered_peaks = peaks[autocorr_trimmed[peaks] > threshold]

    # 6. Mantener solo los dos primeros máximos consecutivos significativos
    if len(filtered_peaks) > 1:
        peak_indices = [peak + 1 for peak in filtered_peaks[:2]]  # Solo los dos primeros máximos

        # Calcular las distancias entre los dos primeros máximos
        distances = np.diff(peak_indices)  # Distancias entre los dos primeros picos
        period_average = np.mean(distances)  # Periodo promedio
        #print(f"Periodo: {period_average}")
        return period_average  # Devolvemos el periodo como resultado

    else:
        return None  # Si no hay suficientes picos, devolvemos None

def calcular_camino_optimo(matriz_correlacion, umbral_correlacion):
    """
    Calcula el camino óptimo de periodos a partir de una matriz de correlaciones.

    Parameters:
    - matriz_correlacion: numpy.ndarray
        Matriz de correlación entre los periodos.
    - umbral_correlacion: float
        Umbral mínimo de correlación para considerar un periodo.

    Returns:
    - mejor_camino: list
        Lista con el índice de los periodos en el camino óptimo.
    - mejor_puntuacion: float
        Puntuación promedio del camino óptimo.
    """
    num_periods = matriz_correlacion.shape[0]
    periodos_confianza = np.where(np.max(matriz_correlacion, axis=1) >= umbral_correlacion)[0]
    
    mejor_camino = []
    mejor_puntuacion = 0

    # Iterar sobre cada periodo de confianza como punto de inicio
    for inicio in periodos_confianza:
        camino_actual = [inicio]
        puntuacion_total = 0
        periodo_actual = inicio  # Mantener el periodo actual

        while True:
            # Obtener las correlaciones del periodo actual
            correlaciones = matriz_correlacion[periodo_actual]
            # Filtrar los periodos a la derecha que cumplen el umbral
            candidatos = np.where(correlaciones[periodo_actual + 1:] >= umbral_correlacion)[0] + periodo_actual + 1
            
            # Si no hay más candidatos, terminamos
            if not candidatos.size:
                break
            
            # Encontrar el candidato con la máxima correlación
            siguiente = candidatos[np.argmax(correlaciones[candidatos])]
            camino_actual.append(siguiente)
            puntuacion_total += correlaciones[siguiente]
            periodo_actual = siguiente  # Actualizar el periodo actual

        # Calcular la puntuación promedio
        puntuacion_promedio = puntuacion_total / len(camino_actual)
        
        # Actualizar el mejor camino si es necesario
        if puntuacion_promedio > mejor_puntuacion:
            mejor_puntuacion = puntuacion_promedio
            mejor_camino = camino_actual

    return mejor_camino, mejor_puntuacion

def calcular_camino_optimo_mejorada(matriz_correlacion, umbral_correlacion):
    """
    Calcula el camino óptimo de periodos a partir de una matriz de correlaciones.

    Parameters:
    - matriz_correlacion: numpy.ndarray
        Matriz de correlación entre los periodos.
    - umbral_correlacion: float
        Umbral mínimo de correlación para considerar un periodo.

    Returns:
    - mejor_camino: list
        Lista con el índice de los periodos en el camino óptimo.
    - mejor_puntuacion: float
        Puntuación promedio del camino óptimo.
    """
    num_periods = matriz_correlacion.shape[0]
    periodos_confianza = np.where(np.max(matriz_correlacion, axis=1) >= umbral_correlacion)[0]
    
    # Si no hay periodos de confianza, devolver el primer periodo como el mejor camino
    if periodos_confianza.size == 0:
        return [0], 0  # Retorna el primer periodo y puntuación 0

    mejor_camino = []
    mejor_puntuacion = 0

    # Iterar sobre cada periodo de confianza como punto de inicio
    for inicio in periodos_confianza:
        camino_actual = [inicio]
        puntuacion_total = 0
        periodo_actual = inicio  # Mantener el periodo actual

        while True:
            # Obtener las correlaciones del periodo actual
            correlaciones = matriz_correlacion[periodo_actual]
            # Filtrar los periodos a la derecha que cumplen el umbral
            candidatos = np.where(correlaciones[periodo_actual + 1:] >= umbral_correlacion)[0] + periodo_actual + 1
            
            # Si no hay más candidatos, terminamos
            if not candidatos.size:
                break
            
            # Encontrar el candidato con la máxima correlación
            siguiente = candidatos[np.argmax(correlaciones[candidatos])]
            camino_actual.append(siguiente)
            puntuacion_total += correlaciones[siguiente]
            periodo_actual = siguiente  # Actualizar el periodo actual

        # Calcular la puntuación promedio
        puntuacion_promedio = puntuacion_total / len(camino_actual) if len(camino_actual) > 1 else 0
        
        # Actualizar el mejor camino si es necesario
        if puntuacion_promedio > mejor_puntuacion:
            mejor_puntuacion = puntuacion_promedio
            mejor_camino = camino_actual

    # Si mejor_camino está vacío, seleccionar el primer periodo
    if not mejor_camino:
        mejor_camino = [0]

    return mejor_camino, mejor_puntuacion
