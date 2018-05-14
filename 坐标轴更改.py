#!/usr/bin/python
# -*- coding:utf-8 -*-
#####主要是对x,y轴进行更改，包括坐标轴上点注释和坐标轴的位置
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,50)
y1=10*x**2+x*3+2
y2=3*x**3-x**2+6*x-8
plt.figure(num=0 ,figsize=(8 ,6))
plt.plot(x,y1,color='green',linewidth=3.0,label='y1')
plt.plot(x,y2,color='yellow',linewidth=2.0,label='y2')
plt.legend(loc='lower right')
#改坐标轴上的值
new_ticks=np.arange(-2,3)
plt.xticks(new_ticks)
plt.yticks([-100,-50,0,50,100],[r'$very\ bad$',r'$bad$',r'$normal$',r'$good$',r'$very\ good$'])

#改坐标轴位置
ax=plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

plt.show()