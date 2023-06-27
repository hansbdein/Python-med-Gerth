# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 10:56:27 2021

@author: Hans
"""
from time import time, sleep


while True:
    inp = input("How large should the table be: ")
    try:
        n=int(inp)
        break
    except ValueError:
        print('Please enter a whole number ')
        
    
print('')    
print('*',' '*(len(str(n))-1), end = '| ')


k=0

space = 1+len(str(n**2-n))



while k<n+1:
    print(k, end = ' '*(space-len(str(k))))
    k+=1
    
print(' ')

print('-'*(space*(n+2)))






i=0
while i<n+1:
    j=0
    print(i,' '*(len(str(n))-len(str(i))), end = '| ')
    while j<n+1:
        t=j*i
        print(t, end = ' '*(space-len(str(t))))
        sleep(0.1)
        j+=1
    print('')
    i+=1
