class emp:
    compony="L&T"
    def __init__(self,name ,sal):
        self.name=name
        self.sal=sal

    # instance method
    def print_info(self):
        print(f"Name is {self.name} and Salary is {self.sal}")

    @staticmethod
    def sum(a,b):
        return a+b
    
    @classmethod
    def print_compony(cls):
        print(cls.compony)
    
    @classmethod
    def change_compony(cls,new_comp):
        cls.compony=new_comp
        


e1= emp("Harsh",100000)
e2= emp("Parth",200000)

print(emp.compony)
print(e1.print_info())
print(e2.print_info())

print(e1.sum(5,7))

e1.print_compony()
e2.print_compony()
e1.change_compony("Lenovo")
e1.print_compony()
e2.change_compony("Acer")
e2.print_compony()