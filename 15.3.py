# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:15:59 2021

@author: Hans
"""

def BoxIt(f): # decorator function
    def wrapper(*args):
        
        text=f(*args).splitlines(True)
        
        size=max(len(x) for x in text)         
        
        return ('+-' + '-'*size + '-+' 
                + '\n| '+ 
                ' |\n| '.join(line + ' '*(size-len(line)) for line in text) 
                + ' |\n' + 
                '+-' + '-'*size + '-+')
        
    return wrapper

@BoxIt
def test():
    return "This\n   is a\n      test"


@BoxIt
@BoxIt
def plus(x, y):
    return "%s + %s = %s" % (x, y, x+y)


print(test())
print(plus(3, 4))