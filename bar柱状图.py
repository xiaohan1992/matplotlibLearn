#!/usr/bin/python
# -*- coding:utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

n=12
X=np.arange(n)
Y1=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2=(1-X/float(n))*np.random.uniform(0.5,1.0,n)
# plt.bar()做柱状图
plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white')
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white')
# zip每一步输出两个值
for x,y in zip(X,Y1):
    # ha:horizontal alignmeter
    # plt.text(x+0.04,y+0.05,'%.2f'%y,ha='center',va='bottom')
    plt.text(x + 0.04, y + 0.05, '%.2f' % y,ha='center',va='bottom')
for x, y in zip(X,Y2):
    # ha:horizontal alignmeter
    plt.text(x + 0.04, -y - 0.05, '-%.2f' % y, ha='center', va='top')

plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())


plt.show()