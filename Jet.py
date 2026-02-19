class plane:
    brand=""
    role=""
    origin=""
    def __init__(self,brand,role,origin):
        self.brand=brand
        self.role=role
        self.origin=origin


class jet(plane):
    model=""
    loadcapacity=""
    maxspeed=""
    afterburner=""
    engin=""

    def __init__(self, brand, role, origin,loadcapacity,maxspeed,afterburner,engine,model):
        super().__init__(brand, role, origin)
        self.model=model
        self.loadcapacity=loadcapacity
        self.maxspeed=maxspeed
        self.afterburner=afterburner
        self.engine=engine

    def display(self):    
        print(f"Brand is :{self.brand} !")
        print(f"Role Of this figher jet is {self.role} !")
        print(f"And this plane is orignated in {origin} !")
        print(f"The Model Was named as {model} !" )
        print(f"Maximum Load Capacity is : {loadcapacity} !")
        print(f"Maxspeed is {maxspeed} !")
        print(f"And it touches upto {afterburner} After-burner !")
        print(f"Cause it have {engin} Engin one of the finest works of mankind !")

brand=input("Enter The Brand : ")
role=input("Enter The Role : ")
origin=input("It is Originated from which country : ")
model=input("Enter The Model Name : ")
loadcapacity=input("Enter The loadcapacity : ")
maxspeed=input("Enter the Maxspeed : ")
afterburner=input("Enter The After Burners Speed : ")
engin=input("Engine Infromation  : ")
MMRCA=jet(brand,role,origin,model,loadcapacity,maxspeed,afterburner,origin)        
MMRCA.display()
