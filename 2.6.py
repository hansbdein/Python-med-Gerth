# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:23:51 2021

@author: Hans
"""
import time as t




a = int(input())
b=int(a)

start=t.time()

print('Factors are')
print('1')
prime=True
i=2
while i<=b**0.5:
    r=b%i
    if r==0:
        b=b//i
        print(i)
        prime=False
    else:    
        i+=1
print(b)    
    
if prime:
    print(str(a),' is prime')
else:
    print(str(a)) 
    

print('completed in', (t.time()-start)/1000, 'milliseconds')