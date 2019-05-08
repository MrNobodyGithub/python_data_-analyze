import numpy as np 
import matplotlib.pyplot as plt 

x1 = [1,5,9]
x2 = [2,6,11]
x3 = [4,8,12]
 

y1 = [1,2,3]#x1 * 3
y2 = [2,3,4]#x2 * 2
y3 = [5,6,7]#x3 * 1

plt.bar(x1,y1)
plt.bar(x2,y2,color='g')
plt.bar(x3,y3,color='c')

plt.title('bar graph')
plt.xlabel('x')
plt.ylabel('y')
# plt.plot()
plt.show()
