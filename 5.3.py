# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:58:58 2021

@author: Hans
"""

L=[[0,3,6,9],[1,2,3,4],[10,8,6,4,2]]

def my_zip(L):
    Lshort=min([len(l) for l in L])
    
    NewL=[ [ 0 for i in range(len(L)) ] for j in range(Lshort) ]
    #NewL=[([[]]*len(L))]*Lshort
    for i in range(len(L)):
        for j in range(Lshort):
            NewL[j][i]=L[i][j]
    return NewL

b=my_zip(L)


