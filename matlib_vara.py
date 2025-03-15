import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Define the range of the variable
x = np.arange(0, 15.1, 0.1)

# Define membership functions (using trapmf for four-point definitions)
VL = fuzz.trapmf(x, [0, 0, 2, 3])      # Very Low (VL)
L  = fuzz.trapmf(x, [0, 3, 4, 7])      # Low (L) - Now Correct
M  = fuzz.trapmf(x, [5, 7, 9, 10])     # Medium (M) - Now Correct
H  = fuzz.trapmf(x, [9, 10, 12, 15])   # High (H)
VH = fuzz.trapmf(x, [12, 13, 15, 15])  # Very High (VH)

# Plot membership functions
plt.figure(figsize=(8,5))
plt.plot(x, VL, 'b', linewidth=2, label="VL (Very Low)")
plt.plot(x, L, 'g', linewidth=2, label="L (Low)")
plt.plot(x, M, 'r', linewidth=2, label="M (Medium)")
plt.plot(x, H, 'c', linewidth=2, label="H (High)")
plt.plot(x, VH, 'm', linewidth=2, label="VH (Very High)")

# Graph settings
plt.xlabel('VarA')
plt.ylabel('Membership Degree')
plt.title('Corrected Membership Functions of VarA')
plt.legend(loc="best")
plt.grid()
plt.show()
