# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:58:16 2021

def cases(s):
    L=[]
    def incases(s):
        L.append(str.lower(s[0])+s[1:])    
        L.append(str.upper(s[0])+s[1:])
        if len(s)>1: incases(s[1:])
    incases(s)
    return L
    

@author: Hans
"""




def cases(s):
    if len(s)>1:
        return [str.lower(s[0])+ x for x in cases(s[1:])]+[str.upper(s[0])+ x for x in cases(s[1:])]
    else:
        return [str.lower(s),str.upper(s)]

    


print(cases('abcB'))