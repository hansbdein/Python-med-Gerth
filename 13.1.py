# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 09:29:41 2021

@author: Hans
"""


def add():
    x, y = input("Input two integers, separated by space: ").split()
 
    try:
        print('sum =',int(x)+int(y))
    
    except ValueError:
        print('invalid input') 
        add()
    
add() 
        
