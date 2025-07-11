import matplotlib.pyplot as plt
import numpy as np

# Define x-axis values
overs = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# Define y-axis values
y = [10,20,30,40,50,55,45,80,90,99,104,110,115,128,130,135,147,151,160,168]
y1 = [8,5,13,20,28,36,48,50,55,70,80,90,100,110,111,128,137,149,157,169]
plt.subplot(1,2,1)
plt.plot(overs,y,color='r',linewidth='5')

plt.subplot(1,2,2)
plt.plot(overs,y1,color='b',linewidth='5')

f1 = {'family':'serif', 'color':'green','size':15}
f2 = {'family':'serif', 'color':'blue','size':20}
plt.xlabel("Overs",fontdict=f1)
plt.ylabel("Runs",fontdict=f1)
plt.title("Score Card",fontdict=f2,loc = 'center')
plt.plot(overs,y1,color='b',linewidth='3')
plt.grid(color='blue',linewidth=0.5,linestyle='dotted')
plt.show()
