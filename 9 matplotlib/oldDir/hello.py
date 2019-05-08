import numpy as np 
from matplotlib import pyplot as plt 
import random
import matplotlib
 

# 中文显示
font_ch = matplotlib.font_manager.FontProperties(fname="SimHei.ttf") 

plt.rcParams['font.family']=['STFangsong']

x = np.arange(1,11) 
y =  2  * x +  5 
# Matplotlib 
plt.title(" matplotlib 类型 颜色",fontProperties=font_ch) 
plt.xlabel("x axis caption") 
# /&lt','/&gt',,'&#124'
char_list=['-','--','-.',':','.',',','o','v','^','1','2','3','4','s','p','*',
			'h','H','+','x','D','d','_']

plt.ylabel("y axis caption \n" + ''.join(str(i)+' ' for i in char_list))


color_list = ['b','g','r','c','m','y','k','w']
 
count = 7 #char_list.count - 1

for char in char_list:
	color = color_list[random.randint(0,count)]
	plt.plot(x,y,char+color)
	y += 8
 
plt.show()