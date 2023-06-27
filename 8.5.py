# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:57:49 2021

if b[1] and b[0]:
         return b
     elif b[0]==None:
         return b[1]
     else:
         return b[0]


@author: Hans



def extract(tree, leaves):
     
     b= tuple(x if x in leaves else extract(x,leaves) if isinstance(x,tuple) else None for x in tree) #laver forkerte blade om til None
     
     return b if b[1] and b[0] else b[1] if b[1] else b[0] #klipper None af


"""






def extract(tree, leaves):
    
    for i in range(len(tree)):
        if isinstance(tree[i],tuple) :
            tree[i]=extract(tree[i],leaves)

    

'''

def extract(tree, leaves):
     
     b= tuple(x if x in leaves else extract(x,leaves) if isinstance(x,tuple) else None for x in tree) #laver forkerte blade om til None
     
     return b if b[1] and b[0] else b[1] if b[1] else b[0] #klipper None af



def extract(tree, leaves): return  tuple(x if x in leaves else extract(x,leaves) if isinstance(x,tuple) else None for x in tree) if tuple(x if x in leaves else extract(x,leaves) if isinstance(x,tuple) else None for x in tree)[1] and tuple(x if x in leaves else extract(x,leaves) if isinstance(x,tuple) else None for x in tree)[0] else tuple(x if x in leaves else extract(x,leaves) if isinstance(x,tuple) else None for x in tree)[1] if tuple(x if x in leaves else extract(x,leaves) if isinstance(x,tuple) else None for x in tree)[0]==None else tuple(x if x in leaves else extract(x,leaves) if isinstance(x,tuple) else None for x in tree)[0]#ses tydeligt



'''




print(extract(((('a', 'b'), 'c'), ((('d', 'e'), 'f'), 'g')), {'a', 'c', 'd', 'f', 'g'}))
#def extract(tree, leaves):
    
print(extract(((('a', 'b'), 'c'), ((('d', 'e'), 'f'), 'g')), { 'c', 'd', 'f', 'g'}))   