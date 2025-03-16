import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import os

# Crear la carpeta 'fixtures' si no existe
os.makedirs('fixtures', exist_ok=True)

# Definimos las variables de entrada
VarA = ctrl.Antecedent(np.arange(0, 11, 1), 'VarA')
VarB = ctrl.Antecedent(np.arange(0, 11, 1), 'VarB')

# Definimos la variable de salida
VarOut = ctrl.Consequent(np.arange(0, 11, 1), 'VarOut')

# Funciones de pertenencia para VarA (3 términos)
VarA['terA1'] = fuzz.trimf(VarA.universe, [0, 0, 5])
VarA['terA2'] = fuzz.trimf(VarA.universe, [0, 5, 10])
VarA['terA3'] = fuzz.trimf(VarA.universe, [5, 10, 10])

# Funciones de pertenencia para VarB (4 términos)
VarB['terB1'] = fuzz.trimf(VarB.universe, [0, 0, 3])
VarB['terB2'] = fuzz.trimf(VarB.universe, [0, 3, 6])
VarB['terB3'] = fuzz.trimf(VarB.universe, [3, 6, 9])
VarB['terB4'] = fuzz.trimf(VarB.universe, [6, 9, 10])

# Funciones de pertenencia para VarOut (3 términos)
VarOut['VarOut1'] = fuzz.trimf(VarOut.universe, [0, 0, 5])
VarOut['VarOut2'] = fuzz.trimf(VarOut.universe, [0, 5, 10])
VarOut['VarOut3'] = fuzz.trimf(VarOut.universe, [5, 10, 10])

# Creamos las reglas
rules = []
combinations = [('terA1', 'terB1', 'VarOut1'), ('terA1', 'terB2', 'VarOut2'), ('terA1', 'terB3', 'VarOut2'),
                ('terA1', 'terB4', 'VarOut3'), ('terA2', 'terB1', 'VarOut1'), ('terA2', 'terB2', 'VarOut1'),
                ('terA2', 'terB3', 'VarOut2'), ('terA2', 'terB4', 'VarOut3'), ('terA3', 'terB1', 'VarOut1'),
                ('terA3', 'terB2', 'VarOut2'), ('terA3', 'terB3', 'VarOut3'), ('terA3', 'terB4', 'VarOut3')]

for comb in combinations:
    rules.append(ctrl.Rule(VarA[comb[0]] & VarB[comb[1]], VarOut[comb[2]]))

# Controlador difuso
system = ctrl.ControlSystem(rules)
simulator = ctrl.ControlSystemSimulation(system)

# Ejemplo de evaluación
simulator.input['VarA'] = 6.5
simulator.input['VarB'] = 4.0

# Computamos el resultado
simulator.compute()

# Mostramos el resultado
print(f'Resultado: {simulator.output['VarOut']}')

# Guardar las gráficas en la carpeta fixtures
VarA.view()
plt.savefig('fixtures/Tuplas_VarA.png')
plt.close()

VarB.view()
plt.savefig('fixtures/Tuplas_VarB.png')
plt.close()

VarOut.view()
plt.savefig('fixtures/Tuplas_VarOut.png')
plt.close()
