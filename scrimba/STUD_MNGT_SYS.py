# Illustrate the development of a Python application utilizing various programming constructs
# and Object-Oriented Programming principles.

# Design a that stores student details, calculates total marks and grade, and displays results using Python programming constructs and OOP concepts.

# Create the required classes using OOP principles.
# Use loops to accept subject marks.
# Apply conditional statements to calculate grades.
# Create objects and demonstrate method calls.
# Ensure proper code structure and readability.

class Student:
    def __init__(self,roll,name):
        self.__roll=roll
        self.__name=name 

    def getroll(self):
        return self.__roll
    def getname(self):
        return self.__name
    
    def display(self):
        print("--Student Details--")


class Result(Student):
    def __init__(self, roll, name, marks,age):
        super().__init__(roll, name)
        self.__marks=marks
        self.__age=age


    def total_marks(self):
        return sum(self.__marks)
    def percentage(self):
        return self.total_marks()/(len(self.__marks) *100)*100
    

    def grade(self):
        per=self.percentage()

        if 100>=per>=90:
            return "O grade"
        elif 90>per>=80:
            return "A grade"
        elif 80>per>=70:
            return "B grade"
        elif 70>per>=50:
            return "C grade"
        elif 50>per>=35:
            return "D grade"
        elif per<35:
            return "F Fail"
        else :
            return "Wrone value"

    
    def display(self):
        print("--Student result--")
        print(f"\nRoll No: {self.getroll()}")
        print(f"\nName : {self.getname()}")
        print(f"\nAge : {self.__age}")
        print(f"\nTotal Marks : {self.total_marks()}")
        print(f"\nPercentage : {self.percentage()}")
        print(f"\nGarade : {self.grade()}\n")


roll=input("Enter the roll Number  : ")
name=input("Enter the name of Student : ")
age=int(input("Enter the Age of Student : "))
marks=[]

subs=int(input("Enter how many Sujects are there :  "))
for i in range(subs):
    m=int(input(f"Enter the marks of Subject no {i+1} : "))
    marks.append(m)

s1=Result(roll,name,marks,age)
s1.display()