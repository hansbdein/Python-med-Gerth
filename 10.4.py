# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:09:30 2021
def bitonic_min(L):
    
    if f(mid):
        return binary_search(f,low,mid)
    else:
        return binary_search(f,mid,high)

@author: Hans
"""

def binary_search(f,low,high):
    
    if high-low==1: return high    
    
    mid=(low+high)//2
    return binary_search(f,low,mid) if f(mid) else binary_search(f,mid,high)
    

def local_min(f,low,high):
    
    return binary_search(lambda x: f(x) < f(x + 1),low,high)

print(binary_search(lambda x: x * x >= 1000, 0, 1000))    
    
    
print(local_min(lambda x: (x - 3.5) ** 2 - 7 * x, -1000, 1000))
    

