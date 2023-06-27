# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 12:41:54 2021

@author: Hans
"""

print('what are the start and end points of the first interval?')


while True:
    a = int(input())
    b = int(input())
    if a>=b:
        print("invalid interval, try again")
    else: break
    
print('what are the start and end points of the second interval?')


while True:
    c = int(input())
    d = int(input())
    if c>=d:
        print("invalid interval, try again")
    else: break



if b<c or d<a:
    print(str([a,b]) + ' and ' + str([c,d]) + ' do not overlap')
else:
    print(str([a,b]) + ' and ' + str([c,d]) + ' overlap in the interval' + str([max(a,c),min(b,d)]) )
    





