import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Define the range of the variable
x = np.arange(0, 15.1, 0.1)

# Define membership functions (using trapmf for four-point definitions)
VL = fuzz.trapmf(x, [0, 0, 2, 3])      # Very Low (VL)
L  = fuzz.trapmf(x, [0, 3, 4, 7])      # Low (L)
M  = fuzz.trapmf(x, [5, 7, 9, 10])     # Medium (M)
H  = fuzz.trapmf(x, [9, 10, 12, 15])   # High (H)
VH = fuzz.trapmf(x, [12, 13, 15, 15])  # Very High (VH)

# Punto a evaluar
x_query = 5.5

# Calcular grado de pertenencia de x_query en cada función
mu_VL = fuzz.interp_membership(x, VL, x_query)
mu_L  = fuzz.interp_membership(x, L, x_query)
mu_M  = fuzz.interp_membership(x, M, x_query)
mu_H  = fuzz.interp_membership(x, H, x_query)
mu_VH = fuzz.interp_membership(x, VH, x_query)

# Mostrar solo las funciones donde hay pertenencia > 0
memberships = {
    "VL (Very Low)": mu_VL,
    "L (Low)": mu_L,
    "M (Medium)": mu_M,
    "H (High)": mu_H,
    "VH (Very High)": mu_VH
}

print(f"Grados de pertenencia para x = {x_query}:")
for label, value in memberships.items():
    if value > 0:
        print(f"  {label}: {value:.3f}")

# Plot membership functions
plt.figure(figsize=(8,5))
plt.plot(x, VL, 'b', linewidth=2, label="VL (Very Low)")
plt.plot(x, L, 'g', linewidth=2, label="L (Low)")
plt.plot(x, M, 'r', linewidth=2, label="M (Medium)")
plt.plot(x, H, 'c', linewidth=2, label="H (High)")
plt.plot(x, VH, 'm', linewidth=2, label="VH (Very High)")

# Marcar el punto evaluado en la gráfica
plt.axvline(x_query, color='k', linestyle='--', alpha=0.6, label=f"x={x_query}")
plt.scatter([x_query]*2, [mu_L, mu_M], color='black', zorder=3)

# Graph settings
plt.xlabel('VarA')
plt.ylabel('Membership Degree')
plt.title('Corrected Membership Functions of VarA')
plt.legend(loc="best")
plt.grid()
plt.show()
