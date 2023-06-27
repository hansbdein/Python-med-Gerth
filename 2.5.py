# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 16:05:37 2021

@author: Hans
"""

a = int(input())

prime=True

i=2
while i<=a**0.5:
    r=a%i
    if r==0:
        print(str(i),' divides', str(a))
        prime=False
        break
    i+=1
if prime:
    print(str(a),' is prime')



    
    