# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 12:16:37 2021

@author: Hans
"""
import numpy as np

from scipy.optimize import linprog

c=np.array([350,300])
A_ub=np.array([[1,1],[9,6],[12,16],[-1,0],[0,-7]])
b_ub=np.array([200,1566,2880,-3,-7])

result=linprog(-c,A_ub=A_ub,b_ub=b_ub)

print(-result.fun)
print(result.x)