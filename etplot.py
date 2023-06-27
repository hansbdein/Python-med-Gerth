# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 14:46:21 2021

@author: Hans
"""
#this code can be run in terminal after all scripts have been run

def average(list_of_values):
    sum(list_of_values) / len(list_of_values)


import numpy as np
average(L) for L in (totalwins1,totalwins2,totalwins3,totalwins4
          ,totalwins5,totalwins6,totalwins7,totalwins8)]

for i in (totalwins1,totalwins2,totalwins3,totalwins4,totalwins7,totalwins8):
    
    plt.plot(range(5,19),np.histogram(i,bins=range(5,20))[0]/10000,'.-')

plt.legend(['Egocentric Prügl','With Gentleman rule','With Trash','Give to lowest','With advanced rules','experimental rules'],loc='upper right')
   


plt.savefig('E.png',bbox_inches='tight')