class palin:
    def __init__(self,num):
        self.num=num

    def palindrome(self):
        temp=self.num
        rev=0
                            #521
        while temp>0:
            rem=temp%10
            rev=(rev*10)+rem
            temp//=10

        if rev==self.num:
            print(" Palindrome!! ")
        else:
            print(" Not ! ")


p=palin(100)
p.palindrome()