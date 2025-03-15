import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir los rangos de las variables
x_vara = np.arange(0, 15.1, 0.1)
x_varb = np.arange(0, 10.1, 0.1)
x_varc = np.arange(-5.0, 10.1, 0.1)
x_out = np.arange(0, 10.1, 0.1)

# Definir las funciones de membresía para cada variable
VL_vara = fuzz.trapmf(x_vara, [0, 0, 2, 3])
L_vara = fuzz.trapmf(x_vara, [0, 3, 4, 7])
M_vara = fuzz.trapmf(x_vara, [5, 7, 9, 10])
H_vara = fuzz.trapmf(x_vara, [9, 10, 12, 15])
VH_vara = fuzz.trapmf(x_vara, [12, 13, 15, 15])

L_varb = fuzz.trapmf(x_varb, [0, 0, 1, 4])
M_varb = fuzz.trapmf(x_varb, [1, 5, 5, 7])
H_varb = fuzz.trapmf(x_varb, [6, 9, 10, 10])

VL_varc = fuzz.trapmf(x_varc, [-5, -5, -4, -2])
L_varc = fuzz.trapmf(x_varc, [-4, -2, 0, 4])
M_varc = fuzz.trapmf(x_varc, [0, 2, 2, 4])
H_varc = fuzz.trapmf(x_varc, [2, 4, 10, 10])

L_out = fuzz.trapmf(x_out, [0, 0, 3, 6])
M_out = fuzz.trapmf(x_out, [4, 5, 5, 6])
H_out = fuzz.trapmf(x_out, [3, 7, 10, 10])

# Valores de entrada
input_vara = 5.5
input_varb = 3
input_varc = 3.5

# Calcular los grados de pertenencia para cada entrada
mf_vara = [fuzz.interp_membership(x_vara, VL_vara, input_vara),
           fuzz.interp_membership(x_vara, L_vara, input_vara),
           fuzz.interp_membership(x_vara, M_vara, input_vara),
           fuzz.interp_membership(x_vara, H_vara, input_vara),
           fuzz.interp_membership(x_vara, VH_vara, input_vara)]

mf_varb = [fuzz.interp_membership(x_varb, L_varb, input_varb),
           fuzz.interp_membership(x_varb, M_varb, input_varb),
           fuzz.interp_membership(x_varb, H_varb, input_varb)]

mf_varc = [fuzz.interp_membership(x_varc, VL_varc, input_varc),
           fuzz.interp_membership(x_varc, L_varc, input_varc),
           fuzz.interp_membership(x_varc, M_varc, input_varc),
           fuzz.interp_membership(x_varc, H_varc, input_varc)]

# Evaluación de reglas difusas (20 reglas)
activations = np.zeros_like(x_out)

rules = [
    (mf_vara[0], mf_varb[2], mf_varc[1], L_out),
    (mf_vara[0], mf_varb[2], mf_varc[2], L_out),
    (mf_vara[0], mf_varb[2], mf_varc[3], L_out),
    (mf_vara[1], mf_varb[0], mf_varc[0], L_out),
    (mf_vara[1], mf_varb[0], mf_varc[1], L_out),
    (mf_vara[1], mf_varb[0], mf_varc[2], M_out),
    (mf_vara[1], mf_varb[0], mf_varc[3], M_out),
    (mf_vara[1], mf_varb[1], mf_varc[0], L_out),
    (mf_vara[1], mf_varb[1], mf_varc[1], L_out),
    (mf_vara[1], mf_varb[1], mf_varc[2], L_out),
    (mf_vara[1], mf_varb[1], mf_varc[3], M_out),
    (mf_vara[1], mf_varb[2], mf_varc[0], L_out),
    (mf_vara[1], mf_varb[2], mf_varc[2], L_out),
    (mf_vara[2], mf_varb[0], mf_varc[0], L_out),
    (mf_vara[2], mf_varb[0], mf_varc[1], L_out),
    (mf_vara[2], mf_varb[0], mf_varc[2], L_out),
    (mf_vara[2], mf_varb[0], mf_varc[3], M_out),
    (mf_vara[2], mf_varb[1], mf_varc[0], L_out),
    (mf_vara[2], mf_varb[1], mf_varc[1], M_out),
    (mf_vara[2], mf_varb[1], mf_varc[2], M_out)
]

for rule in rules:
    activation_level = np.fmin(np.fmin(rule[0], rule[1]), rule[2])
    activation_output = np.fmin(activation_level, rule[3])
    activations = np.fmax(activations, activation_output)

# Cálculo del valor nítido
out_defuzzified = fuzz.defuzz(x_out, activations, 'centroid')

# Visualización
plt.figure(figsize=(8, 5))
plt.plot(x_out, L_out, 'g', linewidth=2, label='L (Low)')
plt.plot(x_out, M_out, 'r', linewidth=2, label='M (Medium)')
plt.plot(x_out, H_out, 'c', linewidth=2, label='H (High)')
plt.fill_between(x_out, 0, activations, color='orange', alpha=0.7)
plt.axvline(out_defuzzified, color='black', lw=2, linestyle='--', label=f'Output = {out_defuzzified:.4f}')
plt.title('Output Membership Function and Resulting Aggregation')
plt.xlabel('Output Variable (Out)')
plt.ylabel('Membership Degree')
plt.legend(loc='best')
plt.grid(True)
plt.show()

# Mostrar el resultado nítido
print(f'Valor nítido resultante: {out_defuzzified:.4f}')
