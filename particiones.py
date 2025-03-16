import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definimos el universo de discurso (0°C a 40°C)
x = np.linspace(0, 40, 400)

# Definimos las funciones de pertenencia usando skfuzzy
mu_frio = fuzz.trapmf(x, [0, 0, 15, 20])
mu_tibio = fuzz.trimf(x, [15, 25, 35])
mu_caliente = fuzz.trapmf(x, [25, 30, 40, 40])

# Calculamos la suma de pertenencias en cada punto para verificar la partición difusa
suma_pertenencias = mu_frio + mu_tibio + mu_caliente

# Graficamos las funciones de pertenencia
plt.figure(figsize=(10, 6))
plt.plot(x, mu_frio, label='Frío', color='blue')
plt.plot(x, mu_tibio, label='Tibio', color='green')
plt.plot(x, mu_caliente, label='Caliente', color='red')
plt.plot(x, suma_pertenencias, label='Suma de pertenencias', color='black', linestyle='dashed')

# Añadimos detalles al gráfico
plt.title('Partición Difusa para la Variable de Temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Grado de Pertenencia')
plt.legend(loc='upper right')
plt.grid(True)
#plt.show()
plt.savefig("particion_difusa.png")

# Verificamos si la suma es aproximadamente igual a 1 en todos los puntos
verificacion = np.allclose(suma_pertenencias, 1, atol=1e-2)
print("¿La partición es válida?:", verificacion)
