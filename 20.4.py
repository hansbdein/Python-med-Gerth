# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 15:28:24 2021

@author: Hans
"""


def subsets(L):
    for i in range(2**len(L)):
        yield [L[y] for y, x in enumerate(format(i, "0"+str(len(L))+"b")) if int(x)]




def subset_sum(x,L):
    for subset in subsets(L):
        if sum(subset)==x: 
            yield subset
