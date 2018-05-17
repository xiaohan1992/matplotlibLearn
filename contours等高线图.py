#!/usr/bin/python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function
    return (1-x/2+x**4+y**3)*np.exp(-x**2-y**2)

n=256
x=np.linspace(-3,3)
y=np.linspace(-3,3)
# 把x,y变成网格的输入值
X,Y=np.meshgrid(x,y)
# plt.contourf()用来将网格分块 10是分块多少
plt.contourf(X,Y,f(X,Y),10,alpha=0.75,cmap=plt.cm.cool)
# plt.contour()用来将分块的线画出来
C=plt.contour(X,Y,f(X,Y),10,colors='black',linewidth=.5)
# plt.clabel是把等高线的值打出来
plt.clabel(C,inline=True,fontsize=10)


plt.xticks(())
plt.yticks(())
plt.show()