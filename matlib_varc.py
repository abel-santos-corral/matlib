import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Define the range of the variable
x = np.arange(-5.0, 10.1, 0.1)

# Define membership functions (using trapmf for four-point definitions)
VL = fuzz.trapmf(x, [-5, -5, -4, -2])      # Very Low (VL)
L  = fuzz.trapmf(x, [-4, -2, 0, 4])      # Low (L) - Now Correct
M  = fuzz.trapmf(x, [0, 2, 2, 4])     # Medium (M) - Now Correct
H  = fuzz.trapmf(x, [2, 4, 10, 10])   # High (H)

# Plot membership functions
plt.figure(figsize=(8,5))
plt.plot(x, VL, 'b', linewidth=2, label="VL (Very Low)")
plt.plot(x, L, 'g', linewidth=2, label="L (Low)")
plt.plot(x, M, 'r', linewidth=2, label="M (Medium)")
plt.plot(x, H, 'c', linewidth=2, label="H (High)")

# Graph settings
plt.xlabel('VarC')
plt.ylabel('Membership Degree')
plt.title('Corrected Membership Functions of VarC')
plt.legend(loc="best")
plt.grid()
plt.show()
