"""
Proyecto AYNHO: Modelado de Paisajes de Energía Atractora
Autor: Isaicarlos (Trujillo, Perú)

Este script simula la trayectoria de un pensamiento en un potencial de doble pozo
utilizando la ecuación de Langevin para modelar el conflicto cognitivo.
"""

import numpy as np
import matplotlib.pyplot as plt

# Definición del potencial V(x) = 0.5*x^4 - 4*x^2
def mental_potential(x):
    return 0.5 * x**4 - 4 * x**2 

# Gradiente negativo (Fuerza restauradora)
def force(x):
    return -(2 * x**3 - 8 * x)

# Parámetros de simulación estocástica
dt = 0.01
steps = 1000
x = 0.1 # Estado de incertidumbre inicial
sigma = 1.2 # Ruido sináptico (Confusión)

history = []
for _ in range(steps):
    # Integración de Euler-Maruyama
    dx = force(x) * dt + sigma * np.sqrt(dt) * np.random.normal()
    x += dx
    history.append(x)

# Visualización para el portafolio
plt.figure(figsize=(10, 5))
plt.plot(history, color='blue')
plt.title(f"Dinámica del Pensamiento con Ruido Sigma = {sigma}")
plt.xlabel("Tiempo"); plt.ylabel("Estado Mental")
plt.show()
