import matplotlib.pyplot as plt
import numpy as np
x1= [1,2,3,4,5,6]
y1=[2,4,8,6,8,1]

x2= [1,2,3,4,5,6]
y2=[5,10,15,20,25,30]


# colors =['red','green','blue','black','purple','orange']
# size = [100,120,80,70,75,90]
plt.scatter(x1,y1, color='blue', label='G1')
plt.scatter(x2,y2, color='red', label='G2')
plt.title('Scatter Plot')
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.show()
