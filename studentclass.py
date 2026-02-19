class Stud:
    Name=""
    Roll=0
    Marks=0
    def display(self):
        print(f"Name: {self.Name} Roll Number: {self.Roll} Marks: {self.Marks}")
    def is_passed(self):
        if self.Marks >=40:
            print(f"Student {self.Name} is Passed! ")
        else :
            print(f"Student {self.Name} is Failed! ")      

#Student 1
a= Stud()
a.Name="Parth"    
a.Roll=1
a.Marks=99              

#Student 2
b= Stud()
b.Name="Kaido"  
b.Roll=10
b.Marks=36 

a.display()
a.is_passed()

b.display()
b.is_passed()
