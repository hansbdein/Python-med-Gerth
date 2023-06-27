# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 15:52:02 2021

@author: Hans
"""
import matplotlib.pyplot as plt





from math import e



minlim=0
maxlim=10

points=1000


x=[]
y=[]


for i in range(points+1):
    
    x+=[i/1000*(maxlim-minlim)+minlim]

    y+=[100*(x[i] - 3)**2+e**(x[i])]


plt.plot(x,y)



plt.figure()



x=[x/100 for x in range(1001)]
y=[100*(xn-3)**2+e**xn for xn in x]
plt.plot(x,y)






plt.figure()



import numpy as np

x=np.linspace(0,10,1001)



def f(x):
    return 100*np.power(x-3,2)  +  np.exp(x)



plt.plot(x,f(x))








