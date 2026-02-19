def main():
    l1=list(map(int,input("Enter elements : ").split()))
    print(l1)
    i,j=0,0
    for i in range(len(l1)-1):
        for j in range(len(l1)-i-1):
            if(l1[j]>l1[j+1]):
                temp=l1[j]
                l1[j]=l1[j+1]
                l1[j+1]=temp

    print(l1)

if __name__=="__main__":
    main()