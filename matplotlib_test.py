import numpy as np
import matplotlib.pyplot as plt

 plt.style.use("seaborn-whitegrid")
x = np.linspace(0, 2*np.pi,20)
plt.plot(x, np.sin(x), c='r')
plt.plot(x, np.cos(x), c='b')
plt.show()



x = np.linspace(0, 50,50)
plt.scatter(x, x**2, cmap='hot', c='y')
plt.axis([-20,70,-200,3000])
plt.colorbar()
plt.show()



x = np.linspace(0, 20,10)
y1 = x
y2 = x+1
plt.barh(x, y1, height = 0.5, label='usa', color='y')
plt.barh(x, y2, height = 0.5, label='prc', left=y1)
plt.legend(loc='best', frameon='True', fontsize=12)
plt.show()