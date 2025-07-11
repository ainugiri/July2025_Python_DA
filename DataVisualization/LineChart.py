import matplotlib.pyplot as plt  # Import the matplotlib library for plotting
import numpy as np  # Import numpy for numerical operations (not used here)

x = [1,2,3,4,5,6,7,8,9,10]  # Define x-axis values
y = [10,20,30,40,50,55,45,80,90,99]  # Define y-axis values


y1 = [15,30,50,60,75,90,105,130,140,150]
y2 = [12,24,36,48,60,72,84,96,108,120]
plt.plot(x,y,'o')  # Plot the line chart with x and y values
plt.plot(x,y1)
plt.plot(x,y2)


#First Graph

#second
plt.figure()
plt.plot([1,2,3],[25,50,70])
plt.title("Second Figure")

#Third Figure
plt.figure()
plt.plot([1,2,3],[10,20,30])
plt.title("Third Figure")

plt.show()