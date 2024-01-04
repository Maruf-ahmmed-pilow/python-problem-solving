import math


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length*self.width 
    
class Circle:
    def __init__(self,radious):
        self.radious = radious
        
    def area(self):
        return math.pi*(self.radious**2)
    
    