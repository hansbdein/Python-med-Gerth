# -*- coding: utf-8 -*-
"""
Write a function average2(x,y) that computes the average of x and y, i.e. (x+y)/2.
Write a function list_average(L) that computes the average of the numbers in the list L.
Write a function average(x1,...,xk) that takes an arbitray number of arguments (but at least one) and computes the average of x1, ..., xk.
Hint. Use a * to indicate an arbitrary argument list.
"""

def average2(x,y): return (x+y)/2

def list_average(L): return sum(L)/len(L)

def average(y,*x): return (y+sum(x))/(1+len(x))