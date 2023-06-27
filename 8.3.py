# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:57:29 2021

@author: Hans
"""




    
def relabel(tree,new_names): 
    return tuple([relabel(x,new_names) if type(x) is tuple  
                  else new_names[x] if x in new_names.keys() else x for x in tree])  
 
    
relabel(('a', ('b', 'c')), {'a': 'x', 'c': 'y'})


'''
def relabel(tree,new_names): 
    return tuple([new_names[x] if x in new_names.keys() 
                  else relabel(x,new_names) if type(x) is tuple else x for x in tree])
'''