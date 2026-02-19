class hospital:
    def __init__(self,dname,hosp):
        self.dname=dname
        self.hosp=hosp

    @property
    def doc(self):
        l=self.dname.split(" ")
        return l[0]
    
    @doc.setter
    def doc(self,newd):
        l=self.dname.split(" ")
        new2=f"{newd} {l[1]} {l[2]}"
        self.dname=new2

d= hospital("champak tampak Jadhav","Jadhav Clinic")

print(d.dname)
print(d.doc)
d.doc="Pampak"
print(d.doc)
print(d.dname)