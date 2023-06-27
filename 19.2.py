# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 14:58:59 2021

HANDIN 9 (maximum flow)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

Først så jeg den første halvdel af forlæsningen, og lavede koden.
Herfeter implementerede jeg c, A_ub, b_ub, b_eq og sidst A_eq.
for del b tilføjede jeg en eq for A of F.
Selvom løsningen til både har mange constraints, som effektivt siger 0==0, er 
det kun i b hvor der kommer en advarsel.

"""



import numpy as np

from scipy.optimize import linprog



#Original code
'''
c=np.array([0,0,0,0,0,0,0,1,1])

A_ub=np.array(np.identity(9))
b_ub=np.array([4,3,1,1,3,1,3,1,5])

A_eq=np.array([[0,-1,0,0,1,1,0,0,0],
               [-1,0,1,1,0,0,0,0,0],
               [0,0,0,-1,0,-1,-1,0,1],
               [0,0,-1,0,-1,0,1,1,0]])
b_eq=np.array([0,0,0,0])

result=linprog(-c,A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq)
'''



#input
edges = [('A', 'C', 4),
         ('A', 'B', 3),
         ('C', 'E', 1),
         ('C', 'D', 1),
         ('B', 'E', 3),
         ('B', 'D', 1),
         ('E', 'D', 3),
         ('E', 'F', 1),
         ('D', 'F', 5),
        ]

source = 'A'

sink = 'F'

#kode til del a
nodes=[]
for edge in edges:
    if edge[0] not in nodes:
        nodes.append(edge[0])
    if edge[1] not in nodes:
        nodes.append(edge[1])        



edges=np.array(edges)

c=np.array([1 if edge[1]==sink else 0 for edge in edges])

A_ub=np.array(np.identity(9))

b_ub=edges[:,2]

A_eq=np.array([[-1 if edge[1]==node else 
                 1 if edge[0]==node else 
                 0 for edge in edges] 
               for node in nodes if node!=source and node!=sink])


b_eq=np.array([0]*len(A_eq))

result=linprog(-c,A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq)


print("Max flow is %.2f " % (-result.fun))
print("Flow rates are" ,np.round(result.x, 3))

print(' ')




#kode til del b
edges = [('A', 'C', 4, 1),
         ('A', 'B', 3, 1),
         ('C', 'E', 1, 1),
         ('C', 'D', 1, 1),
         ('B', 'E', 3, 1),
         ('B', 'D', 1, 1),
         ('E', 'D', 3, 0),
         ('E', 'F', 1, 1),
         ('D', 'F', 5, 2),
        ]

source = 'A'
sink = 'F'
flow = 4

edges=np.array(edges)
c=edges[:,3]

A_ub=np.array(np.identity(9))

b_ub=edges[:,2]

A_eq=np.array([[-1 if edge[1]==node else 
                 1 if edge[0]==node else 
                 0 for edge in edges] 
                for node in nodes])

b_eq=np.array([flow if node==source else -flow if node==sink else 0 for node in nodes])

result=linprog(c,A_ub=A_ub,b_ub=b_ub,A_eq=A_eq,b_eq=b_eq)

print("Minimun cost is %.2f " % (result.fun))
print("Flow rates are" ,np.round(result.x, 3))

