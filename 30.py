# -*- coding: utf-8 -*-
"""
Created on Mon May 23 15:21:57 2022

@author: Hans
"""
import matplotlib.pyplot as plt
import numpy as np
from random import randint

#print(randint(1,6))
#Risiko for at slå mod selv 1/((5/6)**6+1)

tsips=[]


for games in range(10000):
    L=[randint(1,6) for n in range(6)]
    sips=0
    while 1 in L:
        sips+=len([1 for n in L if n==1])
        L=[randint(1,6) for n in L if n!=1]
        if not L:
            L=[randint(1,6) for n in range(6)]
    
    tsips.append(sips)
    
print(max(tsips))
plt.figure() 
plt.bar(range(0,7),np.histogram(tsips,bins=range(0,8))[0]/1000)
plt.figure()
plt.bar(range(7,13),np.histogram(tsips,bins=range(7,14))[0]/1000)