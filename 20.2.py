# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 14:12:12 2021

@author: Hans
"""

#a
def fib(n):
    
    n1, n2 =0,1                 
        
    for x in range(n):  
        
        n1, n2= n2, n1+n2       
        yield n1
            
            

print(list(fib(10)))

print(sum(fib(100)))



class Fibonacci:
    def __init__(self, n):
        self.n = n
        self.start = (0,1)
        
    def __iter__(self):
        return FibonacciIterator(self)
    
class FibonacciIterator:
    def __init__(self, fib):
        self.idx = 0
        self.fib = fib
        self.current = self.fib.start 
        self.n = self.fib.n
    
    def __next__(self):
        if self.idx >= self.fib.n:
                raise StopIteration
        self.idx += 1
        
        self.current = (self.current[1], sum(self.current))
 
        return self.current[0]
    
    def __iter__(self): # make iterator iterable
        return self
    
    
f = Fibonacci(5)


it = iter(f)


for _ in range(3):
      for x in f:
          print(x, end=' ')