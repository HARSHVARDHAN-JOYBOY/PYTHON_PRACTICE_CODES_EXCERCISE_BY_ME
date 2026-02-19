import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement this method")

class Rectangle(Shape):
    def __init__(self,width,height):
        self.width=width
        self.height=height

    def area(self):
        return self.width*self.height
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return math.pi * (self.radius**2)
    
shapes = [Rectangle(4, 5),Circle(4)]
for shape in shapes:
    print(f"{shape.__class__.__name__} area: {shape.area():.2f}")
        
        



