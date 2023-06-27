# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 16:14:50 2021

@author: Hans
"""




def subsets_generator(S):
    if len(S) <= 0:
        yield []
    else:
        for s in subsets_generator(S[1:]):
            yield s
            yield [S[0]] + s
            
            
'''          

def permutations(L):
    if len(L) == 1:
        yield L
    else:
        for i in range(len(L)):          
            for l in permutations(L[:i] + L[i + 1:]):
                yield [L[i]] + l
                
'''         

           
def permutations(L):
    if len(L) == 1:
        yield L
    else:
        for i in range(len(L)):          
           yield from ([L[i]] + l for l in permutations(L[:i] + L[i + 1:]))
           
           

'''                
def permutations(L):
    if len(L) == 1:
        yield L
    else:
        yield from ([L[i]] + l for l in permutations(L[:i] + L[i + 1:])) for i in range(len(L)))
                
                                     '''