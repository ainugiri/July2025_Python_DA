import matplotlib.pyplot as plt
import numpy as np
item_cat = ['COMPUTE','DATABASE','AI-ML']
Jan = [160,55,95]
Feb = [210,120,345]
Mar = [180,240,540]
x = np.arange(len(item_cat))        # label location
width = 0.4
plt.bar(x-width,Jan,    width, label='Jan',color='blue')
plt.bar(x,      Feb,    width, label='Feb',color='green')
plt.bar(x+width,Mar,    width, label='Mar',color='orange')
plt.title("Cloud service cost")
plt.xlabel("Services")
plt.ylabel('Cost per services')
plt.xticks(x,item_cat)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
