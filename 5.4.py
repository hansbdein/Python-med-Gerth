# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:58:58 2021

@author: Hans
"""

L=[[0,3,6,9],[1,2,3,4],[10,8,6,4,2]]






#flat = [ x for x in L[i][j] for i in range(len(L)) for j in range(len(L[i])) ]

flat=[]
#for i in range(len(L)): flat+=(L[i])
for l in L: flat +=l
print(flat)
    
    