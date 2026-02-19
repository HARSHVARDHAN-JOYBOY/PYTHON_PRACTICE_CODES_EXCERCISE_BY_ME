class Bank_acc:
    Acc_Holder=""
    Bal=0
    amt=0
    def depo(self,amt):
        self.Bal+=amt
    def withdraw(self,amt):
        self.Bal-=amt
    def display_bal(self):
        print(f"Balance of User {self.Acc_Holder} is {self.Bal}")   

a=Bank_acc()
a.Acc_Holder="Parth Pallavi Avinash Bhusare"
a.Bal=999900
a.amt=int(input("Enter amount to deposite : "))
#a.depo(900)
#a.withdraw(1800)   
a.display_bal()
a.depo(a.amt)
a.display_bal()
a.amt=int(input("Enter amount to withdraw : "))
a.display_bal()
a.withdraw(a.amt)
a.display_bal()