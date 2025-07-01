import matplotlib.pyplot as plt
import numpy as np
x=np.array([5,7,4,2,17,2,9,4,11,12,9,6])
y=np.array([99,86,87,88,111,86,103,87,94,78,77,86])
colors=np.array([0,10,20,30,40,50,60,70,80,90,100,110])
plt.scatter(x,y,c=colors,cmap='viridis')
plt.show()