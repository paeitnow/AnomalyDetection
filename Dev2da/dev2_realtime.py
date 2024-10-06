import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('graf_periodica.csv')
timestamps = data['timestamp']
values = data['value']

class DetectDerivadaSegunda:
    def __init__(self):
        self.v = [None, None, None]
        self.index = 0
        self.mean = 0;
        self.std = 0;

    def detect_value(self, new_value):
        self.v[self.index % 3] = new_value
        self.index += 1

        #devolvemos 0 en los 3 primeros valores pq necesitamos minimo 3 para calcular la 2da derivada
        if self.index < 3:
            return 0
        
        v0 = self.v[(self.index - 3) % 3]
        v1 = self.v[(self.index - 2) % 3]
        v2 = self.v[(self.index - 1) % 3]
        d1v1 = v1 - v0
        d1v2 = v2 - v1
        d2v = d1v2 - d1v1 #valor de la derivada en el punto v1

        meanp = (self.mean*(self.index-1)+d2v)/self.index
        stdp = ((((self.std**2)*(self.index-1)) + abs( d2v - self.mean)**2)/self.index)**0.5

        k=10
        threshold = meanp + k * stdp
        if d2v > threshold or d2v < (-threshold):
            return 1
        else:
            self.mean = meanp
            self.std = stdp
            return 0

d2v = DetectDerivadaSegunda()
anomalies = []
detect=[]


for i, valor in enumerate(values):
    detection = d2v.detect_value(valor)
    detect.append(detection)
    if detection == 1:
        anomalies.append(i)

plt.plot(timestamps, values, label='Valores', color='blue')
plt.scatter(timestamps[anomalies], values[anomalies], color='red', label='Anomalías Detectadas')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.title('Detección de Anomalías usando Derivada segunda')
plt.show()
