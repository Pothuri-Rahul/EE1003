import numpy as np
import matplotlib.pyplot as plt

# Define the equations
def eq1(l):
    return (3*l - 6) / 5

def eq2(l):
    return (61 - 2*l) / 3

# Generate values for l
l_values = np.linspace(0, 20, 400)

# Generate corresponding b values for both equations
b1_values = eq1(l_values)
b2_values = eq2(l_values)

# Create the plot
plt.figure(figsize=(8,6))
plt.plot(l_values, b1_values, label=r'$3l - 5b = 6$', color='blue')
plt.plot(l_values, b2_values, label=r'$2l + 3b = 61$', color='red')

# Highlight the intersection point
plt.plot(17, 9, 'go', label='Intersection (17, 9)')

# Set plot labels and title
plt.xlabel('l')
plt.ylabel('b')
plt.legend()

# Show grid
plt.grid(True)

# Save the plot as a PNG file
plt.savefig('plot.png')

# Display the plot
plt.show()

