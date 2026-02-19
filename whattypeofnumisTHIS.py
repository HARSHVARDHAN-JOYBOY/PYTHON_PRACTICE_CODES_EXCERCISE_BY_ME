class Whnum:
    def __init__(self,num):
         self.num=num

    def armstrong(self):
        n=len(str(self.num))
        temp=self.num
        sum=0

        while temp>0:
            rem=temp %10
            sum=sum+(rem**n)
            temp//=10
        if sum==self.num:
            print("armstrong")
        else:
            print("not")

n=Whnum(153)
n.armstrong()
