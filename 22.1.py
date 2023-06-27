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

def maybeMakeNumber(s):
    """Returns a string 's' into a integer if possible, a float if needed or
    returns it as is."""

    # handle None, "", 0
    if not s:
        return s
    try:
        f = float(s)
        i = int(f)
        return i if f == i else f
    except ValueError:
        return s

import numpy as np

from scipy.optimize import linprog



import csv
FILE='maxflowa.csv'

rows=[]
with open(FILE, 'r', newline="") as infile:
    for row in csv.reader(infile):
        rows.append(row)



source=rows[0][0]
sink=rows[0][1]
edges=[[maybeMakeNumber(s) for s in edge] for edge in rows[1:]]



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
FILE='maxflowb.csv'

rows=[]
with open(FILE, 'r', newline="") as infile:
    for row in csv.reader(infile):
        rows.append(row)
        
        
source=rows[0][0]
sink=rows[0][1]
flow=int(rows[0][2])
edges=[[maybeMakeNumber(s) for s in edge] for edge in rows[1:]]



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

