class Perf:
    # def __init__(self,num):
    #     self.num=num
    @staticmethod
    def perfect(num):
        i=1
        sum=0
        while(i<num):
            if num%i==0:
                sum=sum+i
            i+=1
        if sum==num:
            print(" Perfect num!!! ")
        else :
            print(" Not!!! ")
            
print(Perf.perfect(9))
print(Perf.perfect(5))
print(Perf.perfect(6))