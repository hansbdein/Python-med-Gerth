# -*- coding: utf-8 -*-
"""
Make a function that can take any number of arguments, and returns the sum of the squares of the values, i.e. square_sum(x1,x2,x3) returns x12+ x22+ x32.

> square_sum()
0
> square_sum(3,4,5)
50
> square_sum(1,2,3,4,5,6,7,8,9,10)
385
Given a list L, e.g. L = [1,2,3,4], use your square_sum function to compute the sum of squares of the values in L:
Hint. Use a * to indicate an arbitrary argument list.
"""

def square_sum(*X): return sum(x**2 for x in X)

L = [1,2,3,4]

print(square_sum(*L))