# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:55:03 2019

@author: a621587
"""

def sigmoid(x, derivative=False):
    sigm = 1. / (1. + np.exp(-x))
    if derivative:
        return sigm * (1. - sigm)
    return sigm

def ReLU(x, derivative=False):
    if derivative:
        return 1. * (x > 0)
    return x * (x > 0)

import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure(figsize=plt.figaspect(2.))
fig.suptitle('A tale of 2 subplots')

x = np.arange(-4, 4, 0.1)
y = np.arange(-4, 4, 0.1)
#print(x)

af_sin = np.sin(x)
af_tanh = np.tanh(x)
af_sigm = sigmoid(x)
af_ReLu = ReLU(x)

ax = fig.add_subplot(2, 1, 1,title='Activation Functions')


#ax.plot(x, af_sin, label='sin')
ax.plot(x, af_tanh,'b--', label='tanh')
ax.plot(x, af_sigm,'k--', label='sigmoid')
ax.plot(x, af_ReLu,'g--', label='ReLu', markerfacecolor='green')
ax.grid(True)

plt.xlabel('X')
plt.ylabel('Y')

plt.legend(loc='upper left', shadow='true', fancybox='true', title='Legend')


ax = fig.add_subplot(2, 1, 2, projection='3d',title='Gradient')
x,y = np.meshgrid(x,y)
z = x**2 + y**2

ax.plot_surface(x,y,z)
plt.show()
