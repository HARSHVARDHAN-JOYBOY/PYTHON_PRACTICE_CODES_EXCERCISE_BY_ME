def sort(l1):
    i,j=0,0

    for i in range(len(l1)-1):
        for j in range(len(l1)-i-1):
            if(l1[j]>l1[j+1]):
                # temp=l1[j]
                # l1[j]=l1[j+1]
                # l1[j+1]=temp
                # or 
                l1[j],l1[j+1]=l1[j+1],l1[j]




def main():
    low=0
    l1=list(map(int,input("Enter a list to binary search ").split()))
    sort(l1)
    high=len(l1)-1
    key=int(input("Enter a number to search: "))
    while(low<=high):
        # mid=int((low+high)/2)
        # or using floor division
        mid=(low+high)//2
        if(l1[mid]==key):
            print(f"Element found : {l1[mid]}")
            return
        elif(key>l1[mid]):
            low=mid+1
        else :
            high=mid-1
    print("Element not found !")


if __name__=="__main__":
    main()