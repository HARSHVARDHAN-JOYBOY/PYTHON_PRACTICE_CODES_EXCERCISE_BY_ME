class Book:
    
    def __init__(self,title,author,price,discount_percent):
        self.title=title
        self.author=author
        self.price=price
        self.discount_percent=discount_percent
    def display(self):
        print(f"Book title is {self.title} and it is written by {self.author} and costs only for {self.price} ruppes")
    def get_discounted_price(self):
        amt=(self.price*self.discount_percent)/100
        discounted= self.price-amt
        print(f" Discounted amount is : {discounted}")

title=input("Enter the name of title !")
author=input("enter the name of author !")
price=int(input("Enter the price of book !"))
Dis=int(input("Enter the discount percentage  !"))
a= Book(title,author,price,Dis)        
a.display()
a.get_discounted_price()