class Circle:
    def __init__(self,radius):
        self.r=radius

    @property
    def radius(self):
        return self.r


    @property
    def area(self):
        import math
        return math.pi*(self.r**2)
    


c=Circle(5)
print(c.radius)
print(c.area)