# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:56:27 2021

while i<len(L)-1:
     
    i+=1
    
    if b<Ls[i][0]:
        L2.append([a,b])
        a=Ls[i][0]

    b=max(b,Ls[i][1]) 


@author: Hans
"""



L=[ [6, 10],[1, 3],[19,36], [2, 5], [8, 13],[14, 23]]

Ls=sorted(L)


a=Ls[0][0]
b=Ls[0][1]
L2=[]

for i in range(1,len(L)):
    
    if b<Ls[i][0]:
        L2.append([a,b])
        a=Ls[i][0]

    b=max(b,Ls[i][1])     
    
L2.append([a,b])

print(L2)

a=Ls[0][0]
b=Ls[0][1]

cursed=[[a,b] if b<Ls[i][0] else None for i in range(1,len(L))]

print(cursed)
