# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 14:08:21 2021

@author: Hans
"""
import numpy as np
import matplotlib.pyplot as plt


vals=np.random.rand(10000,2)

mask=[ dist<1  for dist in np.linalg.norm(vals,axis=1)]

print(sum(mask)/len(mask)*4)

#maskcolor=['r.' if dist<1  else 'b.' for dist in np.linalg.norm(vals,axis=1)]



redvals=np.array([ vals[i]  for i in range(len(vals)) if mask[i] ])

bluevals=np.array([ vals[i]  for i in range(len(vals)) if not mask[i] ])

plt.plot(bluevals[:,0],bluevals[:,1],'b.')

plt.plot(redvals[:,0],redvals[:,1],'r.')

plt.axis('equal')