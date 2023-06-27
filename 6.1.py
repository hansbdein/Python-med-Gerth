# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:55:00 2021

@author: Hans
"""

letters=['A', 'B', 'A', 'A', 'C', 'E', 'C']

hist={}
for letter in letters: 
    if letter not in hist:
        hist[letter] = 0
    hist[letter]+=1
    
print(hist.items())


D=dict()
for element in letters:
    D[element]=D.get(element,0)+1

print(hist.items())