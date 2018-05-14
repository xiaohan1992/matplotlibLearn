#!/usr/bin/python
# -*- coding:utf-8 -*-
### figure就是一张图，每个figure下面的内容，就是图像的内容，可以一次弄好几个图，都用plt.show（）显示
##########
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-3,3,100)
y1=10*x**2+x*3+2
y2=3*x**3-x**2+6*x-8
plt.figure(num=0 ,figsize=(8 ,6))
plt.plot(x,y1,color='green',linewidth=3.0,label='y1')
plt.plot(x,y2,color='yellow',linewidth=2.0,label='y2')
plt.legend(loc='lower right')
plt.figure(num=1,figsize=(6,4))
plt.plot(x,y2)
plt.show()