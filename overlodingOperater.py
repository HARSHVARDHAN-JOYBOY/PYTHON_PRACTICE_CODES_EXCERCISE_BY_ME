class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self, p):
        return point((self.x + p.x),(self.y + p.y ))
    def print_points(self):
        print(f"X ix {self.x} and Y is {self.y}")
    def __add__(self , p):
        return point((self.x + p.x),(self.y + p.y ))

p1= point(3, 2)
p2= point(6, 3)

# p=p1.sum(p2)
p= p1+p2
p.print_points()


