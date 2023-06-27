# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:06:22 2021

@author: Hans
"""

i=0
n = int(input())

x = n

while i<1000:
    x=x-(x**2-n)/2/x
    i+=1
    
    if i<10:
        print(x)
    elif i<100 and i%10==0:
        print(x)
    elif i<1000 and i%100==0:
        print(x)
