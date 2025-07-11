import matplotlib.pyplot as plt
import numpy as np
x1= [1,2,3,4,5,6]
y1=[2,4,8,6,8,1]
fig,ax = plt.subplots()
ax.plot(x1,y1,marker='o')
ax.set_facecolor('lightyellow')
ax.grid(True)
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
plt.show()