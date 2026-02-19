# class Circle:
#     r=1.0
#     pie=3.14
#     area=0
#     circum=0
#     def get_area(self,r):
#         self.area=self.pie*(r*r) 
#         print(f"{self.area}")
#     def get_circum(self,r):
#         self.circum=2*self.pie*r
#         print(f"{self.circum}")    
    
# a= Circle()
# a.r=int(input("enter radious"))
# a.get_area(a.r)
# a.get_circum(a.r)    

class circle:
    pie= 3.14
    def __init__(self,r=1.0):
        self.r=r
        self.area=0
        self.circum=0

    def Area(self):
        self.area= self.pie*(self.r**2)
        print(f"Area of Circle is {self.area}") 
    def Circum(self):
        self.circum=2*self.pie*self.r
        print(f"Circumference of Circle is {self.circum}")

rad=float(input("Enter the value of radious : "))
a= circle(rad)
a.Area()
a.Circum()