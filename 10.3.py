# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 15:09:12 2021

@author: Hans
"""


def f(word):
    L=[]
    
    def duplicatecheck(t):
        #len(list(set(list(t))))
        return len([L.append(str.lower(x)) for x in t if x in L])
    
    return duplicatecheck(word)
    
def str_sort(L):
    return sorted(L,key=f)


