# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:43:45 2021

@author: Hans
"""
from time import sleep


def subsets(l,index=0):
    if len(l)>index:
        
        return subsets(l,index+1) + subsets(l[0:index]+l[index+1:],index)
    else: return [l]
    
    

print(subsets([1,2,3,4]))
#def subsets(l):
    