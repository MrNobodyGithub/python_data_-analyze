import numpy as np 
import matplotlib.pyplot as plt 

x = np.arange(0, 3 * np.pi, 0.1)

y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)

plt.subplot(3,1,1)
plt.title('sin')
plt.plot(x,y_sin)

plt.subplot(3,1,2)
plt.title('cos')
plt.plot(x,y_cos)

plt.subplot(3,1,3)
plt.title('tan')
plt.plot(x,y_tan)

plt.show();


