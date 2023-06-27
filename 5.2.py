# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 13:58:57 2021

@author: Hans
"""

first = ['Donald', 'Mickey', 'Scrooge']

last = ['Duck', 'Mouse', 'McDuck']



print([name[0] +', '+ name[1]  for name in sorted(list(zip(last,first)))])



#print(sorted([last[i]+', '+first[i] for i in range(len(first))]))