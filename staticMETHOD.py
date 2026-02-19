class MathUtilities:
    @staticmethod
    def add(x,y):
        return x+y
    @staticmethod
    def sq(n):
        return n**2
    

# print(MathUtilities.add(5,10))  it runs without errros if object is not used 
# print(MathUtilities.sq(5))


obj=MathUtilities()
print(obj.add(5,10))
print(obj.sq(5))
