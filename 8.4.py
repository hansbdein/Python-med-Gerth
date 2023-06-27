# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:57:38 2021

@author: Hans
"""

#def validate_string_tuple(t):
    
#    return all([validate_string_tuple(x) if type(x) is tuple else x for x in t ])



def validate_string_tuple(t):
    L=[]
    def emptycheck(t):
        return all([emptycheck(x) if type(x) is tuple else 0 if x in L else L.append(x) or isinstance(x,str) and x for x in t ]) 
    
    return emptycheck(t)



def valid_binary_tree(t):
     if len(t)==2:
         return all([valid_binary_tree(x) if type(x) is tuple else True for x in t ])
     else:
         return False