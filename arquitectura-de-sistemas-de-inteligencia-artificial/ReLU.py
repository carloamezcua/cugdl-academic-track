'''
Función ReLU y su gráfica
'''

# Importación de librerías
import numpy as np
import matplotlib.pyplot as plt

# Función ReLU
def ReLU(x):
    return np.maximum(0, x)

# Datos
x = np.linspace(-10, 10, 500)
y = ReLU(x)


# Gráfica
plt.figure(figsize=(8, 5))
plt.plot(x, y, color="blue", linewidth=2, label="ReLU(x)")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Función ReLU")
plt.xlabel("x")
plt.ylabel("ReLU(x)")
plt.legend()
plt.grid(True)
plt.savefig("relu.png", dpi=150, bbox_inches="tight")
plt.show()
