"""
Proyecto AYNHO: Sincronización de Redes Neuronales
Modelo de Kuramoto para osciladores acoplados.

Este script simula cómo diferentes regiones cerebrales alcanzan la coherencia
informativa en función de la constante de acoplamiento (K).
"""

import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
N = 10  # Número de áreas cerebrales o neuronas
steps = 1000
dt = 0.05
K = 1.5  # Fuerza de acoplamiento (Ajustar para ver transiciones de fase)

# Frecuencias naturales aleatorias (Distribución de Lorentz/Gauss)
omega = np.random.normal(0, 1, N)
theta = np.random.uniform(0, 2*np.pi, N)

history = np.zeros((steps, N))

for t in range(steps):
    d_theta = np.zeros(N)
    for i in range(N):
        # Interacción mutua entre osciladores
        interaccion = np.sum(np.sin(theta - theta[i]))
        d_theta[i] = omega[i] + (K / N) * interaccion
    
    theta += d_theta * dt
    history[t] = np.sin(theta) # Guardamos la fase proyectada

# Visualización de la coherencia
plt.figure(figsize=(10, 6))
plt.plot(history)
plt.title(f"Sincronización de Redes (Acoplamiento K = {K})")
plt.xlabel("Tiempo"); plt.ylabel("Amplitud de Oscilación (sin θ)")
plt.grid(alpha=0.3)
plt.show()
