class Employee:
    name=""
    salary=0     
    designation="" 
    
    def __init__(self,name,salary,designation):
        self.name=name
        self.salary=salary
        self.designation=designation

    def give_raise(self,amount):
        amt= (self.salary*amount)/100
        amount=self.salary+amt
        print(f"New Salary For Shri {self.name} is {amount}")
    def Display(self):
        print(f"NAME : {self.name}")
        print(f"SALARY : {self.salary}")
        print(f"DESIGNATION : {self.designation}")



Name= input("Enter the name of new Employee : ")
Salary= int(input("Enter the Amount of Salary to give this Employee ! :"))
Designation=input("Enter the Designation of this Employee ! : ")
golu = Employee(Name,Salary,Designation)
golu.Display()
Amount=int(input("Enter the Percentage of Increase In Salary : "))
golu.give_raise(Amount)










