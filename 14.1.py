# -*- coding: utf-8 -*-
"""
HANDIN 7 (convex hull)

This handin is done by:

    201706079 Hans Brüner Dein

Reflection upon resubmission

Jeg kan ikke se hvordan jeg skulle bruge docstring på en random_points,
da outputtet jo helst altid skal være forskelligt.

resten af tests og asserts er minimal effort, da jeg har påskeferie


"""

from random import random
import  matplotlib.pyplot as plt



def random_points(n):
    assert isinstance(n,int), 'invalid input'
    return [(random(),random()) for x in range(n)]

def plot_Hull(points,polygon):
    plt.plot(*list(zip(*polygon,polygon[0])), "r-",markersize=6) #plotter polygonen
    plt.plot(*list(zip(*points)), "go")                          #plotter punkterne
    plt.plot(*list(zip(*polygon,polygon[0])), "ro",markersize=3) #plotter punkter i polygonen
    plt.show()



def convex_hull(points):
    """This function computes the convex hull of a set of points in the plane.
    
    Assumes that points is a list of tuples with two elements each
    returns a clockwise ordered subset of points representing the vertices of the convex hull
    
    Examples:
    >>> convex_hull([(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)])
    [(1, 1), (1, 1.5), (2, 3), (3, 2), (2, 1.25)]
    
    >>> convex_hull([(3,-2), (1,3), (0,0), (-6,2), (1.5, 2.25), (2, 2.25), (0, 1.25), (1, 1.5)])
    [(-6, 2), (1, 3), (2, 2.25), (3, -2)]
    """
    
    assert isinstance(points,list) and all(isinstance(x,tuple) and len(x)==2 for x in points) , 'invalid input'
    
    start = sorted(points)[0]       #finder CH[0]
    
    currentp = start                #sætter CH[0] som start 
    poly = []
    nextp = None
    
    while nextp != start:           #kører igennem alle punkter i polygonen
        
        for point in points:        #kører igennem alle punkterne
            nextp=point             #sætter midlertidigt det punkt vi tester som det næste punkt i polygonet
            if all(left_turn(currentp, nextp, x) for x in points): 
                break               #stopper løkken når det næste punkt er fundet

        currentp=nextp              #går videre til det fundne punkt
        poly.append(nextp)          #sætter det næste punkt ind i polygonet
    
    poly.reverse()                  #ændre mod til med uret
    

    #fjern elementer på linjer
    for i in range(1, len(poly)-2):     
        if on_line(poly[i-1], poly[i], poly[i+1]):
            poly.pop(i)
            
    if on_line(poly[-2], poly[-1], poly[0]):
        poly.pop(-1)      
    
   
    return poly
    

def left_turn(p, q, r):
    """
    Examples:
    >>> left_turn((1, 1), (1, 1.5), (2, 3))
    False
    
    >>> left_turn((1, 1.5), (1, 1.5), (2, 3))
    False
    
    >>> left_turn((1, 1), (2, 3), (1, 1.5))
    True
    """
    
    assert isinstance(q,tuple), 'invalid input'
    assert isinstance(p,tuple), 'invalid input'
    assert isinstance(r,tuple), 'invalid input'
    
    
    return False if p==q else (q[0]-p[0]) * (r[1]-p[1]) - (r[0]-p[0]) * (q[1]-p[1]) >= 0   

def on_line(p, q, r):
    """
    Examples:
    >>> on_line((1, 1), (1, 1.5), (2, 3))
    False
    
    >>> on_line((-1, 1), (1, 1), (2, 2))
    False
    
    >>> on_line((-1, -1), (1, 1), (2, 2))
    True
    """
    assert isinstance(q,tuple), 'invalid input'
    assert isinstance(p,tuple), 'invalid input'
    assert isinstance(r,tuple), 'invalid input'
    
    return (q[0]-p[0]) * (r[1]-p[1]) - (r[0]-p[0]) * (q[1]-p[1]) == 0 

points=[(3,2), (1,1), (2,3), (2,2), (1.5, 2.25), (2.5, 2.25), (2, 1.25), (1, 1.5)]

plot_Hull(points,convex_hull(points))

import doctest
doctest.testmod(verbose=True)


