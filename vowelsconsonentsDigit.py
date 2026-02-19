class check:
    def __init__(self,str1):
        self.str1=str1

    def ch(self):
        sp,vc,cc,di=0,0,0,0
        for i in self.str1:
            if i==" ":
                sp+=1
            elif i in "aeiou":
                vc+=1
            elif i in "0123456789":
                di+=1
            else :
                cc+=1
        print(f"\n Total Vowels are : {vc} \n")
        print(f"\n Total Consonants are : {cc} \n")
        print(f"\n Total Digits are : {di} \n")
        print(f"\n Total space are : {sp} \n")


chh=input("\n Enter a random string !! ")
c=check(chh)
c.ch()


