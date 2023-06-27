# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:07:26 2021

@author: Hans
"""



from scipy.optimize import minimize

import matplotlib.pyplot as plt

import numpy as np


def f(x):
    return 100*np.power(x-3,2)+np.power(np.exp(1),x)


xm=minimize(f,3).x

x=np.linspace(0,10,1000)


plt.plot(x,f(x))
plt.plot(xm,f(xm),'r.')

print(xm)