# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:13:12 2021

@author: Hans
"""
import numpy as np
import matplotlib.pyplot as plt

L = np.array([(2, 3), (5, 7), (4, 10), (10, 15), (2.5, 5), (8, 4), (9, 10), (6, 6)])
x = L[:,0]
y = L[:,1]





i=1

while True:

    i+=1
    polycoff=np.polyfit(x,y,i)
    print(y-np.polyval(polycoff,x))
    if all(abs(y-np.polyval(polycoff,x))<1):
        break
    


plt.plot(x,y,'r.')
fx=np.linspace(1,10,1000)
plt.plot(fx,np.polyval(polycoff,fx))