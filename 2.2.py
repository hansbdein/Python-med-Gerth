# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:05:08 2021

@author: Hans
"""
print('how many numbers do you want to add?')

k = int(input())

x=[[]]*k
print( )
print('please enter these numbers')
i = 0
while i < k:  
    x[i] = int(input())
    i += 1
    
    
    
print( )
print('=' + str(sum(x)))