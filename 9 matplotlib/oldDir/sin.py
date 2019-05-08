import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0,3 * np.pi, 0.1)
y = np.sin(x)
plt.title('sin')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y)
plt.show()



 