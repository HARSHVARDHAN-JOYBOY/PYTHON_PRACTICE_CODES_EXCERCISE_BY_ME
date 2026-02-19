class emp:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal

    @property
    def first_name(self):
        l= self.name.split(" ")
        return l[0]
        
    @first_name.setter    
    
    def first_name(self,newname):
        l= self.name.split(" ")

        newname2=f"{newname} {l[1]}"
        self.name=newname2

e= emp("jack bhusare",8799)

print(e.first_name)

e.first_name="Harsh"
print(e.name)