class school:
    def __init__(self,roll,name):
        self.roll=roll
        self.name=name

    @property
    def full_name(self):
        l=self.name.split(" ") 
        # l2=l[1]+l[2]
        return l[0]
    
    @full_name.setter
    def full_name(self,newname):
        l=self.name.split(" ")
        newname2= f"{newname} {l[1]} {l[2]}"
        self.name= newname2

s= school(1,"Harshvardhan Avinash Bhusare")
print(s.name)
print(s.full_name)
s.full_name="Parth"
print(s.name)


