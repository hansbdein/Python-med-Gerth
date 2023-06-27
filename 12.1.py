# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:46:54 2021

@author: Hans
"""




from math import pi, sqrt



class Shape:
   
    def fatness(self) :
    
        return 4*pi*self.area()/self.perimeter()**2
    


class Circle(Shape):
    def __init__(self,radius=0,x=0,y=0):
        self.x = x
        self.y = y
        self.radius=radius
    
    
    def area(self):
        return self.radius**2*pi
    
    def perimeter(self):
        return self.radius*2*pi
    
    def __str__(self):
        return ("Circle(radius=%s, center=(%s, %s))" % (self.radius,self.x, self.y))
    
    def contains(self,x=0,y=0):
        
        return True if sqrt((x-self.x)**2+(y-self.y)**2)<self.radius else False
            
        
    
    
class Rectangle(Shape):
    def __init__(self,x_min=0,x_max=0,y_min=0,y_max=0):
        self.x = x_max-x_min
        self.y = y_max-y_min
        self.x_min=x_min
        self.x_max=x_max
        self.y_min=y_min
        self.y_max=y_max
        
      
    
    def area(self):
        return self.x*self.y
    
    def perimeter(self):
        return 2*(self.x+self.y)
    
    def __str__(self):
        return ("Rectangle((%s, %s), (%s, %s))" % (self.x_min,self.y_min,self.x_max, self.y_max))
    
    def contains(self,x=0,y=0):
        
        return False if self.x_min > x > self.x_max and self.y_min > y > self.y_max  else True
        
class Triangle(Shape):
    def __init__(self,x0=0, y0=0, x1=0, y1=0, x2=0, y2=0):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
      
    
    def area(self):
        return abs(self.x1*self.y0+self.x2*self.y1+self.x0*self.y2
                -(self.x1*self.y2+self.x2*self.y0+self.x0*self.y1))/2
    
    def perimeter(self):
        return (sqrt((self.x0-self.x1)**2+(self.y0-self.y1)**2)
                +sqrt((self.x0-self.x2)**2+(self.y0-self.y2)**2)
                +sqrt((self.x2-self.x1)**2+(self.y2-self.y1)**2))
    
    def __str__(self):
        return ("Triangle((%s, %s), (%s, %s), (%s, %s))" % (self.x0, self.y0,self.x1,self.y1,self.x2, self.y2))
    
    def contains(self,x=0,y=0):
        return True if (Triangle(x,y,self.x1,self.y1,self.x2,self.y2).area()
                       +Triangle(self.x0,self.y0,x,y,self.x2,self.y2).area()
                       +Triangle(self.x0,self.y0,self.x1,self.y1,x,y).area()
                       ) == self.area() else False




shapes = [Rectangle(0,10,0,1), Circle(4,1,4), Triangle(1,2,1,4,2,3)]

#[str(s) for s in shapes]
#[s.area() for s in shapes]
#[s.perimeter() for s in shapes]
#[s.fatness() for s in shapes]
#[s.contains(1,1) for s in shapes]

