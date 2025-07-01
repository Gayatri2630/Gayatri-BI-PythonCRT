import numpy as np 
import matplotlib as mp
import matplotlib.pyplot as plt 
#plot1:
x=np.array([0,1,2,3])
y=np.array([3,8,1,10])
plt.subplot(2,3,1)
plt.title("PLot-1")
plt.plot(x,y)
#plot2:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,3,2)
plt.title("Plot-2")
plt.plot(x,y)
#plot3:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,3,3)
plt.title("Plot-3")
plt.plot(x,y)

#plot4:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,3,4)
plt.title("Plot-4")
plt.plot(x,y)
#plot5:
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,3,5)
plt.title("Plot-5")
plt.plot(x,y)
#plot-6
x=np.array([0,1,2,3])
y=np.array([10,20,30,40])
plt.subplot(2,3,6)
plt.title("Plot-6")
plt.plot(x,y)
plt.suptitle("MY SHOP")
plt.show()