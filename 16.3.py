# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 23:15:08 2021

HANDIN 8 (longest common subsequence)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

Jeg lavede det første program direkte baseret på "The basic observation" 
som Gerth beskriver i opgaven. 
Derefter kopiered jeg den og ændre den til at returnere strings, og bruge key=len.



"""

def memoize(f):
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper


@memoize 
def LCS_length(x,y):
    if x=='' or y=='':
        return 0
    if x[-1]==y[-1 ]: 
        return 1 + LCS(x[:-1],y[:-1])    
    return max(LCS(x,y[:-1]),LCS(x[:-1],y))
        

@memoize 
def LCS(x,y):
    if x=='' or y=='':
        return ''
    if x[-1]==y[-1 ]: 
        return x[-1] + LCS(x[:-1],y[:-1])
    return max(LCS(x,y[:-1]),LCS(x[:-1],y),key=len)


print(LCS('abracadabra', 'azrael'))