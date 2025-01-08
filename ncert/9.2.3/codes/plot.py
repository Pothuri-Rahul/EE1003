import numpy as np
import matplotlib.pyplot as plt
from ctypes import CDLL, c_double

# Load the shared library
lib = CDLL('./code.so')

# Define the function prototype
lib.fun.argtypes = [c_double, c_double, c_double, np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS'), np.ctypeslib.ndpointer(dtype=np.float64, flags='C_CONTIGUOUS')]
lib.fun.restype = None

# Allocate memory for the x and y values
x_vals = np.zeros(100, dtype=np.float64)
y_vals = np.zeros(100, dtype=np.float64)

# Initial values
x = 0.0
y = 1.0
h = 0.1

# Call the C function
lib.fun(x, y, h, x_vals, y_vals)

# Plot the results
plt.plot(x_vals, y_vals, label="Sim", color='red')

# Plot cos(x) for comparison
x_vals_cos = np.linspace(0, 10, 100)
plt.plot(x_vals_cos, np.cos(x_vals_cos), label="Theory", color='blue', linestyle='--')

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.savefig('fig.png')
plt.show()

