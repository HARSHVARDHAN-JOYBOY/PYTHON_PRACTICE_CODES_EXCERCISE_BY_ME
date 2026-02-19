class Library:
    def __init__(self):
        self.books=[]
        self.no_of_books=0
    def add(self,book_name):
        self.books.append(book_name)
        self.no_of_books+=1   
    def delete(self,book_name):
        pass
    def get_books(self):
        return self.books
    def get_book_count(self):
        return self.no_of_books
    
my_lab= Library()
while (True):
    b=input("Want to add books !! type 'add' if you want to see all books type 'see' if you want to see number of total books type 'no'").lower()
    if(b=="add"):    
        a=input("enter the name of book ! ")
        my_lab.add(a)
    elif(b=="see"):
        a=my_lab.get_books()
        for b in a:
            print(f" ",b)
    elif(b=="no"):

        print(my_lab.get_book_count())
    else:
        exit()    

