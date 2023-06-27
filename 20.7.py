# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 18:09:35 2021

HANDIN 10 (random walk)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon solution:

Den første del var næsten triviel at løse, ud over at jeg brugte flere timer på
at indse at jeg skulle yielde tuple(p) frem for p for at undgå pointer ting.

Til del b skulle jeg bytte om på ymax og ymin i extent argumentet, 
ved ikke hvorfor, men det virker nu. Jeg så ikke hintet om collections.Counter,
men list comprehension er sjovere.

"""


from random import randint
import matplotlib.pyplot as plt; 
from itertools import islice



def random_walk():
    p=[0,0]   
    while True:       
        p[randint(0,1)]+= 2*randint(0,1) -1
        yield tuple(p)

    
L=list(islice(random_walk(),0,1000))




((xmin,xmax),(ymin,ymax))=((min(xy),max(xy)) for xy in list(zip(*L)))

LL=[[0]*(xmax-xmin+1) for i in range((ymax-ymin+1))]

#LL[-min(y)][-min(x)] +=30
for (x,y) in L:
    print(x,y)
    LL[y-ymin][x-xmin]+=1 


plt.imshow(LL, extent=(xmin,xmax,ymax,ymin)); plt.colorbar(); plt.show()
