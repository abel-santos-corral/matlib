import numpy as np
import matplotlib.pyplot as plt

# Definir la función de Yager
def yager_membership(x, c, a, w):
    return 1 - np.minimum(1, ((np.abs(x - c) / a) ** w))

# Rango de valores
x = np.linspace(-10, 10, 100)

# Parámetros
c, a = 0, 5  # Centro y radio
w_values = [0.5, 1, 2, 5, 10]  # Diferentes valores de w

# Graficar diferentes curvas
plt.figure(figsize=(8, 5))
for w in w_values:
    mu = yager_membership(x, c, a, w)
    plt.plot(x, mu, label=f'w={w}')

plt.xlabel("x")
plt.ylabel("Grado de Pertenencia")
plt.title("Funciones de Pertenencia de Yager con Diferentes w")
plt.legend()
plt.grid()
plt.show()
