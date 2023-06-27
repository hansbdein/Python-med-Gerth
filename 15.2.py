# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:35:38 2021

@BoxIt
def plus(x, y):
    return "The sum of %s and %s is %s" % (x, y, x + y)

print(plus(3,4))

---------------------------
| The sum of 3 and 4 is 7 |
---------------------------


"""


def BoxIt(f): # decorator function
    def wrapper(*args):
        
        
        return ('-'*(len(f(*args))+4) + '\n'
                 + '| '+f(*args)+' |' + '\n'
                 + '-'*(len(f(*args))+4))
        
    return wrapper

@BoxIt
def plus(x, y):
    return "The sum of %s and %s is %s" % (x, y, x + y)



