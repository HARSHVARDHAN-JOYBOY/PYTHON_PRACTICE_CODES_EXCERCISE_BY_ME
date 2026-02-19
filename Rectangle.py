class Rectangle:
    length=0
    width=0

    def __init__(self,length,width):
        self.length=length
        self.width=width

    def get_area(self):
        area=self.length*self.width
        print(f"Area of Rectangle is : {area}")
    def get_perimeter(self):        
        peri=2*(self.length+self.width)
        print(f"Perimeter of Rectangle is : {peri}")

length=int(input("Enter value of Length  : "))
width=int(input("Enter the value of Width : "))
rec=Rectangle(length,width)        
rec.get_area()
rec.get_perimeter()