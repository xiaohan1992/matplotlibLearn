#!/usr/bin/python
# -*- coding:utf-8 -*-
# 绘制一个简单的直线
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,50)
print(x)

y=x**2+3*x-5
print(y)
x0=5
y0=x0**2+3*x0-5
print(y0)
plt.figure(num=0,figsize=(6,4))
plt.plot(x,y,color='b',linewidth=2.0)
plt.show()