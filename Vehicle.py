class Vehicle:
    brand=""
    speed=0
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
        
class car(Vehicle):
    model="" 
    engine=""
    fuel=""
    seats=0
    colour=""

    def __init__(self, brand, speed,model,engine,fuel,seats,colour):
        super().__init__(brand, speed)
        self.model=model
        self.engine=engine
        self.fuel=fuel
        self.seats=seats
        self.colour=colour

    def display(self):
        print(f"CAR Brand : {self.brand}")
        print(f"CAR Model : {self.model}")
        print(f"CAR Engine : {self.engine}")
        print(f"CAR Fuel Type : {self.fuel}")
        print(f"CAR Max Speed : {self.speed}")
        print(f"CAR Colour : {self.colour}")
        print(f"CAR Seats : {self.seats}")

Brand=input("Enter the Brand Of Car ! : ")
Model=input("Enter the Model Of Car ! : ")
Engine=input("Enter the Engine Model Of Car ! : ")
Fuel=input("Enter the Fuel Type Of Car ! : ")
Speed=int(input("Enter the Max Speed Of Car ! : "))
Colour=input("Enter the Colour Of Car ! : ")
Seats=int(input("Enter the Number OF Seats Of Car ! : "))
Supra=car(Brand,Speed,Model,Engine,Fuel,Seats,Colour)        
Supra.display()