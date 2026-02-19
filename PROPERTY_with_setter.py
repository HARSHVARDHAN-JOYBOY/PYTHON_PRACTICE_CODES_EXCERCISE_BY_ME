class Emp:
    def __init__(self,first,last):
        self.first=first
        self.last=last 

    @property
    def email(self):
        return f"{self.first.lower()}{self.last.lower()}@compony.com"
    
    @property
    def fullname(self):
        return f"Name is {self.first} {self.last}"
    
    @fullname.setter
    def fullname(self,name):
        first,last=name.split(" ")
        self.first,self.last=first,last

e=Emp("Harsh","Bhusare")
print(e.email)

e.fullname="John Smith"
print(e.email)