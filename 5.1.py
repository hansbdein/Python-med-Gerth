# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:58:41 2021

@author: Hans
"""

poly=(5, 0, -2, 3)
x=7

print(sum([coff*x**p for (p,coff) in enumerate(poly)]))