import ctypes
import numpy as np
import matplotlib.pyplot as plt

# Load the shared library (code.so)
lib = ctypes.CDLL('./code.so')

# Define the argument and return types of the function
lib.fun.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double,
                    ctypes.POINTER(ctypes.c_double), ctypes.POINTER(ctypes.c_double)]
lib.fun.restype = None  # The function does not return anything (void)

# Prepare ctypes arrays to store the results
x = (ctypes.c_double * 100)()  # Array to store x (time t) values
y = (ctypes.c_double * 100)()  # Array to store y (value p) values

# Call the function
lib.fun(0, 0, 0, x, y)

# Convert ctypes arrays to NumPy arrays for easier manipulation
x_array = np.array(x)
y_array = np.array(y)

# Plot the results
plt.plot(x_array, y_array, label="theoy", linestyle="-", color="blue")  # Line plot
plt.scatter(x_array, y_array,s=10, color="red", label="Sim")  # Add dots for each point

# Add labels, title, and legend
plt.xlabel("Time (t)")
plt.ylabel("Value (p)")
plt.title("Plot of y vs x with Data Points")
plt.legend()
plt.grid()

# Save the figure as a file (e.g., PNG, JPG, or PDF)
plt.savefig("plot.png", dpi=300, bbox_inches="tight")  # Save with high resolution

# Show the plot
plt.show()

