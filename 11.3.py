# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:46:58 2021

@author: Hans
"""
from math import sqrt

class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def length(self):
        return sqrt(self.x**2+self.y**2)
    
    def add(self,other):
        return Vector(other.x+self.x,other.y+self.y)
    
    def __add__(self,other):
        return self.add(other)
    
    def mult(self,factor):
        return Vector(self.x*factor, self.y*factor)
    
    def dot(self,other):
        return Vector(other.x*self.x,other.y*self.y)
    
    def __mul__(self,other):
        if isinstance(other,Vector): 
            return self.dot(other)
        else:
            return self.mult(other)
        
    def __rmul__(self,factor):
        return self.mult(factor)
         
         
    def __str__(self):
        return ("<%s, %s>" % (self.x, self.y))
     

b=Vector(3,4)
