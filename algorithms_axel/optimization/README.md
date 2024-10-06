# Optimization

Esta carpeta contiene algoritmos para optimización de funciones, útiles en la búsqueda de mínimos o máximos de una función objetivo, ya sea para ajustar parámetros o para encontrar soluciones óptimas en problemas de decisión.

## Contenido de la carpeta

### 1. `gradient_descent.py`

Este script implementa el algoritmo de descenso de gradiente, un método iterativo para minimizar funciones, comúnmente utilizado en optimización y aprendizaje automático.

#### Descripción:
- **Entrada:** Una función objetivo, su gradiente, una tasa de aprendizaje, y el número de iteraciones.
- **Salida:** El mínimo local de la función objetivo tras ejecutar el algoritmo.

### 2. `simulated_annealing.py`

Este archivo implementa el método de recocido simulado (simulated annealing), un algoritmo probabilístico para encontrar la solución óptima global en problemas de optimización, incluso en funciones con múltiples mínimos locales.

#### Descripción:
- **Entrada:** Una función objetivo y los parámetros del algoritmo (temperatura inicial, tasa de enfriamiento, etc.).
- **Salida:** El mejor valor encontrado para la función objetivo.

## Aplicaciones

- **Optimización de funciones:** para encontrar parámetros óptimos en problemas de ingeniería, economía y ciencias aplicadas.
- **Entrenamiento de modelos de machine learning:** para minimizar funciones de pérdida.
