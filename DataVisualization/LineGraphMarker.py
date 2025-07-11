import matplotlib.pyplot as plt
import numpy as np

# Define x-axis values
x = [1,2,3,4,5,6,7,8,9,10]

# Define y-axis values
y = [10,20,30,40,50,55,45,80,90,99]

# Plot the line graph with markers
# 'o--c' means circle markers, dashed line, cyan color
# ms=15 sets marker size, mec='r' sets marker edge color to red, mfc='b' sets marker face color to blue
plt.plot(x, y, 'o--c', ms=15, mec='r', mfc='b')

# Display the plot
plt.show()