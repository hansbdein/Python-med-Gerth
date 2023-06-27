# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:46:58 2021

@author: Hans
"""
from time import time


class Stopwatch:
    '''Documentation of class'''
    laps=[]
    end=False
    
    def start(self):
        self.start=time()
        self.prevlap=time()

    def lap(self):
        
        Stopwatch.laps.append(time()-self.prevlap)
        
        self.prevlap=time()

    def stop(self):
        Stopwatch.end = time()-self.start
        Stopwatch.laps.append(time()-self.prevlap)
        

    def total_time(self):
        if not Stopwatch.end:
            self.stop()
        
        return Stopwatch.end
    
    def lap_times(self):
        
        return Stopwatch.laps
        
    
    
    


x=Stopwatch()
x.start()



