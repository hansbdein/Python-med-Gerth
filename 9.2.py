# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 21:42:00 2021

@author: Hans
"""

def print_tree(T,depth=0):
    for node in T:
        if isinstance(node,str):
            print('  |'*depth +'--'+node)
        else:
            print_tree(node,depth+1)