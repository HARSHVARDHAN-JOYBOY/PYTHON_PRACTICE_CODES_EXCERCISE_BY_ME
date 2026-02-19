class Bank:
    def __init__(self,owner,accno,balence):
        self.owner,self.accno,self.balence=owner,accno,balence

    def deposite(self ,amount):
        self.balence+=amount
        print(f"Dear {self.owner} in your Account (NO:{self.accno}) Rupees {amount} is Debited Succesfully !!!")
        return f"Dear Customer your Current Balence = {self.balence}"


    def withdraw(self,amount):
        if amount>self.balence:
            return "Insufficent Balence !!! "
        self.balence-=amount
        return f"{amount} was Succesfully withdrawed from your account no:{self.accno} !!!"

    def view(self):
        return f"Dear Customer AcNo:{self.accno} your curent Bal is : n{self.balence} !!!"


acc1=Bank("Harshvardhan",102030,100000)
print(acc1.deposite(10000))
print(acc1.withdraw(11000))
print(acc1.view())