# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:41:50 2021

@author: Hans
"""

def bitonic_min(L):
    
    def bitonic_inner(bot,top):
        mid=(bot+top)//2
        
        if L[mid]>L[mid+1]:
            return bitonic_inner(mid,top)
        elif L[mid]>L[mid-1]:
            return bitonic_inner(bot,mid)
        else: return L[mid]
    
    return bitonic_inner(1,len(L)-2)
