class BankAccount:
    Total_Accounts=0
    def __init__(self,account_no,holder_name,balance):
        self.__account_no=account_no
        self.__holder_name=holder_name
        self.__balance=balance
        BankAccount.Total_Accounts+=1

    def deposit(self,amt):
        self.__balance+=amt
        print(f"Balance Updated of Mr./Ms./ShriMT.{self.__holder_name}")





    def withdraw(self,amt):
        self.__balance-=amt
        print(f"For Account:{self.__account_no} the amount {amt} is Debited.")




    def display_details(self):
        print(f"Holder : Mr./Ms./ShriMT.{self.__holder_name} \nAccount Number : {self.__account_no} \nAvailable Balance : {self.__balance}\n")
    @classmethod
    def TotalAccountsmade(self):
        print(f"Total Accounts made on this accounts are : {BankAccount.Total_Accounts}")


s1=BankAccount(101,"rajsoni",1000)
s1.display_details()
s1.deposit(100)
s1.display_details()
s1.withdraw(200)
s1.display_details()
s2=BankAccount(102,"chetandeshmukh",190090)
s2.display_details()
s2.deposit(10000)
s2.display_details()
s2.withdraw(15000)
s2.display_details()
s3=BankAccount(103,"sanketgite",8000000)
s3.display_details()
s3.deposit(18)
s3.display_details()
s3.withdraw(39)
s3.display_details()


BankAccount.TotalAccountsmade()