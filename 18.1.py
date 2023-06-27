# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:45:18 2021

@author: Hans
"""

import numpy as np



A=np.array([[np.random.normal(0,1) for x in range(5)] for x in range(5)])

A=np.random.normal(0,1,(5,5))

A=np.random.randn(5,5)



B=np.linalg.inv(A)

np.array([[A[i][j] if abs(A[i][j])>10**(-14) else 0 for i in range(len(A))] for j in range(len(A[0]))])

def f(x):
    if -10**-14 < x < 10**-14:
        return 0
    return x
B = f(np.linalg.inv(A))


print(np.dot(A,B))

print(np.mean(A, axis=0))
print(np.mean(B, axis=0))
print(np.mean(A, axis=1))
print(np.mean(B, axis=1))

C=np.random.rand(100,100)

np.sum(C,1)


#sums=np.where(np.sum(C,1)>55,  np.sum(C,1),None)

sums=np.sum(C,1)

print([(i,sums[i]) for i in range(len(sums)) if sums[i]>55])