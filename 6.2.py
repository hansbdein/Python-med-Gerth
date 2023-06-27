# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 15:55:00 2021

@author: Hans
"""

import re
txt = open("saxo.txt").read()  
txt = txt.lower()
words = re.split('[^a-z]+', txt)


hist={}
for word in words: 
    if len(word)>5:     
        if word not in hist:
            hist[word] = 0
        hist[word]+=1
    


for i in range(10):
    print((sorted(list(zip(hist.values(),hist.keys())))[::-1])[i])
    
    
#print((sorted(list(zip(hist.values(),hist.keys())))[::-1])[:10])