# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:46:56 2021

@author: Hans
"""

class PersonReader:
   
    def input_person(self):
        
        self.name=input("Name: ")
        self.year=input("Year of birth: ")
        
    def __str__(self):
       return ("%s (%s)" % (self.name, self.year))
   